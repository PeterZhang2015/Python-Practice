import sys
import os
import requests
from requests.auth import HTTPBasicAuth
import json
import time
from datetime import datetime
import subprocess

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
    url = "http://{}:{}/api".format(management_ip, management_port)

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
    url = "http://{}:{}/api/libraries/{}/testSessions".format(management_ip, management_port, libraries_id)

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

    # Construct the URL to execute test session.
    url = "http://{}:{}/api/runningTests".format(memenanagt_ip, management_port)

    # Execute Landslide test session with the input body through Landslide REST API.
    response = requests.post(url, body, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Get running test session id if it has been executed successfully from the API information response.
    test_session_info = json.loads(response.text)
    response_code = test_session_info["code"]

    if response_code != "200":  # Fail to run the test session.
        print "Fail to execute the test session."
        sys.exit()

    test_session_id = test_session_info["id"]

    return test_session_id

#################stopLandslideTestSession#################################.
def stopLandslideTestSession(management_ip, management_port, username, password, test_session_id):

    # Construct the URL to execute test session.
    url = "http://{}:{}/api/runningTests/{}?action = stop".format(management_ip, management_port, test_session_id)

    # Stop test session running through Landslide REST API.
    response = requests.post(url, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Check whether the test session has been stopped successfully from the API information response.
    test_session_info = json.loads(response.text)
    result = test_session_info["result"]

    if result != "Command successful":  # Fail to stop the test session.
        print "Fail to stop the test session."
        sys.exit()

#################getTestMeasurements#################################.
def getTestMeasurements(management_ip, management_port, username, password, test_session_id):
    # Initialize variables.
    test_summary_list = []

    # Construct the URL to execute test session.
    url = "http://{}:{}/api/runningTests/{}/measurements/".format(management_ip, management_port, test_session_id)

    # Get test measurements running through Landslide REST API.
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Check REST API response.
    test_measurement_info = json.loads(response.text)
    result = test_measurement_info["result"]

    if result != "Command successful":  # Fail to stop the test session.
        print "Fail to stop the test session."
        sys.exit()

    for test_server in test_measurement_info["testServers"]:
        for test_case in test_server["testCases"]:
            test_summary_list.append(test_case["tabs"]["Test Summary"])

    return test_summary_list


#################getTestCriteriasResult#################################.
def getTestCriteriasResult(management_ip, management_port, username, password, test_session_id):

    # Initialize variables.
    test_criteria_result_list = []

    # Construct the URL to execute test session.
    url = "http://{}:{}/api/runningTests/{}/criteria/".format(management_ip, management_port, test_session_id)

    # Get test criterias result through Landslide REST API.
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Check REST API response.
    test_criteria_info = json.loads(response.text)
    result = test_criteria_info["criteriaStatus"]

    if result != "PASSED":  # Fail to stop the test session.
        print "Test session failed according to the criteria on Landslide test session."
        sys.exit()

    test_criteria_result_list = test_criteria_info["criteria"]

    return test_criteria_result_list

#################getTestWiresharkPcapUrl#################################.
def getTestWiresharkPcapUrl(management_ip, management_port, username, password, test_session_id, pcap_port_name):

    # Initialize variables.
    test_criteria_result_list = []

    # Construct the URL to execute test session.
    url = "http://{}:{}/api/runningTests/{}/capturefiles/0/{}".format(management_ip, management_port, test_session_id, pcap_port_name)

    # Get test wireshark pcap url through Landslide REST API.
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.text)

    # Check REST API response.
    wireshark_pcap_info = json.loads(response.text)
    response_code = wireshark_pcap_info["code"]

    if response_code != "200":  # Fail to get the wireshark pcap url.
        print "Fail to get wireshark pcap url."
        sys.exit()

    wireshark_pcap_url = wireshark_pcap_info["captureFileUrl"]

    return wireshark_pcap_url


#################constructTestSessionExecutionBody#################################.
def constructTestSessionExecutionBody(libraries_id, test_session_name, parameters_data=None):

    # Initialize variables
    test_case_data = {}
    test_cases_data = []
    tsGroup_data = {}
    tsGroups_data = []
    data = {}

    # Insert the input json parameters data if parameters_data is not equal to None.
    if parameters_data != None:
        test_case_data['parameters'] = parameters_data
    else:
        test_case_data['parameters'] = {}

    # Starting to construct the basic json body for the REST API to execute Landslide test session.
    test_cases_data.append(test_case_data)
    tsGroup_data['tsId'] = 2
    tsGroup_data['testCases'] = test_cases_data
    tsGroups_data.append(tsGroup_data)

    data['library'] = libraries_id
    data['name'] = test_session_name
    data['tsGroups'] = tsGroups_data

    # Transfer the Python dictionary data structure to Json format.
    json_data = json.dumps(data, indent=4)
    print(json_data)

    return json_data


#################downloadFile#################################.
def downloadFile(username, password, remote_file_location, local_file_location):

    # Download file from the remote file location by curl command.
    subprocess.check_output(['curl', '--ntlm', '-u', username, password, remote_file_location, local_file_location])

    # Check whether the file was downloaded successfully or not.
    if os.path.isfile(local_file_location):
        print "Successfully download {}".format(remote_file_location)
    else:
        print "Failed to download {}".format(remote_file_location)
        sys.exit()



#################getTsharkFilterResults#################################.
def getTsharkFilterResults(pcap_file, filter_str):

    # Initialize variables
    frame_number_list = []

    # Decode pcap file by tshark command.
    response = subprocess.check_output(['tshark', '-nr', pcap_file, '-Y', filter_str])

    # Split the filtered result lines.
    line_list = response.splitlines()
    print len(line_list)

    # Get frame number list of the matched results.
    for line in line_list:
        # Delete the leading space of a line and split it by space character.
        line = line.lstrip()
        temp_list = line.split(' ')

        # Take the first element as the frame number.
        frame_number_list.append(temp_list[0])

    # Return frame number list of the matched results
    return frame_number_list


#################wiresharkAnalysis#################################.
def wiresharkAnalysis(pcap_file, target_web_host, redirect_url):

    # Set filter string for checking HTTP host
    filter_str = "http.host == {}".format(target_web_host)

    # Find the request frame number list that can match with the filter in the wireshark pcap.
    request_frame_number_list = getTsharkFilterResults(pcap_file, filter_str)
    matched_result_number = len(request_frame_number_list)
    if matched_result_number > 0:
        print "HTTP Get with web host {} found".format(target_web_host)
    else:
        print "HTTP Get with web host {} cannot been found".format(target_web_host)
        sys.exit()

    # Check there is response for each request frame.
    for request_frame_number in request_frame_number_list:
        # Set filter string for checking response of each request.
        filter_str = "tcp.analysis.acks_frame == {} && http.response.code == 302 && http.location ==  \"{}\"".format(request_frame_number, redirect_url)

        # Find the frame number list that can match with the filter in the wireshark pcap.
        response_frame_number_list = getTsharkFilterResults(pcap_file, filter_str)
        matched_result_number = len(response_frame_number_list)
        if matched_result_number > 0:
            print "Find matched response for HTTP Get request with frame number {}".format(request_frame_number)
        else:
            print "Cannot find matched response for HTTP Get request with frame number {}".format(request_frame_number)
            sys.exit()

    print "Find matched response for all HTTP Get request!"

#################Main test logical#################################.
def main():

    #Testing arguments
    management_ip = "10.195.44.94"
    management_port = "8080"
    username = "sms"
    password= "a1b2c3d4"
    library_name = "sms"
    test_session_name = "TempWebBrowsingWap"

    pcap_port_name = "eth1"

    local_download_folder =  "c:/temp/"
    test_case_name = os.path.basename(sys.argv[0][:-3])
    timeStamp = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
    local_pcap_location = "{}{}{}.pcap".format(local_download_folder, test_case_name, timeStamp)
    print local_pcap_location

    MmeSut_data = {}
    MmeSut_data['class'] = "Sut"
    MmeSut_data['name'] = "173.0.0.124"
    parameters_data = {}
    parameters_data['MmeSut'] = MmeSut_data

    target_web_host = "wap.telstra.com"
    redirect_url = "http://m.bigpond.com"


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
        print "{} exists on Landslide.".format(test_session_name)
    else:
        print "{} does not exist on Landslide, abort execution.".format(test_session_name)
        sys.exit()

    # Construct post data structure to execute Landslide test session with optional modified parameters.
    json_data = constructTestSessionExecutionBody(libraries_id, test_session_name, parameters_data)

    # #Run the test session and get the running test session ID.
    # test_session_id = executeLandslideTestSession(management_ip, management_port, username, password, json_data)
    # print test_session_id
    #
    # #Setting waiting time for the test session execution.
    # time.sleep(10)
    #
    # #Stop the running test session.
    # stopLandslideTestSession(management_ip, management_port, username, password, test_session_id)

    test_session_id =

    #Get test measurements.
    test_summary_list = getTestMeasurements(management_ip, management_port, username, password, test_session_id)
    print test_summary_list

    #Get test criterias results.
    test_criteria_result_list = getTestCriteriasResult(management_ip, management_port, username, password, test_session_id)
    print test_criteria_result_list

    #Get wireshark pcap url.
    wireshark_pcap_url = getTestWiresharkPcapUrl(management_ip, management_port, username, password, test_session_id, pcap_port_name)
    print wireshark_pcap_url

    #Download wireshark pcap from Landslide.
    download_result = downloadFile(username, password, wireshark_pcap_url, local_pcap_location)
    if download_result != "Successful":
        print "Fail to download wireshark pcap file from Landslide, abort."
        sys.exit()
    else:
        print "Get wireshark pcap from Landslide successfully."

    #Analyze the downloaded wireshark pcap.
    #wiresharkAnalysis(pcap_file, target_web_host, redirect_url)


#Call main function.
if __name__ == "__main__":
    main()