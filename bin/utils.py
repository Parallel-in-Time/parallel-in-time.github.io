import html
import re
from html.parser import HTMLParser

import requests


class _MetaTagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "meta":
            return

        attrs = dict(attrs)
        name = attrs.get("name")
        content = attrs.get("content")
        if name is not None and content is not None:
            self.meta.setdefault(name, []).append(html.unescape(content).strip())


def fixBadBibFormat(bibString:str)->str:
    """
    Fixes the formatting of a BibTeX entry string by ensuring all field values are enclosed in braces.

    Parameters
    ----------
    bibString : str
        The BibTeX entry string to be fixed. Must start with '@' and end with '}'.

    Returns
    -------
    str
        The corrected BibTeX entry string with all field values enclosed in braces.

    Raises
    ------
    AssertionError
        If the input string does not start with '@' or does not end with '}'.
    """
    bibString = bibString.strip()
    assert bibString.startswith("@") and bibString.endswith("}"), \
        "bib entry should start with '@' and finish with '}', got :\n{bibString}"
    content = bibString[1:-1]
    fields = content.split(",")
    for i, field in enumerate(fields[1:]):
        item = field.split("=")
        if len(item) == 2 and "{" not in item[1]:
            item[1] = "{"+item[1]+"}"
            fields[i+1] = "=".join(item)
    return "@"+",".join(fields)+"}"


def parseArxivPage(html_content:str, url:str, arxiv_id:str):
    parser = _MetaTagParser()
    parser.feed(html_content)
    meta = parser.meta

    def first(*names):
        for name in names:
            values = meta.get(name, [])
            if len(values) > 0:
                return values[0]
        return ""

    title = re.sub(r'\s+', ' ', first("citation_title", "og:title")).strip()
    authors = [re.sub(r'\s+', ' ', author).strip() for author in meta.get("citation_author", []) if author.strip()]
    published = first("citation_date", "citation_publication_date", "citation_online_date").replace("/", "-")
    summary = re.sub(r'\s+', ' ', first("citation_abstract", "description")).strip()
    link = first("citation_abstract_html_url", "citation_public_url") or url

    category = ""
    keywords = first("citation_keywords")
    if keywords:
        category_match = re.search(r'\(([^()]+)\)', keywords.split(";")[0])
        if category_match is not None:
            category = category_match.group(1)

    if not title or len(authors) == 0 or not published or not summary:
        return None

    return {
        "title": title,
        "authors": [{"name": author} for author in authors],
        "published": published,
        "summary": summary,
        "link": link,
        "id": f"https://arxiv.org/abs/{arxiv_id}",
        "arxiv_primary_category": {"term": category},
    }


def getArxivInfoFromPage(url:str, arxiv_id:str):
    req = requests.get(url, timeout=30)
    req.raise_for_status()
    return parseArxivPage(req.text, url, arxiv_id)