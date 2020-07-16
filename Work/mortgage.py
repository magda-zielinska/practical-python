# mortgage.py
#
# Exercise 1.7

mortgage = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
paid = 0.00
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while mortgage > 0:

    mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
    paid = paid + monthly_payment
    months = months + 1

    if extra_payment_start_month <= months <= extra_payment_end_month:
        mortgage = mortgage - 1000.00
        paid = paid + 1000.00

    # fixing the overpayment that occurs in the last month:
    if mortgage < monthly_payment:
        paid += mortgage
        mortgage = mortgage - mortgage

    print(months, round(paid, 2), round(mortgage, 2))

print(round(paid, 2), months)

