import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GOOGLE_FORM_LINK = ''
DEFAULT_MESSAGE = f"Please fill out your symptom attestation if you plan on working out today {GOOGLE_FORM_LINK}"



def send_message(groupme_bots, msg=DEFAULT_MESSAGE):
    for id in groupme_bots:
        url = 'https://api.groupme.com/v3/bots/post'
        data = {
            'bot_id': os.environ.get(id),
            'text': msg,
        }
        try:
            print(f"sending to bot {id}")
            request = Request(url, urlencode(data).encode())
            json = urlopen(request).read().decode()
        except Exception as e:
            print(e)
            continue
        print(f"success sending to bot {id}")


send_message()
