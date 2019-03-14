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
def getLibrariesId(libraries_path, username, password, library_name):

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
def getTestSessionsName(management_ip, management_port, username, password, libraries_id):

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

#################executeLandslideTestSession#################################.
def executeLandslideTestSession(management_ip, management_port, username, password, body):

    # Initialize internal variable.
    test_session_id = 0

    # Construct the URL to execute test session.
    url = "http://" + management_ip + ":" + management_port + "/api/runningTests"

    # Get libraries information through Landslide REST API.
    response = requests.post(url, body, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Get library id from the API information response.
    test_session_info = json.loads(response.text)
    response_code = test_session_info["code"]


    if response_code != "200":  # Fail to run the test session.
        print "Fail to execute the test session."
        sys.exit()

    test_session_id = test_session_info["id"]

    return test_session_id



#################Main test logical#################################.
def main():

    #Testing arguments
    management_ip = "10.195.44.94"
    management_port = "8080"
    username = "sms"
    password= "a1b2c3d4"
    library_name = "sms"
    test_session_name = "TempWebBrowsingWap"
    tsGroups_number = 1
    test_cases_number = 1

    MmeSut_data = {}
    MmeSut_data['class'] = "Sut"
    MmeSut_data['name'] = "173.0.0.124"
    parameters_data = {}
    parameters_data['MmeSut'] = MmeSut_data

    test_case_data = {}
    test_case_data['parameters'] = parameters_data

    test_cases_data = []
    test_cases_data.append(test_case_data)

    tsGroup_data = {}
    tsGroup_data['tsId'] = 2
    tsGroup_data['testCases'] = test_cases_data

    tsGroups_data = []
    tsGroups_data.append(tsGroup_data)


    #Get libraries path.
    libraries_path = getLibrariesPath(management_ip, management_port, username, password)
    print libraries_path

    #Get libraries id.
    libraries_id = getLibrariesId(libraries_path, username, password, library_name)
    print libraries_id

    #Get test sessions name list.
    test_sessions_name_list = getTestSessionsName(management_ip, management_port, username, password, libraries_id)
    print test_sessions_name_list

    # Check whether the test session exists in test sessions name list.
    if test_session_name in test_sessions_name_list:
        print test_session_name + " exists on Landslide."
    else:
        print test_session_name + " does not exist on Landslide, abort execution."
        sys.exit()

    # Construct post data structure.
    data = {}
    data['library'] = libraries_id
    data['name'] = test_session_name
    data['tsGroups'] = tsGroups_data
    json_data = json.dumps(data, indent=4)
    print(json_data)

    #Run the test session and get the running test session ID.
    test_session_id = executeLandslideTestSession(management_ip, management_port, username, password, json_data)
    print test_session_id


#Call main function.
if __name__ == "__main__":
    main()