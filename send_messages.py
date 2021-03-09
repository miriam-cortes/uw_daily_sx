import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_message(groupme_bot, form_link, msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': os.environ.get(groupme_bot),
        'text': "{} {}".format(msg, form_link),
    }
    tries = 4
    for i in range(tries):
        try:
            print("sending to bot {}".format(groupme_bot))
            request = Request(url, urlencode(data).encode())
            json = urlopen(request).read().decode()
            print("success sending to bot {}".format(groupme_bot))
            print("response: {}".format(json))
            break
        except Exception as e:
            print("failed sending to bot {}".format(groupme_bot))
            print(e)

