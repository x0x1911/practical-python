# report.py
#
# Exercise 2.4
from typing import Any

from . import fileparse
import sys
from . import tableformat
from .portfolio import Portfolio



def read_portfolio(filename: str, **opts) -> object:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)


def read_prices(filename: str) -> dict[Any, Any]:
    """
    Read prices from a CSV file of name,price data
    """
    with open(filename) as f:
        return dict(fileparse.parse_csv(f, types=[str, float], has_headers=False))


def make_report(portfolio: list, prices: dict) -> list:
    result = []
    for i in portfolio:
        x = (i.name, i.shares, i.price, prices[i.name] - i.price)
        result.append(x)

    return result


def print_report(report: list, formatter) -> None:
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio: str, prices: str, fmt='txt') -> None:
    # Read Data
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    # Create report
    report = make_report(portfolio, prices)
    # print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(arglist):
    if len(arglist) < 3:
        raise SystemExit(f'Usage: {sys.argv[0][-9::]} ' 'portfile pricefile format')
    if len(arglist) > 3:
        portfolio_report(arglist[1], arglist[2], arglist[3])
    elif len(arglist) > 2:
        portfolio_report(arglist[1], arglist[2])


if __name__ == '__main__':
    import logging

    logging.basicConfig(
        filename='../../app.log',  # Name of the log file (omit to use stderr)
        filemode='a',  # File mode (use 'a' to append)
        level=logging.WARNING,  # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )
    main(sys.argv)
    # main(['report.py', '../portfolio.csv', '../prices.csv'])
