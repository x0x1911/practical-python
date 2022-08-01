# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename):
    result = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            x = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
            result.append(x)
        return result


def read_prices(filename):
    result = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                result[row[0]] = float(row[1])
            except IndexError:
                pass
        return result


def make_report(portfolio, prices):
    result = []
    for i in portfolio:
        x = (i['name'], i['shares'], prices[i['name']], prices[i['name']] - i['price'])
        result.append(x)
    return result


headers = ('Name', 'Shares', 'Price', 'Change')
prices = read_prices('Work/Data/prices.csv')  # dict company:price
portfolio = read_portfolio('Work/Data/portfoliodate.csv')  # list company:stock
report = make_report(portfolio, prices)
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}  {headers[3]:>10s}')
print(f'---------- ---------- ---------- -----------')
for name, shares, price, change in report:
    price = '$'+str(price)
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

total_cost = 0.0
for s in portfolio:
    total_cost += (s['price']*s['shares'])

total_value = 0.0
for s in portfolio:
    total_value += (s['shares']*prices[s['name']])

print('Total cost', total_cost)
print('Current cost:', total_value)
print('Total gain:', (total_value-total_cost))
