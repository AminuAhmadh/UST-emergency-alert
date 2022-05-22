# import the required libraries
from datetime import datetime
from time import time
import vonage
import time
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

# get creds and env variables
KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
MY_TOKEN = os.getenv("MY_TOKEN")
SMS_TO = os.getenv("TO_SMS")
API_KEY = os.getenv('COIN_API_KEY')

# setting up client for VONAGE TEXT messages
client = vonage.Client(key=KEY, secret=SECRET)
sms = vonage.Sms(client)

current_time = datetime.now()
# func to send telegram message
def send_telegram(message):
    requests.get(
        'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown'.format(MY_TOKEN, 786259592, message))

# url to scrape price of UST
url = 'https://www.coinmarketcap.com/currencies/terrausd'

while True:
    print('Getting Price...')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_value = soup.find('div', {'class': 'priceValue'})
    price = float(price_value.text.strip('$'))
    print ('Price Obtained.')

    if price > 0.90:
        sell = True
        if sell:
            send_telegram(f'Terra USD (UST) Price now at ${price}. SELL IMMEDIATELY !!!')
            responseData = sms.send_message({
            "from": "EMERGENCY ALERT",
            "to": SMS_TO,
            "text": "Sell UST NOW!",})
            if responseData["messages"][0]["status"] == "0":
                print("SMS sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

            print('EMERGENCY sell alert sent')

    elif price < 0.90:
        hodl = True
        if hodl:
            send_telegram(f'Terra USD (UST) price now at ${price}. Price below sell target. HODL!')
            print('EMERGENCY HODL sent.')
        
        print('Done for the Hour', str(current_time.hour))
        # wait 1 HOUR
        time.sleep(5200)
