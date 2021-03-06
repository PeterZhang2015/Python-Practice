from selenium import webdriver

import time
import sys
import Selenium2Library
import json
import re
import requests
from requests.auth import HTTPDigestAuth

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

#Set variables
usr = "admin"
pwd = "admin"
kibana_url = "https://{}:{}@192.168.32.75:5601".format(usr, pwd)

target_test_case_name = "main/Temp/test_cases/temp.fftc"

recent_records_number = 10

#Set functions
#Function of open web url with max browser window.
def OpenWebUrlWithMaxWindow(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    return browser

#Function of expand some records on Kibana.
def ExpandRecentRecordsOnKibana(elements, elements_xpath, recent_records_number):
    elements_number = len(elements)
    print ("Record number", elements_number)

    index = 0

    # Expand all json data.
    while elements_number > 0 and recent_records_number > 0:
        print(index)

        # Click the link element
        elements[index].click()

        # Re-define link element
        elements = browser.find_elements_by_xpath(elements_xpath)

        # Modify loop variables
        index = index + 1
        element_numbers = elements_number - 1
        recent_records_number = recent_records_number - 1
        # end of while elements_number > 0 and recent_records_number > 0:

#Function of expand some records on Kibana.
def ExpandRecentJsonOnKibanaRecords(elements, elements_xpath, recent_records_number):

    elements_number = len(elements)
    print ("Json number", elements_number)
    index = 0

    # loop to expand all json area
    while elements_number > 0 and recent_records_number > 0:
        print(index)

        # Get test case path information from expand json data
        elements[index].click()

        # Re-define link element
        elements = browser.find_elements_by_xpath(elements_xpath)

        index = index + 1
        elements_number = elements_number - 1

        recent_records_number = recent_records_number - 1
        # end of while elements_number > 0 and recent_records_number > 0:

#POST customized data to the recent record with the same test path name on Kibana.
def PostCustomizedDataToLatestRecord(elements, elements_xpath, recent_records_number, target_test_case_name, insert_field):

    elements_number = len(elements)
    print ("json value number", elements_number)

    index = 0

    # loop all json value text area.
    while elements_number > 0 and recent_records_number > 0:

        print ("***********index*************8")
        print(index)

        # json_information_text = repr(json_value_element[index].text)
        json_information_text = elements[index].text
        print ("***********json_information_text*************8")
        print(json_information_text)
        time.sleep(2)

        if json_information_text:
            data = json.loads(json_information_text.replace('\n', ''))
            test_case_name = data["_source"]["testPath"]
            print ("***********test case name from format json*************8")
            print (test_case_name)

            data_index = data["_index"]
            print ("***********index from format json*************8")
            print (data_index)

            type = data["_type"]
            print ("***********type from format json*************8")
            print (type)

            id = data["_id"]
            print ("***********test id from format json*************8")
            print (id)

            if (test_case_name == target_test_case_name):
                print ("Found testing case name:", test_case_name)

                m = re.sub(r'(.*)("agentId":)', r'\1{}\2'.format(insert_field), json_information_text)
                print ("***********POST body*************8")
                print (m)

                temp_data = json.loads(m)
                json_source = temp_data["_source"]
                json_source = json.dumps(json_source)

                print ("***********json_source*************8")
                print (json_source)

                url = 'https://192.168.32.75:9200/{}/{}/{}'.format(data_index, type, id)
                print ("***********post URL*************8")
                print (url)

                username = "api"
                password = "index"

                # response = requests.post(url, data=m, auth=('api', 'index'))
                # response = requests.post(url, data=json_source,  auth=HTTPDigestAuth(raw_input("api"), raw_input("index")), verify=True)
                response = requests.post(url, data=json_source, auth=('api', 'index'), verify=False)
                print ("***********post response*************8")
                print (response)

                break
            else:
                print "Continue"
        else:
            print "Continue"

        # Re-define link element
        elements = browser.find_elements_by_xpath(elements_xpath)

        index = index + 1
        elements_number = elements_number - 1

        recent_records_number = recent_records_number - 1
        # end of while record_element_number > 0 and avoid_dead_loop_counter > 0:


#Open URL with specified web browser.
browser = OpenWebUrlWithMaxWindow(kibana_url)
time.sleep(12)

#Find the record elements according to attribute.
records_path ='//*[@data-test-subj="docTableExpandToggleColumn"]'
record_elements = browser.find_elements_by_xpath(records_path)
#Expand some recent records on Kibana.
ExpandRecentRecordsOnKibana(record_elements, records_path, recent_records_number)

#Find the json elements according to attribute.
json_path = '//*[@ng-click="mode=\'JSON\'"]'
json_elements = browser.find_elements_by_xpath(json_path)
#Expand some recent Json on Kibana records.
ExpandRecentJsonOnKibanaRecords(json_elements, json_path, recent_records_number)

#Find the json elements according to attribute.
json_value_path = '//*[@class="ace_content"]'
json_text_elements = browser.find_elements_by_xpath(json_value_path)

#Post customized data to recent Kibana record with the same test path name.
output_file_name = "output_response.txt"
file = open(output_file_name, "r")
insert_field = file.read()
#insert_field = '"testCustomedField": {},\\n    '.format(testCustomizedField)
PostCustomizedDataToLatestRecord(json_text_elements, json_value_path, recent_records_number, target_test_case_name, insert_field)














