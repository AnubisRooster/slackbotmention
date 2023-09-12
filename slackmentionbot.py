import os
import logging
import csv
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.error import BoltUnhandledRequestError
from slack_bolt import BoltResponse
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = App(token=os.environ.get("SLACK_TOKEN"), raise_error_for_unhandled_request=True)

@app.error
def handle_errors(error):
    if isinstance(error, BoltUnhandledRequestError):
        return BoltResponse(status=200, body="")
    else:
        return BoltResponse(status=500, body="Something Wrong")

def get_assignee_string(jira_message, logger):
    # Modify the regular expression to match the new Assignee format
    m = re.search('Assignee: (.*?) \|', jira_message)
    if m:
        found = m.group(1)

    result = re.sub('[^a-zA-Z ]+', '', found)
    assignee_name = result.strip()
    return assignee_name

def find_assignee_slackid_in_csv(csv_filename, assignee_name, logger):
    csv_file = csv.reader(open(csv_filename, "r"), delimiter=",")
    for row in csv_file:
        if assignee_name.lower() == row[2].lower():
            assignee_slack_id = row[0]
            return assignee_slack_id

@app.message()
def read_incoming_message(event, say, logger):
    slackid_csvfilename = 'slack_user_id_list.csv'
    logger.info("************* Incoming message is " + event['text'])

    target_channel = 'C05H6GPHW93'

    message_lines = event['text'].split('\n')

    # Initialize a dictionary to store Assignee names and their corresponding Slack IDs
    assignee_mapping = {}

    # Iterate through the message lines to find Assignees and build the mapping
    for line in message_lines:
        if "Assignee:" in line:
            assignee_name = get_assignee_string(line, logger)

            # Try to find the assignee's Slack ID in the CSV file
            assignee_slack_id = find_assignee_slackid_in_csv(slackid_csvfilename, assignee_name, logger)

            # Add Assignee name and Slack ID to the mapping dictionary
            assignee_mapping[assignee_name] = assignee_slack_id

    logger.info("Assignee Mapping: " + str(assignee_mapping))  # Debugging line

    # Iterate through the message lines again to replace Assignee names with Slack mentions
    modified_message_final = ""

    for line in message_lines:
        modified_line = line

        for assignee_name, assignee_slack_id in assignee_mapping.items():
            if assignee_name and assignee_slack_id:
                modified_line = modified_line.replace(assignee_name, f"<@{assignee_slack_id}>")

        modified_message_final += modified_line + "\n"

    # Check if the message has already been posted
    if not event.get('message_posted'):
        say(modified_message_final, channel=target_channel)
        logger.info("Modified message sent to channel: " + target_channel)

        # Mark the message as posted to prevent duplication
        event['message_posted'] = True

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
