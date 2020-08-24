# pcost.py
#
# Exercise 1.27
import csv
import sys
from Work import report

def portfolio_cost():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

        rows = report.read_portfolio(filename)
        total_cost = 0.00
        for line in rows:
            try:
                total_cost += int(line['shares']) * float(line['price'])
            except ValueError:
                pass
        return total_cost

def missing_portfolio():

    with open('Data/portfoliodate.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        next(rows)
        missing_cost = 0.00
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                missing_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
    return missing_cost


cost = portfolio_cost()
print(f'Total cost: ', cost)

missing = missing_portfolio()
print('Total cost in the missing file: ', missing)
