from collections import Counter
from _collections import defaultdict
from _collections import deque

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

total_shares = Counter()

for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares['IBM'])
print(total_shares['GOOG'])
print(total_shares['AA'])
print(total_shares)
print('Mostly held shares: ', total_shares.most_common(3))


holdings = defaultdict(list)

for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print(holdings['IBM'])
print(holdings)

# to keep record of the last 3 elements added to the portfolio:
history = deque(maxlen=3)
for holding in portfolio:
    history.append(holding)

print(history)



