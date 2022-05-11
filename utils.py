import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import vonage
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
load_dotenv()

MY_TOKEN = os.getenv("MY_TOKEN")
SMS_TO = os.getenv("TO_SMS")
API_KEY = os.getenv('COIN_API_KEY')


def send_telegram(message):
    requests.post(
        'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown'.format(MY_TOKEN, 786259592, message))


def get_ust_price():
    price = cg.get_price(ids='terrausd', vs_currencies='usd')
    return (price['terrausd']['usd'])