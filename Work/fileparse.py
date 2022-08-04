# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records

    file: any file-like/iterable object.
    select: a list of strings ['column name1, column name2, ...]
        optionally allows user-specified columns to be picked.
    types: optionally allows type-conversions to be applied to the returned data
        types=[str, int, float].
    has_headers: optionally allows to parse csv files without header has_headers=False.
    delimiter: allows to specify delimiter default is: delimiter=','.
    """

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    rows = csv.reader(file, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    records = []
    for rownumber, row in enumerate(rows, start=1):
        if not row:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if silence_errors:
                    continue
                else:
                    print(f'Row {rownumber}:  Couldn\'t convert {row}')
                    print(f'Row {rownumber}: Reason {e}')
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records
