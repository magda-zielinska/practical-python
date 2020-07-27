# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        total_cost = 0.00
        for line in rows:
            try:
                total_cost += int(line[1]) * float(line[2])
            except ValueError:
                pass
        return total_cost

def missing_portfolio():

    with open('Data/missing.csv') as f:
        rows = csv.reader(f)
        next(rows)
        missing_cost = 0.00
        for rowno, row in enumerate(rows):
            try:
                missing_cost += int(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
    return missing_cost


cost = portfolio_cost()
print(f'Total cost: ', cost)

missing = missing_portfolio()
print('Total cost in the missing file: ', missing)
