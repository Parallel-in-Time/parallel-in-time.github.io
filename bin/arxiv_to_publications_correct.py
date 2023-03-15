import re
import requests
import argparse
import fileinput

import bibtexparser
from bibtexparser.bwriter import BibTexWriter


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--body", help="input issue body here", type=str, default="")
    args = parser.parse_args()

    with open('../_bibliography/pint.bib', 'r') as bibtex_file:
        db = bibtexparser.load(bibtex_file)

    id_list = re.findall(r"- \[x\] ID: (.*)\n", args.body.replace('\r', ''))
    doi_list = re.findall(r"- \[x\] ID: .*\n.*\n.*\n.*DOI: (.*)\n", args.body.replace('\r', ''))

    for url, id_db in zip(doi_list, id_list):
        print(f'Working on {id_db} with URL {url}')
        req = requests.get(url, headers={'Accept': 'application/x-bibtex'})
        if not req.status_code == 200:
            print(f'Ignoring {url}, got status code {req.status_code}\n\n')
            continue
        bib = req.content.decode()
        req = requests.get(url, headers={'Accept': 'application/json'})
        if not req.status_code == 200:
            print(f'Ignoring {url}, got status code {req.status_code}\n\n')
            continue
        data = req.json()

        if len(data['author']) > 1:
            id = data['author'][0]['family'] + 'EtAl' + str(data['issued']['date-parts'][0][0])
        else:
            id = data['author'][0]['family'] + str(data['issued']['date-parts'][0][0])

        d = db.get_entry_dict()
        id_orig = id
        letters = 'bcdefghijklmnopqrstuvwxyz'
        i = 0
        duplicate = False
        while id in d:
            for author in data["author"]:
                if 'given' not in author:
                    author["given"] = ''
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

            for item in db.get_entry_list():
                if item['ID'] == id_db and item['ENTRYTYPE'] == 'unpublished':
                    # print(f"removing {item['ID']}")
                    db.entries.remove(item)

            bib = re.sub(r'(@[a-z]*{)(.*),', r'\1' + id + ',', bib)
            bib_db = bibtexparser.loads(bib)
            db.entries.extend(bib_db.get_entry_list())
        else:
            bib_db = None

    if id_list:
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
