import re
from datetime import date
# from alpaca_trade_api.rest import REST, TimeFrame


def find_crypto_value(crypto_json):
    bulk_str = str(crypto_json['data'].values())
    coin_price_match = re.search(r"(price': )(\d+.\d\d)",bulk_str)
    coin_price = float(coin_price_match.group(2))
    return coin_price


def calc_start_date(years_ago):
    to_day=str(date.today())
    match = re.match(r'(\d\d\d\d)-(\d\d)-(\d\d)', to_day)
    _yrsago= int(match.group(1))-years_ago
    _yrsago = str(_yrsago)+'-'+match.group(2)+'-'+match.group(3)
    return _yrsago

# def get_company(ticker, start, end, tradeapi):
#     return tradeapi.get_bars(
#         ticker,
#         TimeFrame.Day,
#         start,
#         end
#     ).df
