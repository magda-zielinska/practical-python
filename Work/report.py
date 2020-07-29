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
    # using dictionary comprehensions:
    # f = open('Data/portfoliodate.csv')
    # rows = csv.reader(f)
    # headers = next(rows)
    # selected = ['name', 'shares', 'price']
    # indices = [headers.index(colname) for colname in selected]
    # portfolio = [ {colname: row[index] for colname, index in zip(selected, indices)} for row in rows]


    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            holding = dict(zip(headers, row))
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

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print((10 * '-' + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>9.2f} {change:>10.2f}')

#for row in report:
#     print('%10s %10d' '$''%10.2f %10.2f' % row)


