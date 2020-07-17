# pcost.py
#
# Exercise 1.27

total_cost = 0.00
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        line = line.split(',')
        total_cost += int(line[1]) * float(line[2])
        #print(line)

print(f'Total cost {total_cost}')