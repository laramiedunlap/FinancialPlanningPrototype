import re
from datetime import date
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame


def find_crypto_value(num_coins, crypto_json, round_to):
    bulk_str = str(crypto_json['data'].values())
    coin_price_match = re.search(r"(price': )(\d+.\d\d)",bulk_str)
    coin_price = float(coin_price_match.group(2))
    crypto_value = round(coin_price*num_coins,int(round_to))
    return crypto_value


def calc_start_date(years_ago):
    to_day=str(date.today())
    match = re.match(r'(\d\d\d\d)-(\d\d)-(\d\d)', to_day)
    _yrsago= int(match.group(1))-years_ago
    _yrsago = str(_yrsago)+'-'+match.group(2)+'-'+match.group(3)
    return _yrsago

def get_company(ticker, start, end, tradeapi):
    return tradeapi.get_bars(
        ticker,
        TimeFrame.Day,
        start,
        end
    ).df
