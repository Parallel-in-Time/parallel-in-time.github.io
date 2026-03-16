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
        id = id.replace(" ", "_")

        entries = db.get_entry_dict()
        assert entries[id_db]["ENTRYTYPE"] == 'unpublished', "original entry in bib file was NOT unpublished !"
        db.entries.remove(entries[id_db])

        # Check for duplicate keys in the remaining database and add letter suffixes if needed
        remaining = db.get_entry_dict()
        id_orig = id
        letters = 'bcdefghijklmnopqrstuvwxyz'
        i = 0
        while id in remaining:
            print(f'Key {id} already exists, augmenting with letter suffix.')
            id = id_orig + letters[i]
            i += 1

        if id != id_db:
            print(f'Note: ID updated from {id_db} to {id} to reflect the publication year.')

        bType, *rest1 = bib.split("{")
        oldID, *rest2 = rest1[0].split(",")
        bib = "{".join([bType] + [','.join([id]+rest2)] + rest1[1:])
        bib_db = bibtexparser.loads(bib)
        db.entries.extend(bib_db.get_entry_list())

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
