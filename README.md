# uwdailysx

A simple app that sends messages to a groupme account via a registered bot

## To add a bot to the scheduled messages list
1. Go to the [GroupMe developers site](https://dev.groupme.com/tutorials/bots#:~:text=Bots%20Tutorial,to%20users%20in%20SMS%2Dmode.) and create a bot for the group you want to send messages to.
2. Once you have your bot id go to the [Heroku](https://dashboard.heroku.com/apps) dashboard for uwdailysx. Click the `Settings` menu and scroll to `Config Vars` and click `Reveal Config Vars`.
3. Add the new bot id (the one you got from GroupMe) in the `VALUE` box and name it something appropriate in the `KEY` box. (make sure to use all caps and separate words with _  for example, `GROUPME_SPORTNAME_BOT_ID`)
4. Click `Add`
5. Copy this key name and go to [the code](https://github.com/miriam-cortes/uw_daily_sx)
6. Check if there is already a file with the time that you want your message sent. If there is, click to open that file and go to step 7. If not, open one of the other files and copy all the code in there to a new file named with the time this message should be sent and end it in `_scheduled_messages.py` continue with step 8.
7. Click the pencil icon toward the top of the code so you can edit in Github
8. Copy one of the `send_message(...)` pieces of code and paste it at the bottom of the page (make sure to leave one line at the end....for reasons).  Make sure to change the BOT_ID and Google form link to the keys you put in the Heroku configs in step 3. If there should be a different message add it to [the constants file](https://github.com/miriam-cortes/uw_daily_sx/blob/master/constants.py) and make sure to import it in line 4 of your file.
9. In the `commit changes` box below the code, add the message "added GROUPME_SPORTNAME_BOT_ID" and click the green "Commit changes" button.
10. This should kick off a deploy in Heroku. Click the `Overview` menu and you should see on the right column a new deploy started a few seconds ago. Give it a minute and maybe refresh the page if you haven't seen it start.
11. Create a new scheduled job in Heroku, following the pattern from the other jobs (don't forget times are UTC!)
12. The next time the scheduled job runs it will send a message to the new group as well! :self-high-five: you did it!
