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
            slack_user_id = user["id"]
            user_csl = user["name"]
            real_name = user["profile"]["real_name"]
            deleted_user = user["deleted"] # return true or false. true for users that have been deactivated


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
    U026GDM4B26 dbooker Danny Booker
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
