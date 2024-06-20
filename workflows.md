# Workflows

This project uses many different workflows to make the development easier and more efficient. This document describes the workflows and how to use them.

## I. [publish.yml](./.github/workflows/publish.yml)

This Workflow publishes the page to GitHub Pages. It is triggered by a push to the `source` branch.

## II. [issue_to_bib.yml](./.github/workflows/issue_to_bib.yml)

Converts the issue to a bibtex entry and adds it to the `pint.bib` file. It is triggered by a new issue that is labeled.

## III. [arxiv_to_publications_correct.yml](./.github/workflows/arxiv_to_publications_correct.yml)

This workflow is triggered when a new issue is opened with the label "food for arxivbot". It runs the script arxiv_to_publications_correct.py, which looks for bibtex entries that now have a Digital Object Identifier (DOI). If it finds any, it creates a pull request with the updated bibtex file. It also adds a comment to the issue with the output of the script.


## IV. [arxiv_to_publications_detect.yml](./.github/workflows/arxiv_to_publications_detect.yml)

This workflow is used to detect DOIs for unpublished results. It uses the title of the unpublished result and queries the Crossref API. If the similarity between the title of the unpublished result and the title of the result returned by the Crossref API is above 0.9, the result is printed to the console. The output can be used to update the bibtex file.
