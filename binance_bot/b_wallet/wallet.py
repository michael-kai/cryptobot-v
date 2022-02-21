"""
Local wallet for testing algorithm
"""


import json
import os

dirname = os.path.dirname(__file__)
balance_path = os.path.join(dirname, 'balance.json')
profit_path = os.path.join(dirname, 'profit.json')
closed_orders_path = os.path.join(dirname, 'closed_orders.json')


def get_closed_orders():
    with open(closed_orders_path, 'r') as reader:
        closed_orders = json.loads(reader.read())
    return closed_orders['closed_orders']


def add_closed_orders(order):
    with open(closed_orders_path, 'r') as reader:
        closed_orders = json.loads(reader.read())
        closed_orders['closed_orders'].append(order)

    with open(closed_orders_path, 'w+') as writer:
        json.dump(closed_orders, writer)


def get_balance():
    with open(balance_path, 'r') as reader:
        current_balance = json.loads(reader.read())
    return float(current_balance['balance'])


def add_balance(closed_order_money):
    with open(balance_path, 'r') as reader:
        current_balance = json.loads(reader.read())
        current_balance['balance'] += closed_order_money

    with open(balance_path, 'w+') as writer:
        json.dump(current_balance, writer)


def substract_balance(opened_order_money):
    with open(balance_path, 'r') as reader:
        current_balance = json.loads(reader.read())
        current_balance['balance'] -= opened_order_money

    with open(balance_path, 'w+') as writer:
        json.dump(current_balance, writer)


def get_profit():
    with open(profit_path, 'r') as reader:
        current_balance = json.loads(reader.read())
    return current_balance['profit']


def add_profit():
    fee = 0.015
    with open(profit_path, 'r') as reader:
        current_balance = json.loads(reader.read())
    current_balance['profit'] += fee
    with open(profit_path, 'w+') as writer:
        json.dump(current_balance, writer)
