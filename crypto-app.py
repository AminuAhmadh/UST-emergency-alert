# import the required libraries
from datetime import datetime
from time import time
import vonage
import os
import time
from utils import send_emails, send_telegram, get_ust_price

KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
API_KEY = os.getenv('COIN_API_KEY')
SMS_TO = os.getenv("TO_SMS")

# setting up client for VONAGE TEXT messages
client = vonage.Client(key=KEY, secret=SECRET)
sms = vonage.Sms(client)

current_time = datetime.now()

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
