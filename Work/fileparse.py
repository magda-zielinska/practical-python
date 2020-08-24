# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=","):
    '''
    Parse a CSV file into a list of records
    '''
    if select is not None and has_headers is False:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:
                continue

            if select:
                row = [row[index] for index in indices]

            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                print('Couldn\'t convert: ', row)
                print('Reason: ', e)

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

        return records

