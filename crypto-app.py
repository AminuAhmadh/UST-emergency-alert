# import the required libraries
from datetime import datetime
from time import time
import vonage
import os
import time
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv
import requests
import json

cg = CoinGeckoAPI()
load_dotenv()

KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
MY_TOKEN = os.getenv("MY_TOKEN")
SMS_TO = os.getenv("TO_SMS")
API_KEY = os.getenv('COIN_API_KEY')

# setting up client for VONAGE TEXT messages
client = vonage.Client(key=KEY, secret=SECRET)
sms = vonage.Sms(client)

current_time = datetime.now()

def send_telegram(message):
    requests.post(
        'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown'.format(MY_TOKEN, 786259592, message))


def get_ust_price():
    price = cg.get_price(ids='terrausd', vs_currencies='usd')
    return (price['terrausd']['usd'])

while True:
    print('Getting Price...')
    price = get_ust_price ()
    print ('Price Obtained.')

    if price > 0.90:
        send_telegram(f'Terra USD (UST) Price now at {price}. SELL IMMEDIATELY !!!')
        responseData = sms.send_message({
        "from": "EMERGENCY ALERT",
        "to": SMS_TO,
        "text": "Sell UST NOW!",})
        if responseData["messages"][0]["status"] == "0":
            print("SMS sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

        print('EMERGENCY sell alert sent')

        quit()

    else:
        send_telegram(f'Terra USD (UST) price now at {price}. Price below sell target. HODL!')
        print('EMERGENCY HODL sent.')
    
    print('Done for the Hour', str(current_time.hour))

    time.sleep(5400)
