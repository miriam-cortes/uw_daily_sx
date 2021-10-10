import os
from datetime import date
from send_messages import send_message
from constants import INTERN_LOG_MESSAGE

# DAILY REMINDER FOR ATCS TO LOG STUDENT INTERN HOURS
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

if date.today().weekday() == 6:
    send_message(
        'STUDENT_INTERN_LOG_BOT', # Intern log bot from heroku configs
        '',
        INTERN_LOG_MESSAGE # message
    )
