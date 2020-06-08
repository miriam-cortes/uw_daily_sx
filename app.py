import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

GOOGLE_FORM_LINK = 'google_form_link'
DEFAULT_MESSAGE = f"Please fill out your symptom attestation if you plan on working out today {GOOGLE_FORM_LINK}"


def send_message(msg=DEFAULT_MESSAGE):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get('GROUPME_TEST_BOT_ID'),
        'text': msg,
    }
    try:
        print(f"sending to {url} with data {data}")
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
    except Exception as e:
        print(e)


send_message()

