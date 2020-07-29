# Python-Slack-Channel-Alert
This repository contains python code for programming slack user bot for posting alerts on any slack channel. Slack is a messenger which is both free and paid. The basic idea behind this code is to provide a setup where we can post a conditional alert in any slack channel. Here as a conditional alert, the alert is set when any new record is entered in the people_information for Pune city.

## How to use this code
1. Sign in to your slack account.
2. Create a slack app from this link "https://api.slack.com/apps/new" to recieve an API token for your bot.
3. Provide proper mysql host ip, username, password and any database name in ```sqlquery_to_df.py``` file.
4. Provide in ```slack_channel_alert.py```, your slack bot api token in 'token' variable, your mysql select query and the respective column names for your output dataframe.
5. Provide slack channel name, where you want to post the alert, in the slack api call.
6. The default check is of the 30 seconds interval. The frequency can be reduced or increased as per the alert requirement and can be updated in the time.sleep() method.
7. Execute ```slack_channel_alert.py```.

## Future Features
Adding the feature of responding with csv, xlsx and txt files to the bot.

## Dependencies
- Python3 any version
- Slack account
- Python package: slackclient==1.3.1, time, pandas==1.0.3, mysql-connector==2.2.9

```pip3 install slackclient==1.3.1 pandas==1.0.3 mysql-connector==2.2.9```
