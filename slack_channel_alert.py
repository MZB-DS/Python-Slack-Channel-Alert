from slackclient import SlackClient
import time
from sqlquery_to_df import get_data

token = '' # Enter your slack app token
slack_client = SlackClient(token)

count=0

while True:

  queries = 'select count(*) from people_information where city="PUNE";'
  column_names = ["Count"]
  sql_query_output_df = get_data(queries, column_names)

  count1 = sql_query_output_df["Count"][0]

  if count1>count: # Condition for triggering the alert
    count=count1
    text="New person added in the Pune city. Kindly check" #Message you want to post.
    slack_client.api_call("chat.postMessage",channel='Channel_Name',text=text) # Enter the slack channel yo want to trigger this alert on.

  time.sleep(30)
