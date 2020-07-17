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
    f = open(filename, 'rt')
    rows = csv.reader(f)
    next(rows)
    total_cost = 0.00
    for line in rows:
        try:
            total_cost += int(line[1]) * float(line[2])
        except ValueError:
            pass
    return total_cost


cost = portfolio_cost()
print(f'Total cost: ', cost)
