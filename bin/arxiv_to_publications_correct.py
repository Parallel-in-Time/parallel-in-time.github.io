import re
import requests
import argparse
import fileinput

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from requests.exceptions import RequestException


def fetch_doi_content(url, accept_header, description):
    try:
        response = requests.get(url, headers={'Accept': accept_header}, timeout=30)
        response.raise_for_status()
    except RequestException as exc:
        print(f'Ignoring {url}, failed to fetch {description}: {exc}\n\n')
        return None
    return response


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
        bibtex_req = fetch_doi_content(url, 'application/x-bibtex', 'BibTeX')
        if bibtex_req is None:
            continue
        meta_req = fetch_doi_content(url, 'application/json', 'metadata')
        if meta_req is None:
            continue
        try:
            data = meta_req.json()
        except ValueError as exc:
            print(f'Ignoring {url}, invalid metadata response: {exc}\n\n')
            continue

        try:
            if len(data['author']) > 1:
                id = data['author'][0]['family'] + 'EtAl' + str(data['issued']['date-parts'][0][0])
            else:
                id = data['author'][0]['family'] + str(data['issued']['date-parts'][0][0])
        except (KeyError, IndexError, TypeError) as exc:
            print(f'Ignoring {url}, incomplete metadata response: {exc}\n\n')
            continue
        id = id.replace(" ", "_")

        entries = db.get_entry_dict()
        if id_db not in entries:
            print(f'Ignoring {id_db}, entry not found in bibliography.\n\n')
            continue
        if entries[id_db]["ENTRYTYPE"] != 'unpublished':
            print(f'Ignoring {id_db}, original entry in bib file was not unpublished.\n\n')
            continue

        # Parse the BibTeX and replace the key before modifying the database
        try:
            bib = bibtex_req.text
            bType, *rest1 = bib.split("{")
            if not rest1:
                print(f'Ignoring {id_db}, DOI did not return valid BibTeX (no opening brace found).\n\n')
                continue
            oldID, *rest2 = rest1[0].split(",")
            # Check for duplicate keys in the remaining database and add letter suffixes if needed
            remaining = db.get_entry_dict()
            del remaining[id_db]  # exclude the entry being replaced from duplicate check
            id_orig = id
            letters = 'bcdefghijklmnopqrstuvwxyz'
            i = 0
            while id in remaining:
                print(f'Key {id} already exists, augmenting with letter suffix.')
                id = id_orig + letters[i]
                i += 1
            if id != id_db:
                print(f'Note: ID updated from {id_db} to {id} to reflect the publication year.')
            bib = "{".join([bType] + [','.join([id]+rest2)] + rest1[1:])
            bib_db = bibtexparser.loads(bib)
            new_entries = bib_db.get_entry_list()
            if not new_entries:
                print(f'Ignoring {id_db}, could not parse BibTeX returned by DOI.\n\n')
                continue
        except Exception as exc:
            print(f'Ignoring {id_db}, error processing BibTeX from DOI: {exc}\n\n')
            continue

        # Only mutate the database once we have a valid replacement entry
        db.entries.remove(entries[id_db])
        db.entries.extend(new_entries)

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
