import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GOOGLE_FORM_LINK = 'https://forms.gle/s3Sn7PHuT8NNtPv86'
DEFAULT_MESSAGE = f"Please fill out your symptom attestation if you plan on working out today {GOOGLE_FORM_LINK}"
GROUPME_BOT_IDS = [
    'GROUPME_TEST_BOT_ID',
]


def send_message(msg=DEFAULT_MESSAGE):
    for id in GROUPME_BOT_IDS:
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
