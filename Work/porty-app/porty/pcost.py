# pcost.py
#
# Exercise 1.27
from . import report
import sys


def portfoliocost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(arglist):
    if len(arglist) != 2:
        raise SystemExit(f'Usage: {sys.argv[0][-8::]} ' 'portfile')
    print(f'Total cost: {portfoliocost(arglist[1])}')


if __name__ == '__main__':
    # main(sys.argv)
    main(['pcost.py', 'Data/portfolioblank.csv'])
