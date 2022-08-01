# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month += 1
    total_paid = total_paid + payment
    principal = principal * (1 + rate / 12) - payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment


    print(f'Month : {month:3.0f} Total paid : {total_paid:9.2f} Principal remainder : {principal:0.2f}')

print('Total paid', round(total_paid, 2))
print('Monhts', month)
