from urllib.parse import urlencode
from urllib.request import Request, urlopen
from constants import DEFAULT_MESSAGE


def send_message(groupme_bot, form_link, msg=DEFAULT_MESSAGE):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': groupme_bot,
        'text': "{} {}".format(msg, form_link),
    }
    try:
        print("sending to bot {}".format(groupme_bot))
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
        print(json)
    except Exception as e:
        print(e)
    print("success sending to bot {}".format(groupme_bot))
