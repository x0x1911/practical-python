# pcost.py
#
# Exercise 1.27
import report
import sys


def portfoliocost(filename):
    result = 0
    portfolio = report.read_portfolio(filename)
    for n, i in enumerate(portfolio, start=1):
        try:
            a = int(i.shares)
            b = float(i.price)
            result += a * b
        except ValueError:
            print(f'Row {n}: Couldn\'t convert: {i}')
    return result



def main(arglist):
    if len(arglist) != 2:
        raise SystemExit(f'Usage: {sys.argv[0][-8::]} ' 'portfile')
    print(f'Total cost: {portfoliocost(arglist[1])}')


if __name__ == '__main__':
    #main(sys.argv)
    main(['pcost.py', 'Data/portfolio.csv'])