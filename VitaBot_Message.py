import os
from datetime import date
from send_messages import send_message
from constants import VITABOT_MESSAGE

# DAILY REMINDER FOR GYMNASTICS TO TAKE THEIR VITAMINS
send_message(
    'GYM_VITABOT', # vitabot from heroku configs
    '',
    VITABOT_MESSAGE # message
)
