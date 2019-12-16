import json
from urllib.error import HTTPError
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request

from Levenshtein import ratio

import bibtexparser


def crossref_query_title(title):
    EMPTY_RESULT = {
        "crossref_title": "",
        "similarity": 0,
        "doi": ""
    }
    api_url = "https://api.crossref.org/works?"
    params = {"rows": "5", "query.bibliographic": title}
    url = api_url + urlencode(params, quote_via=quote_plus)
    request = Request(url)
    request.add_header("User-Agent",
                       "OpenAPC DOI Importer (https://github.com/OpenAPC/openapc-de/blob/master/python/import_dois.py; mailto:openapc@uni-bielefeld.de)")
    try:
        ret = urlopen(request)
        content = ret.read()
        data = json.loads(content)
        items = data["message"]["items"]
        most_similar = EMPTY_RESULT
        for item in items:
            title = item["title"][0]
            result = {
                "crossref_title": title,
                "similarity": ratio(title.lower(), params["query.bibliographic"].lower()),
                "doi": item["DOI"]
            }
            if most_similar["similarity"] < result["similarity"]:
                most_similar = result
        return {"success": True, "result": most_similar}
    except HTTPError as httpe:
        return {"success": False, "result": EMPTY_RESULT, "exception": httpe}


if __name__ == '__main__':

    with open('../_bibliography/pint.bib', 'r') as bibtex_file:
        db = bibtexparser.load(bibtex_file)

    string = ''

    for item in db.get_entry_list():
        # if not 'doi' in item:
        if item['ENTRYTYPE'] == 'unpublished':
            title = item['title'].replace('{', '').replace('}','')
            output = crossref_query_title(title)
            if output['success'] and output['result']['similarity'] > 0.9:

                string += '- [ ] ID: ' + item['ID'] + '\n'
                string += 'Current title:  ' + item['title'] + '\n'
                string += 'Crossref title: ' + output['result']['crossref_title'] + '\n'
                string += f"DOI: https://doi.org/{output['result']['doi']}" + '\n\n'

    if string != '':
        string = '---\n' \
                 'title: DOI found for unpublished results\n' \
                 'assignees: pancetta\n' \
                 '---\n' \
                 'Hi there, I found some papers which are listed as unpublished, but which now have a DOI. ' \
                 'Please check the list below and mark the ones which are correct. ' \
                 "Add the label 'food for arxivbot' when you are done and I will take care of the rest. " \
                 'Here we go:\n\n' + string
    print(string)
