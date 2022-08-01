# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfoliocost(filename):
    result = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for n, i in enumerate(rows, start=1):
            record = dict(zip(headers, i))
            try:
                a = int(record['shares'])
                b = float(record['price'])
                result += a * b
            except ValueError:
                print(f'Row {n}: Couldn\'t convert: {i}')
    return result


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfoliocost(filename)
print('Total cost:', cost)
