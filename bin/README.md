# Script development guidelines

## Testing your changes

Before pushing you changes, create a `test.sh` file in this folder with this content :

```sh
#!/bin/bash

BODY="" # -> put there the content of the issue

python $SCRIPT_NAME -b "${BODY}"
```

- from github, copy-paste the issue body using the "..." icon and `Copy Markdown`
- replace $SCRIPT_NAME by the script you want to test, like `issue_to_bibtex.py`, `arxiv_to_publications_correct.py`, ...

Then, check that the modification of the `_bibliography/pint.bib` file is correct.
You can commit the changes on the `pint.bib` file (done now, no need to do it again), or reset those and trigger the scripts on Github using the label manipulation on the issue (check if the whole pipeline works well).
