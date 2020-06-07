import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

import schedule
import time


def send_message(msg='test'):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


schedule.every().minute.do(send_message)

while True:
    print('running pending')
    schedule.run_pending()
    time.sleep(60)

