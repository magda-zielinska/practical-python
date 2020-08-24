# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and has_headers is False:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows):
            if not row:
                continue

            if select:
                row = [row[index] for index in indices]

            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors:
                    pass
                else:
                    print(f'Row {rowno}: Couldn\'t convert: ', row)
                    print(f'Row {rowno}: Reason: ', e)

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

        return records

