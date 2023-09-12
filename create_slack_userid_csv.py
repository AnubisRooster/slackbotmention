import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import csv 
from csv import writer

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

def start():

    #### CREATE A NEW CSV FILE TO STORE SLACK USER ID's
    # field names 
    fields = ['slack_user_id', 'user_csl', 'real_name'] 
    # name of csv file 
    filename = "slack_user_id_list.csv"

    # create csv file and write column headings
    create_csv_file_for_slack_userid_data(filename, fields)

    #### GET A LIST OF SLACK USER IDS, NAMES
    try:
        # Call the users.list method using the WebClient
        # users.list requires the users:read scope

        result = []
        for paginated_response in client.users_list(limit=1000):
            result += paginated_response["members"]

        #result = client.users_list()
        #print(result, end='\n\n')


        #for user in result["members"]:
        for user in result:
            #print(user, end='\n\n\n')
            #{'id': 'U026GDM4B25', 'team_id': 'T02G42F7P', 'name': 'tbooker-ctr', 'deleted': True, 'profile': {'title': 'Procurement', 'phone': '5037013052', 'skype': '', 'real_name': 'Toni Booker', 'real_name_normalized': 'Toni Booker', 'display_name': 'tbooker-ctr', 'display_name_normalized': 'tbooker-ctr', 'fields': None, 'status_text': '', 'status_emoji': '', 'status_emoji_display_info': [], 'status_expiration': 0, 'avatar_hash': 'b097db3e7a39', 'image_original': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_original.jpg', 'is_custom_image': True, 'first_name': 'Toni', 'last_name': 'Booker', 'image_24': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_24.jpg', 'image_32': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_32.jpg', 'image_48': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_48.jpg', 'image_72': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_72.jpg', 'image_192': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_192.jpg', 'image_512': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_512.jpg', 'image_1024': 'https://avatars.slack-edge.com/2021-06-28/2219465672691_b097db3e7a39662e6f93_1024.jpg', 'status_text_canonical': '', 'team': 'T02G42F7P'}, 'is_bot': False, 'is_app_user': False, 'updated': 1631619826}

            slack_user_id = user["id"]
            user_csl = user["name"]
            real_name = user["profile"]["real_name"]
            deleted_user = user["deleted"] # return true or false. true for users that have been deactivated
            #print(real_name)


            # write user_id slack data to csv file if they are not in deleted/deactivated state
            if not deleted_user:
                write_userid_list_to_csv(filename, slack_user_id, user_csl,real_name)

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

# CREATE A NEW CSV FILE TO STORE SLACK USER ID's 
def create_csv_file_for_slack_userid_data(filename, fields):

    # open the file in the write mode
    f = open(filename, 'w')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(fields)

    # close the file
    f.close()

#### WRITE USER_ID LIST TO CSV
def write_userid_list_to_csv(filename, slack_user_id, user_csl, real_name):
    #print(slack_user_id, user_csl,real_name)
    '''
    U026GDM4B25 tbooker-ctr Toni Booker
    '''

    # data rows of csv file 
    row_data = []
    row_data.append(slack_user_id)
    row_data.append(user_csl)
    row_data.append(real_name)
    #print(row_data)

    #row_data = ['6', 'William', '5532']
        
    # writing to csv file 
    with open(filename, 'a') as csvfile: 
        # Pass this file object to csv.writer() and get a writer object
        writer_object = writer(csvfile)
    
        # Pass the list as an argument into the writerow()
        writer_object.writerow(row_data)
    
        # Close the file object
        csvfile.close()

if __name__=="__main__":
    start()
