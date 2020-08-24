import csv

prices = {}

def read_prices():
    with open('Data/prices.csv', 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


print(read_prices())

