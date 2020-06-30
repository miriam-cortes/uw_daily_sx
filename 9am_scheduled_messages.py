import os
from datetime import date
from send_messages import send_message
from constants import QUARANTINE_MESSAGE

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


# DAILY FOOTBALL MESSAGE TO QUARANTINED ATHLETES
send_message(
    'FOOTBALL_Q_BOT_ID', # football-quarantined bot from heroku configs
    os.environ.get('FB_Q_DAILY'), # google form link from heroku configs
    QUARANTINE_MESSAGE # message
)
# DAILY OLYMPIC MESSAGE TO QUARANTINED ATHLETES
send_message(
    'OLY_Q_BOT_ID', # olympics-quarantined bot from heroku configs
    os.environ.get('OLY_Q_DAILY'), # google form link from heroku configs
    QUARANTINE_MESSAGE # message
)
# DAILY MESSAGE TO QUARANTINED STUDENT INTERNS
send_message(
    'STUDENT_Q_BOT_ID', 
    os.environ.get('STUDENT_Q_DAILY'), 
    QUARANTINE_MESSAGE # message
)
# DAILY MESSAGE TO QUARANTINED STUDENT MANAGERS
send_message(
    'MANAGER_Q_BOT_ID', #
    os.environ.get('MANAGER_Q_DAILY'), 
    QUARANTINE_MESSAGE # message
)
