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

url = "https://{}:{}@192.168.32.75:5601".format(usr, pwd)

project_path = "main/Temp"
target_test_case_name = "main/Temp/test_cases/temp.fftc"


#Open URL with specified web browser.
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

time.sleep(8)

#Find the element according to CSS name.
records_path ='//*[@data-test-subj="docTableExpandToggleColumn"]'

#define link element
record_element = browser.find_elements_by_xpath(records_path)
record_element_number = len(record_element)
print ("Record number", record_element_number)

avoid_dead_loop_counter = 100
index = 0

# Expand all json data.
while record_element_number > 0 and avoid_dead_loop_counter > 0:

    print(index)

    #Click the link element
    record_element[index].click()

    # Re-define link element
    record_element = browser.find_elements_by_xpath(records_path)

    #Modify loop variables
    index = index + 1
    record_element_number = record_element_number - 1
    avoid_dead_loop_counter = avoid_dead_loop_counter - 1
    # end of while record_element_number > 0 and avoid_dead_loop_counter > 0:

#define link element
record_element = browser.find_elements_by_xpath(records_path)
record_element_number = len(record_element)

json_path = '//*[@ng-click="mode=\'JSON\'"]'
json_element = browser.find_elements_by_xpath(json_path)
json_element_number = len(record_element)
print ("json number", json_element_number)

avoid_dead_loop_counter = 100
index = 0

# loop to expand all json area
while json_element_number > 0 and avoid_dead_loop_counter > 0:

    print(index)

    #Get test case path information from expand json data
    json_element[index].click()

    # Re-define link element
    record_element = browser.find_elements_by_xpath(records_path)
    json_element = browser.find_elements_by_xpath(json_path)

    index = index + 1
    json_element_number = json_element_number - 1

    avoid_dead_loop_counter = avoid_dead_loop_counter - 1
    # end of while record_element_number > 0 and avoid_dead_loop_counter > 0:


#define link element
record_element = browser.find_elements_by_xpath(records_path)
record_element_number = len(record_element)

json_value_path = '//*[@class="ace_content"]'
json_value_element = browser.find_elements_by_xpath(json_value_path)
json_value_element_number = len(json_value_element)
print ("json number", json_value_element_number)

avoid_dead_loop_counter = 100
index = 0

# loop all json value text area.
while json_value_element_number > 0 and avoid_dead_loop_counter > 0:

    print ("***********index*************8")
    print(index)

    #json_information_text = repr(json_value_element[index].text)
    json_information_text = json_value_element[index].text
    print ("***********json_information_text*************8")
    print(json_information_text)

    if json_information_text:
        #n = re.search(r'"agentHost".*}', json_information_text, re.M | re.I | re.S)
        #print ("***********n.group() from format json*************8")
        #print (n.group())
        #format_json = "{" + format(n.group()) + "}"

        data = json.loads(json_information_text)
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
            insert_field = '"testCustomedField": "test",\\n    '
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

            #response = requests.post(url, data=m, auth=('api', 'index'))
            #response = requests.post(url, data=json_source,  auth=HTTPDigestAuth(raw_input("api"), raw_input("index")), verify=True)
            response = requests.post(url, data=json_source, auth=('api', 'index'), verify=False)
            print ("***********post response*************8")
            print (response)

            break
        else:
            print "Continue"
    else:
        print "Continue"

    # Re-define link element
    record_element = browser.find_elements_by_xpath(records_path)
    json_element = browser.find_elements_by_xpath(json_path)

    index = index + 1
    json_value_element_number = json_value_element_number - 1

    avoid_dead_loop_counter = avoid_dead_loop_counter - 1
    # end of while record_element_number > 0 and avoid_dead_loop_counter > 0:














