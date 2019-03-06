import sys
import requests
from requests.auth import HTTPBasicAuth
import json

#Get Parameters calling this python script
# management_ip = sys.argv[1]
# print ("***********management_ip*************")
# print(management_ip)
#
# management_port = sys.argv[2]
# print ("***********management_port*************")
# print(management_port)
#
#
# library_name = sys.argv[3]
# print ("***********library_name*************")
# print(api_url)
#
#
# username = sys.argv[4]
# print ("***********username*************")
# print(username)
#
# password = sys.argv[5]
# print ("***********password*************")
# print(password)



#################getLibrariesPath#################################.
def getLibrariesPath(management_ip, management_port, username, password):

    # Construct the URL to get the Libraries path.
    url = "http://" + management_ip + ":" + management_port + "/api"
    print url

    # Get API information through Landslide REST API.
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print response.text

    # Get libraries path from the API information response.
    data = json.loads(response.text)
    libraries_path = data["libraries"]

    return libraries_path

#################getLibrariesId#################################.
def getLibrariesId(libraries_path, library_name, username, password):

    # Get libraries information through Landslide REST API.
    response = requests.get(libraries_path, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Get library id from the API information response.
    libraries_info = json.loads(response.text)
    data_list = libraries_info["libraries"]
    for data in data_list:
        #Get the library id of input library name.
        if data["name"] == library_name:  # And room also, then update info.
            libraries_id = data["id"]
            exit

    return str(libraries_id)

#################getTestSessionsName#################################.
def getTestSessionsName(management_ip, management_port, libraries_id, username, password):

    # Initialize the return list.
    test_sessions_name_list = []

    # Construct the URL to get the test sessions name list.
    url = "http://" + management_ip + ":" + management_port + "/api/libraries/" + libraries_id + "/testSessions"
    print url

    # Get libraries information through Landslide REST API.
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Get test sessions name list from the API information response.
    formated_response = json.loads(response.text)
    testSessionsList = formated_response['testSessions']
    for testSession in testSessionsList:
        name = testSession['name']
        test_sessions_name_list.append(name)

    return test_sessions_name_list


#################Main test logical#################################.
def main():

    #Testing arguments
    management_ip = "10.195.44.94"
    management_port = "8080"
    username = "sms"
    password= "a1b2c3d4"
    library_name = "sms"
    test_session_name = "TempWebBrowsingWap"

    #Get libraries path.
    libraries_path = getLibrariesPath(management_ip, management_port, username, password)
    print libraries_path

    #Get libraries id.
    libraries_id = getLibrariesId(libraries_path, library_name, username, password)
    print libraries_id

    #Get test sessions name list.
    test_sessions_name_list = getTestSessionsName(management_ip, management_port, libraries_id, username, password)
    print test_sessions_name_list

    # Check whether the test session exists in test sessions name list.
    if test_session_name in test_sessions_name_list:
        print test_session_name + " exists on Landslide."
    else:
        print test_session_name + " does not exist on Landslide."
        sys.exit()



#Call main function.
if __name__ == "__main__":
    main()