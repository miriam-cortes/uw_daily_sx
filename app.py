import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

import schedule
import time

GOOGLE_FORM_LINK = 'google_form_link'
DEFAULT_MESSAGE = f"Please fill our your symptom attestation if you plan on working out today {GOOGLE_FORM_LINK}"


def send_message(msg=DEFAULT_MESSAGE):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg,
    }
    try:
        request = Request(url, urlencode(data).encode())
        import pdb; pdb.set_trace()
        json = urlopen(request).read().decode()
    except Exception as e:
        print(e)


schedule.every().minute.do(send_message)

while True:
    print('running pending')
    schedule.run_pending()
    time.sleep(50)

