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