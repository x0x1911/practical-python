# report.py
#
# Exercise 2.4
import fileparse
import sys
import stock
import tableformat

def read_portfolio(filename: str) -> list:
    """
    Read portfolio from a csv file of name, shares, price data
    """
    with open(filename) as f:
        portdicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio


def read_prices(filename: str) -> dict:
    """
    Read prices from a CSV file of name,price data
    """
    with open(filename) as f:
        result = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    assert isinstance(result, list)
    return dict(result)


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
    main(sys.argv)
    #main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
