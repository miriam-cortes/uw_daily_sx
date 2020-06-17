import os
from datetime import date
from send_messages import send_message
from constants import DEFAULT_MESSAGE

# Messages to be sent only on specific days should be in an if-statement like below:
# Messages to be sent only on Thursdays
# if date.today().weekday() == 3:
#     send_message(
#         'FOOTBALL_q', 'FB_Q_DAILY', QUARANTINE_MESSAGE
#     )

# Days:
# 0- Monday
# 1- Tuesday
# 2- Wednesday
# 3- Thursday
# 4- Friday
# 5- Saturday
# 6- Sunday


# DAILY ATC MESSAGE
send_message(
    os.environ.get('ATC_BOT'), # ATC bot from heroku configs
    os.environ.get('WORKDAY_LINK'), # workday link from heroku configs
    DEFAULT_MESSAGE # message
)
