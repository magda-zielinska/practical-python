# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0.00
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            line = line.split(',')
            total_cost += int(line[1]) * float(line[2])
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: ', cost)