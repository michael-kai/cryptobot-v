import sys
import datetime
import time as sleeper
from listeners.hourly_listener import hourly_listener
from binance_bot.telegram_notifier.tg_notifier import send_message


def start_bot():
    for hour in range(sys.maxsize):
        delay = 3600.0
        now = datetime.datetime.now()
        time, opened_orders, closed_orders, balance, profit, alert = hourly_listener()
        msg = f"***<b>Actual binance data</b>***\n<b>"\
              f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}</b>\n"\
              f"Opened orders: {opened_orders}\n"\
              f"Closed orders: {closed_orders}\n"\
              f"Balance: {balance}\n"\
              f"Profit: {profit}\n"\
              f"Alerts: {alert}\n"
        send_message(msg)
        request_delay = datetime.datetime.now() - now
        delay -= float(request_delay.seconds) + float('0.' + str(request_delay.microseconds))
        sleeper.sleep(delay)


