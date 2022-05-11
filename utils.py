import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import yagmail
from pretty_html_table import build_table
import vonage
from requests.sessions import Session
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
load_dotenv()

MY_TOKEN = os.getenv("MY_TOKEN")
RECIPENT_EMAIL = os.getenv("RECIPENT_EMAIL")
MAIL_FROM_PASS = os.getenv("MESSAGE_FROM_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")
SMS_TO = os.getenv("TO_SMS")
API_KEY = os.getenv('COIN_API_KEY')


def send_telegram(message):
    requests.post(
        'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown'.format(MY_TOKEN, 786259592, message))

# function to send emails
def send_emails(contents):
    global RECIPENT_EMAIL
    recipent_email_address = RECIPENT_EMAIL
    global MAIL_FROM_PASS
    password1 = MAIL_FROM_PASS
    msg_from = EMAIL_FROM
    yag = yagmail.SMTP(msg_from, password1)
    content = ["<h1> TODAY'S TREND... </h1>", contents + '<h1> End Of Message </h1>']
    yag.send(to=recipent_email_address, subject= '[Automated Email] Apes Trend: ' + 
    str(datetime.now().date()), contents=content)


def get_ust_price():
    price = cg.get_price(ids='terrausd', vs_currencies='usd')
    return (price['terrausd']['usd'])

get_ust_price()