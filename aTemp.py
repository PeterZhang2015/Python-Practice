# -*- coding: utf-8 -*-
# from selenium import webdriver
#
# import time
# import sys
# import Selenium2Library
# import json, ast
# import re
#
# #Set testing url
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# output_file_name = "json_data.txt"
# file = open(output_file_name, "r")
# json_information_text = file.read()
#
# print ("***********json_information_text*************8")
# print(json_information_text)
#
# time.sleep(2)
#
# if json_information_text:
#     data = json.loads(json_information_text.replace('\n', ''))
#     test_case_name = data["_source"]["testPath"]
#     print ("***********test case name from format json*************8")
#     print (test_case_name)
#
#     data_index = data["_index"]
#     print ("***********index from format json*************8")
#     print (data_index)
#
#     type = data["_type"]
#     print ("***********type from format json*************8")
#     print (type)
#
#     id = data["_id"]
#     print ("***********test id from format json*************8")
#     print (id)
#
#     time.sleep(2)
#     reportIdPath = data["_source"]["reportIdPath"]
#     print ("***********reportIdPath*************8")
#     print (reportIdPath)

# import time
# from datetime import datetime
#
# import os
# import sys
#
# local_download_folder = "c:/temp/"
#
# test_case_name = os.path.basename(sys.argv[0][:-3])
#
# print test_case_name
#
# timeStamp = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
#
# local_pcap_location = local_download_folder + test_case_name + timeStamp + ".pcap"
#
# print local_pcap_location


import os
import subprocess
import re
import sys
#################getTsharkRequest#################################.
def getTsharkRequest(pcap_file, filter_str, packet_fields=None, return_data=None):

    # Initialize variables.
    temp_display_list = []
    d_field_string = ""

    # Build up the display fields
    if packet_fields != None:
        temp_list = packet_fields.split(',')
        for packet_field in temp_list:
            new_val = "-e $i "
            temp_display_list.append(new_val)
        d_field_string.join(temp_display_list)

    # Decode pcap file
    if len(temp_display_list) > 0:
        response = subprocess.check_output(['tshark', '-nr', pcap_file, '-Y', filter_str, '-T', 'fields', 'd_field_string'])
    else:
        response = subprocess.check_output(['tshark', '-nr', pcap_file, '-Y', filter_str])

    print response

    line_list = response.splitlines()


    print "result number is: " + str(len(line_list))

    return len(line_list)


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

    # Find the frame number list that can match with the filter in the wireshark pcap.
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

    target_web_host = "wap.telstra.com"
    redirect_url = "http://m.bigpond.com"

    # getTsharkRequest(local_pcap_location, filter_str)
    # local_pcap_location = "c:/temp/WebBrowsingWap_2018-08-21_143947.pcap"
    # frame_number_list = getTsharkFilterResults(local_pcap_location, filter_str)
    # print len(frame_number_list)

    pcap_file = "c:/temp/WebBrowsingWap_2018-08-21_143947.pcap"
    target_web_host = "wap.telstra.com"
    redirect_url = "http://m.bigpond.com"

    wiresharkAnalysis(pcap_file, target_web_host, redirect_url)

    # result = os.path.isfile('c:/temp/WebBrowsingWap_2018-08-21_143947.pcap')
    # print result

    # response = "71 2018-08-20 19:19:27.045757 144.140.217.42 → 10.61.2.180   HTTP/1.1 302 Found  (text/html) 491 GTP <HTTP>"
    # match_result = re.findall(r"(\d+) (\S+) (\S+) (\S+) (\S+) (.*) (\S+) (\d+) (\S+) (\S+)", response)
    # print match_result
    #response = "70 2018-08-20 19:19:27.029767  10.61.2.180 → 144.140.217.42 GET /wap HTTP/1.1\r\n Continuation 312 GTP <HTTP>"

    # response = "70 2018-08-20 19:19:27.029767  10.61.2.180 → 144.140.217.42 GET /wap HTTP/1.1\r\n"
    # match_result = re.findall(r"(\d+) (\S+) (\S+)  (\S+) (\S+) (\S+) (\S+) (.*)\n", response)
    # print match_result


if __name__ == "__main__":
    main()





