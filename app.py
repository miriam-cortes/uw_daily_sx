import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)



# @app.route('/', methods=['POST'])
# def webhook():
#     data = request.get_json()
#
#     # We don't want to reply to ourselves!
#     if data['name'] != 'apnorton-test-bot':
#         msg = '{}, you sent "{}".'.format(data['name'], data['text'])
#         send_message(msg)
#     return "ok", 200

import schedule
import time


def job():
    send_message('testing a schedule...you should receive this again in 1 minute')


while True:
    schedule.every(1).minutes.do(job)


def send_message(msg='test'):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_TEST_BOT_ID'),
        'text': msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

