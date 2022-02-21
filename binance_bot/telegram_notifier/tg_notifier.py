import requests
from decouple import config


def send_message(message):
    resp = requests.get(
        f'https://api.telegram.org/bot{config("api_key")}/sendMessage?chat_id={config("chat_id")}&text={message}&parse_mode=html')


if __name__ == '__main__':
    send_message('Hello')