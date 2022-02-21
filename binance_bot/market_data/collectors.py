import json
import datetime
import requests
from utils import bot_utils


def get_24hr_stats(symbol='ETHUSDT'):
    resp = requests.get(f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}')
    result = {}
    for field, value in resp.json().items():
        result[field] = value if "Time" not in field\
            else str(bot_utils.convert_time_from_unix(value))
    return result


def get_custom_candlestick_data(currency_pair='ETHUSDT', interval='1h',
                                limit=None, start_time=None, end_time=None):
    params_custom = {
        'symbol': currency_pair,
        'interval': interval,
        'limit': limit,
        'startTime': bot_utils.convert_time_to_unix(start_time),
        'endTime': bot_utils.convert_time_to_unix(end_time),
    }

    resp = requests.get(f'https://api.binance.com/api/v3/klines', params=params_custom)

    data = json.loads(resp.text)
    result = []
    for row in data:
        candle_data = {
            'Original open time': row[0],
            'Original close time': row[6],
            'Open time': str(bot_utils.convert_time_from_unix(row[0])),
            'Close time': str(bot_utils.convert_time_from_unix(row[6])),
            'Open': row[1],
            'High': row[2],
            'Low': row[3],
            'Close': row[4],
            'Volume': row[5],
            'Quote asset volume': row[7],
            'Number of trades': row[8],
            'Taker buy base asset volume': row[9],
            'Taker buy quote asset volume': row[10],
        }
        result.append(candle_data)
    return result


# result = get_custom_candlestick_data(currency_pair=CURRENCY_PAIR,
#                                      interval=INTERVALS['1d'],
#                                      limit=1,
#                                      start_time=(2021, 1, 1, 1, 1, 1),
#                                      end_time=(2021, 1, 2, 1, 1, 1),
#                                      )

def check_server():
    resp = requests.get('https://api.binance.com/api/v3/time')
    return {
        'status_code': resp.status_code,
        'current_time': bot_utils.convert_time_from_unix(resp.json()['serverTime']),
    }


def get_order_book(symbol='ETHUSDT', limit=1):
    """available limits: 1-100, 500, 1000, 5000"""
    params = {
        'symbol': symbol,
        'limit': limit,
    }
    resp = requests.get('https://api.binance.com/api/v3/depth', params=params)
    return resp.json()


def get_max_price(currency_pair='ETHUSDT', interval='1w', limit=50,):
    start = datetime.datetime.now() - datetime.timedelta(weeks=24)
    end = datetime.datetime.now()

    params_custom = {
        'symbol': currency_pair,
        'interval': interval,
        'limit': limit,
        'startTime': bot_utils.convert_time_to_unix(start.year, start.month, start.day, 0, 0, 0),
        'endTime': bot_utils.convert_time_to_unix(end.year, end.month, end.day, 0, 0, 0),

    }
    resp = requests.get(f'https://api.binance.com/api/v3/klines', params=params_custom)
    data = json.loads(resp.text)
    result = max([row[1] for row in data])
    result = float(result) - ((float(result) / 100) * 5)
    return result


def get_hourly_candlestick_data(currency_pair='ETHUSDT', interval='1h', limit=2,):
    last_hour_date = datetime.datetime.now() - datetime.timedelta(hours=12)
    last_hour = last_hour_date + datetime.timedelta(hours=1)
    params_custom = {
        'symbol': currency_pair,
        'interval': interval,
        'limit': limit,
        'startTime': bot_utils.convert_time_to_unix(last_hour_date.year,
                                                    last_hour_date.month,
                                                    last_hour_date.day,
                                                    last_hour_date.hour, 0, 0),
        'endTime': bot_utils.convert_time_to_unix(last_hour_date.year,
                                                  last_hour_date.month,
                                                  last_hour_date.day if last_hour.hour != 0 else last_hour_date.day + 1,
                                                  last_hour.hour, 59, 59),

    }
    resp = requests.get(f'https://api.binance.com/api/v3/klines', params=params_custom)

    data = json.loads(resp.text)
    result = []
    for row in data:
        candle_data = {
            'Original open time': row[0],
            'Original close time': row[6],
            'Open time': str(bot_utils.convert_time_from_unix(row[0])),
            'Close time': str(bot_utils.convert_time_from_unix(row[6])),
            'Open': row[1],
            'High': row[2],
            'Low': row[3],
            'Close': row[4],
            'Volume': row[5],
            'Quote asset volume': row[7],
            'Number of trades': row[8],
            'Taker buy base asset volume': row[9],
            'Taker buy quote asset volume': row[10],
        }
        result.append(candle_data)
    return result[0], result[1]
