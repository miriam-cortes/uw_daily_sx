import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GOOGLE_FORM_LINK = 'https://forms.gle/s3Sn7PHuT8NNtPv86'
DEFAULT_MESSAGE = f"Please fill out your symptom attestation if you plan on working out today {GOOGLE_FORM_LINK}"
GROUPME_BOT_IDS = [
    os.environ.get('GROUPME_TEST_BOT_ID'),
]


def send_message(msg=DEFAULT_MESSAGE):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': GROUPME_BOT_IDS,
        'text': msg,
    }
    try:
        print(f"sending to {url} with data {data}")
        import pdb; pdb.set_trace()
        # request = Request(url, urlencode(data).encode())
        # json = urlopen(request).read().decode()
    except Exception as e:
        print(e)
    print("success")


send_message()
