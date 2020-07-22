# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    :param filename: filepath
    :return: a list of dictionaries
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    """
    Read a csv file with stock prices into a dictionary where the key is the name of the stock
    and the value is its price
    :param filename: path to file
    :return: a dictionary
    """
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # row = row.split(',')
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Compute the total value of the stock from the portfolio file
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*s['price']

print('Total cost', total_value)

# Compute the current value of the portfolio based on the new prices
total_new_value = 0.0
for s in portfolio:
    total_new_value += s['shares']*prices[s['name']]

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
        shares = s['shares']
        price = prices[s['name']]
        change = price - s['price']
        holding = (name, shares, price, change)
        data.append(holding)
    return data

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print((10 * '-' + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# or: for row in report:
#     print('%10s %10d %10.2f %10.2f' % row)


