# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename: str) -> list:
    """
    Read portfolio from a csv file of name, shares, price data
    """
    result = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            x = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
            result.append(x)
        return result


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name,price data
    """
    result = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                result[row[0]] = float(row[1])
            except IndexError:
                pass
        return result


def make_report(portfolio: list, prices: dict) -> list:
    result = []
    for i in portfolio:
        x = (i['name'], i['shares'], prices[i['name']], prices[i['name']] - i['price'])
        result.append(x)
    return result


def print_report(report: list) -> None:
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


def portfolio_report(portfolio: str, prices: str) -> None:
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')