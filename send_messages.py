import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from constants import DEFAULT_MESSAGE


def send_message(groupme_bot, form_link, msg=DEFAULT_MESSAGE):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get(groupme_bot),
        'text': f"{msg} {form_link}",
    }
    try:
        print(f"sending to bot {groupme_bot}")
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
    except Exception as e:
        print(e)
    print(f"success sending to bot {groupme_bot}")
