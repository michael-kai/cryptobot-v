**Goal** - create a small project with minimal budget and real business-task
Attention! This project is not a money-making guide

**Description** - each hour bot makes an HTTP request to Binance API and uses simple logic to decide when to buy and sell ETH cryptocurrency. After making a request, the bot sends a notification to the Telegram channel with statistics and alerts.
The bot can be deployed to Heroku.
At this point, the bot emulates buying and selling. This way, I'm testing the buy/sell strategy.
When ETH price rises to the needed level, I will add real buy/sell functions.


**Usage**  
Create venv, install requirements.txt inside venv. In the root directory create .env file with the next values:
api_key=YOUR_API_KEY(telegram API token)
chat_id=YOUR_CHAT_ID(telegram chat id)

Guide for Telegram bots creation - https://core.telegram.org/bots  
Then, just run start_worker.py, and the bot will start working.


**Deploy**  
Cryptobot is completely ready for deployment on Heroku. All you need beyond classic instruction is to set up 3 Config Vars in Heroku app:
1) api_key=YOUR_API_KEY(telegram API token)
2) chat_id=YOUR_CHAT_ID(telegram chat id)
3) TZ=YOUR_TIME_ZONE
