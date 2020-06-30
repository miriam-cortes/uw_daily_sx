import os
from datetime import date
from send_messages import send_message
from constants import OTHER_MESSAGE

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


# DAILY FOOTBALL MESSAGE TO ONSITE ATHLETES
send_message(
    'FOOTBALL_ONSITE_BOT_ID', # football-onsite bot from heroku configs
    os.environ.get('FB_ONSITE_DAILY'), # google form link from heroku configs
    OTHER_MESSAGE # message
)
# DAILY OLYMPIC MESSAGE TO ONSITE ATHLETES
send_message(
    'OLY_ONSITE_BOT_ID', # olympic-onsite bot from heroku configs
    os.environ.get('OLY_ONSITE_DAILY'), # google form link from heroku configs
    OTHER_MESSAGE # message
)
# DAILY MESSAGE TO ONSITE STUDENT INTERNS
send_message(
    'STUDENT_ONSITE_BOT_ID', 
    os.environ.get('STUDENT_ONSITE'), # google form link from heroku configs
    OTHER_MESSAGE # message
)
# DAILY OLYMPIC MESSAGE TO ONSITE ATHLETES
send_message(
    'MANAGER_ONSITE_BOT_ID', # olympic-onsite bot from heroku configs
    os.environ.get('MANAGER_ONSITE'), # google form link from heroku configs
    OTHER_MESSAGE # message
)
