import argparse
import re
import requests
import fileinput

from arxivcheck.arxiv import get_arxiv_info

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--body", help="input issue body here", type=str, default="")
    args = parser.parse_args()

    url_list = re.findall(r'(https?://\S+)', args.body)

    if len(url_list) == 0:
        print(f'I did not find any URLs in the text you provided. '
              f'What I got is this:\n\n{args.body}\n\nPlease try again!')
        exit()

    for url in url_list:

        with open('../_bibliography/pint.bib', 'r') as bibtex_file:
            db = bibtexparser.load(bibtex_file)

        url = url.rstrip('.,')
        duplicate = False
        bib_db = None

        if 'arxiv' in url:

            arxiv_id = url.split('/')[-1]
            found, items = get_arxiv_info(arxiv_id, field='id')
            if len(items) > 1:
                print(f'I got more than one item back from arXiv for {url}. See what I got:\n' +
                      '\n'.join([item.title for item in items]) + '\n' +
                      f'I am taking the first one only, just FYI. I hope this is the correct one..\n\n')
            url = items[0].link
            title = items[0].title.replace('\n', '').replace('  ', ' ')
            year = items[0]['published'].split('-')[0]
            authors = items[0].authors
            if len(authors) > 1:
                first_author = authors[0]["name"].split(" ")
                authors = " and ".join([author["name"] for author in authors])
                id = first_author[-1] + 'EtAl' + year
            else:
                first_author = authors[0]["name"].split(" ")
                authors = authors[0]["name"]
                id = first_author[-1] + year

            d = db.get_entry_dict()
            id_orig = id
            letters = 'bcdefghijklmnopqrstuvwxyz'
            i = 0
            while id in d:
                candidate_title = re.sub('[^A-Za-z0-9]+', '', title)
                existing_title = re.sub('[^A-Za-z0-9]+', '', d[id]['title'])
                if authors == d[id]['author'] and candidate_title == existing_title:
                    print(f'I detected a duplicate based on the key {id}, the list of authors and the title for {url}. '
                          f'I will ignore this entry. If this is wrong, sorry for that..\n\n')
                    duplicate = True
                    break
                else:
                    print(f'I detected a duplicate based on the key {id}. '
                          f'I will augment it with a letter and try again. '
                          f'Please double-check, if this is correct.. '
                          f'my duplicate detection algorithm is pretty bad.\n\n')
                    id = id_orig + letters[i]
                    i += 1

            howpublished = "arXiv:" + items[0]["id"].split('/')[-1] + \
                           " [" + items[0]["arxiv_primary_category"]["term"] + "]"

            if not duplicate:
                bib_db = BibDatabase()
                bib_db.entries = [
                    {
                        "ENTRYTYPE": "unpublished",
                        "ID": id,
                        "author": authors,
                        "title": title,
                        "howpublished": howpublished,
                        "url": url,
                        "year": year,
                        "abstract": items[0]['summary'].replace('\n', ' ').replace('  ', ' '),
                    }
                ]
            else:
                bib_db = None

        elif 'doi.org' in url:

            req = requests.get(url, headers={'Accept': 'application/x-bibtex'})
            bib = req.content.decode()
            req = requests.get(url, headers={'Accept': 'application/json'})
            data = req.json()

            if len(data['author']) > 1:
                id = data['author'][0]['family'] + 'EtAl' + str(data['issued']['date-parts'][0][0])
            else:
                id = data['author'][0]['family'] + str(data['issued']['date-parts'][0][0])

            d = db.get_entry_dict()
            id_orig = id
            letters = 'bcdefghijklmnopqrstuvwxyz'
            i = 0
            while id in d:
                authors = " and ".join([author['given'] + ' ' + author['family'] for author in data["author"]])
                candidate_title = re.sub('[^A-Za-z0-9]+', '', data['title'])
                existing_title = re.sub('[^A-Za-z0-9]+', '', d[id]['title'])
                if authors == d[id]['author'] and candidate_title == existing_title:
                    print(f'I detected a duplicate based on the key {id}, the list of authors and the title for {url}. '
                          f'I will ignore this entry. If this is wrong, sorry for that..\n\n')
                    duplicate = True
                    break
                else:
                    print(f'I detected a duplicate based on the key {id}. '
                          f'I will augment it with a letter and try again. '
                          f'Please double-check, if this is correct.. '
                          f'my duplicate detection algorithm is pretty bad.\n\n')
                    id = id_orig + letters[i]
                    i += 1

            if not duplicate:
                bib = re.sub(r'(@[a-z]*{)(.*),', r'\1' + id + ',', bib)
                bib_db = bibtexparser.loads(bib)
            else:
                bib_db = None

        else:
            print(f'The URL {url} does not seem to be an arXiv or '
                  f'a doi.org link. I will ignore it.\n\n')

        if bib_db is not None:
            db.entries.extend(bib_db.get_entry_list())
            writer = BibTexWriter()
            writer.indent = '\t'
            writer.order_entries_by = ('year', 'ID')
            writer.add_trailing_comma = True
            with open('../_bibliography/pint.bib', 'w') as bibfile:
                bibfile.write(writer.write(db))

            for line in fileinput.input('../_bibliography/pint.bib', inplace=True):
                if '@comment{' in line:
                    line = line.replace('@comment{', '')
                if re.match(r'%}+', line) is not None:
                    line = re.sub(r'%}+', '%', line)
                line = line.rstrip('\r\n')
                print(line)
