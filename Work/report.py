# report.py
#
# Exercise 2.4

import csv
import fileparse


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    :param filename: filepath
    :return: a list of dictionaries
    """
    # using dictionary comprehensions:
    # f = open('Data/portfoliodate.csv')
    # rows = csv.reader(f)
    # headers = next(rows)
    select = ['name', 'shares', 'price']
    types = [str, int, float]
    portfolio = fileparse.parse_csv(filename, select=select, types=types)
    # indices = [headers.index(colname) for colname in selected]
    # portfolio = [ {colname: type(row[index]) for colname, type, index in zip(selected, types, indices)} for row in rows]


    # portfolio = []
    #
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         # holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
    #         holding = dict(zip(headers, row))
    #         portfolio.append(holding)
    return portfolio


def read_prices(filename):
    """
    Read a csv file with stock prices into a dictionary where the key is the name of the stock
    and the value is its price
    :param filename: path to file
    :return: a dictionary
    """
    prices = dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))

    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         # row = row.split(',')
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError:
    #             pass
    return prices


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

# Compute the total value of the stock from the portfolio file
total_value = 0.0
for s in portfolio:
    total_value += int(s['shares']) * float(s['price'])

print('Total cost', total_value)

# Compute the current value of the portfolio based on the new prices
total_new_value = 0.0
for s in portfolio:
    total_new_value += int(s['shares']) * float(prices[s['name']])

print('Current value', total_new_value)
print('Gain', total_new_value - total_value)


def make_report(portfolio, prices):
    """
    Compute the new change in the price of the stock
    :param portfolio: list of dictionaries
    :param prices: dictionary
    :return: a list of tuples
    """
    data = []
    for s in portfolio:
        name = s['name']
        shares = int(s['shares'])
        price = float(prices[s['name']])
        change = price - float(s['price'])
        holding = (name, shares, price, change)
        data.append(holding)
    return data

def print_report(data):
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print((10 * '-' + ' ') * len(headers))
    for name, shares, price, change in data:
        print(f'{name:>10s} {shares:>10d} {price:>9.2f} {change:>10.2f}')


def cli_report(fileportfolio, fileprices):
    portfolio = read_portfolio(fileportfolio)
    prices = read_prices(fileprices)
    report = make_report(portfolio, prices)
    print_report(report)


#for row in report:
#     print('%10s %10d' '$''%10.2f %10.2f' % row)

def main(args):
    fileportfolio = str(read_portfolio(args[1]))
    fileprices = str(read_prices(args[2]))
    cli_report(fileportfolio, fileprices)


if __name__ == '__main':
    import sys
    main(sys.argv)

