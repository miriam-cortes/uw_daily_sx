import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from constants import QUARANTINE_MESSAGE

GOOGLE_FORM_LINK = os.environ.get('FB_Q_DAILY')
football_message = f"{QUARANTINE_MESSAGE} {GOOGLE_FORM_LINK}"


def send_football_message(message=football_message):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get('FOOTBALL_q'),
        'text': message,
    }
    try:
        print(f"sending to bot {id}")
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
    except Exception as e:
        print(e)
    print(f"success sending to bot {id}")


send_football_message()

