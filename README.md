# uwdailysx

A simple app that sends messages to a groupme account via a registered bot

## To add a bot to the scheduled messages list
- Go to the (GroupMe developers site)|[https://dev.groupme.com/tutorials/bots#:~:text=Bots%20Tutorial,to%20users%20in%20SMS%2Dmode.] and create a bot for the group you want to send messages to.
- Once you have your bot id go to the (Heroku)|[https://dashboard.heroku.com/apps] dashboard for uwdailysx. Click the `Settings` menu and scroll to `Config Vars` and click `Reveal Config Vars`.
- Add the new bot id (the one you got from GroupMe) in the `VALUE` box and name it something appropriate in the `KEY` box. (make sure to use all caps and separate words with _  for example, `GROUPME_SPORTNAME_BOT_ID`)
- Click `Add`
- Copy this key name and go to (the code)|[https://github.com/miriam-cortes/uw_daily_sx/blob/master/send_messages.py]
- Click the pencil icon toward the top of the code so you can edit in Github
- Paste the key name into the `GROUPME_BOT_IDS` list that starts on line 7 (make sure you're putting it in single quotes and separating with a comma)
- In the `commit changes` box below the code, add the message "added GROUPME_SPORTNAME_BOT_ID" and click the green "Commit changes" button.
- This should kick off a deploy in Heroku. Click the `Overview` menu and you should see on the right column a new deploy started a few seconds ago. Give it a minute and maybe refresh the page if you haven't seen it start.
- The next time the scheduled job runs it will send a message to the new group as well.