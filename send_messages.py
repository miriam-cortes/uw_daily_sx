import json
import os
import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_message(groupme_bot, form_link, msg):
#     url = os.environ.get(groupme_bot)
#     data = {
#                     'bot_id': os.environ.get(groupme_bot),
#                     'text': "{} {}".format(msg, form_link)
#                 }

    print("sending to bot {}".format(groupme_bot))
    tries = 10
    for i in range(tries):
        try:
#             request = Request(url, urlencode(data).encode())
#             json = urlopen(request).read().decode()
            response = requests.post(
                url='https://api.groupme.com/v3/bots/post',
                data={
                    'bot_id': os.environ.get(groupme_bot),
                    'text': "{} {}".format(msg, form_link)
                })
            import pdb; pdb.set_trace()
            if response.status_code == 200:
                print("success sending to bot {} on the {} try".format(groupme_bot, i))
                break
            else:
                print("failed: {}".format(response.text))
        except Exception as e:
            print("failed for bot {} on try number {} - error: {}".format(groupme_bot, i, e))

