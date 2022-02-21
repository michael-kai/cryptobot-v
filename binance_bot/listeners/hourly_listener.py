"""
Hourly listener created in purpose to test getting hourly data from binance
and send it to telegram chat via telegram bot
"""
from datetime import datetime
from market_data.collectors import get_hourly_candlestick_data, get_max_price
from b_wallet.wallet import (get_balance, substract_balance,
                             add_balance, add_profit, get_profit,
                             get_closed_orders, add_closed_orders,
                             )

ALERTS = {
    '0': 'No alerts',
    '1': '<ins>Balance less than $5</ins>',
    '2': '<ins>Max opened orders</ins>',
    '3': 'Price is too close to TOP price'
}
OPENED_ORDERS = []
CLOSED_ORDERS = []
MAX_ORDERS = 3
PLUS_PERCENT = 0.3
BID = 5


def check_opened_order(data):
    for order in OPENED_ORDERS:
        if order['sell_price'] <= float(data['Close']):
            order['sell_data'] = data
            add_closed_orders(order)
            OPENED_ORDERS.pop(OPENED_ORDERS.index(order))
            add_balance(BID)
            add_profit()


def make_order(buy_data=None):
    order = {
        'buy_price': float(buy_data['Open']),
        'sell_price': ((float(buy_data['Open'])//100 * PLUS_PERCENT) + float(buy_data['Open'])),
        'buy_data' : buy_data,
            }
    return order


def get_growth_percentage(data):
    if data['Close'] > data['Open']:
        percentage = float('%.2f' % (100 - ((float(data['Open']) / float(data['Close'])) * 100)))
        if percentage > 2.0:
            return False
        else:
            return True


def hourly_listener():
    balance = get_balance()
    now = datetime.now()
    last_hour_data, actual_hour_data = get_hourly_candlestick_data()

    if OPENED_ORDERS:
        check_opened_order(actual_hour_data)

    if balance < 5.1:
        return now, len(OPENED_ORDERS), len(get_closed_orders()), balance, get_profit(), ALERTS['1']
    if len(OPENED_ORDERS) >= MAX_ORDERS:
        return now, len(OPENED_ORDERS), len(get_closed_orders()), balance, get_profit(), ALERTS['2']

    normal_growth = get_growth_percentage(last_hour_data)
    if float(actual_hour_data['Open']) >= get_max_price():
        return now, len(OPENED_ORDERS), len(get_closed_orders()), balance, get_profit(), ALERTS['3']

    if normal_growth:
        order = make_order(buy_data=actual_hour_data)
        OPENED_ORDERS.append(order)
        substract_balance(BID)
        balance = get_balance()
        return now, len(OPENED_ORDERS), len(get_closed_orders()), balance, get_profit(), ALERTS['0']
    else:
        return now, len(OPENED_ORDERS), len(get_closed_orders()), balance, get_profit(), ALERTS['0']
