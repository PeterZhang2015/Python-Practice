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
import sys



#Get Parameters calling this python script
insert_field = sys.argv[1]
print ("***********insert_field*************")
print(insert_field)

target_test_case_name = sys.argv[2]
print ("***********target_test_case_name*************")
print(target_test_case_name)

recent_records_number = int(sys.argv[3])
print ("***********recent_records_number*************")
print(recent_records_number)

ite_ip_address = str(sys.argv[4])
print ("***********ite_ip_address*************")
print(ite_ip_address)

ite_username = str(sys.argv[5])
print ("***********ite_username*************")
print(ite_username)

ite_password = str(sys.argv[6])
print ("***********ite_password*************")
print(ite_password)

chromedriver_path = str(sys.argv[7])
print ("***********chromedriver_path*************")
print(chromedriver_path)

#Set variables
kibana_url = "https://{}:{}@{}:5601".format(ite_username, ite_password, ite_ip_address)

#Set functions
#Function of open web url with max browser window.
def OpenWebUrlWithMaxWindow(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chromedriver_path, chrome_options=options)
    browser.get(url)
    return browser


#Function of expand some records on Kibana.
def ExpandRecentRecordsOnKibana(browser, elements, elements_xpath, recent_records_number):
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
        elements_number = elements_number - 1
        recent_records_number = recent_records_number - 1
        # end of while elements_number > 0 and recent_records_number > 0:

#Function of expand some records on Kibana.
def ExpandRecentJsonOnKibanaRecords(browser, elements, elements_xpath, recent_records_number):

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

#Function of POST customized data to the recent record with the same test path name on Kibana.
def PostCustomizedDataToLatestRecord(browser, elements, elements_xpath, recent_records_number, target_test_case_name, insert_field):

    elements_number = len(elements)
    print ("json value number", elements_number)

    index = 0

    # loop all json value text area.
    while elements_number > 0 and recent_records_number > 0:

        print ("***********index*************")
        print(index)

        # json_information_text = repr(json_value_element[index].text)
        json_information_text = elements[index].text
        print ("***********json_information_text*************")
        print(json_information_text)
        time.sleep(2)

        if json_information_text:
            json_information_text = json_information_text.replace('\r\n', '')
            json_information_text = json_information_text.replace('\\n', '')
            json_information_text = json_information_text.replace('\n', '')
            data = json.loads(json_information_text)
            test_case_name = data["_source"]["testPath"]
            print ("***********test case name from format json*************")
            print (test_case_name)

            data_index = data["_index"]
            print ("***********index from format json*************")
            print (data_index)

            type = data["_type"]
            print ("***********type from format json*************")
            print (type)

            id = data["_id"]
            print ("***********test id from format json*************")
            print (id)

            if (test_case_name == target_test_case_name):
                print ("Found testing case name:", test_case_name)

                m = re.sub(r'(.*)("agentId":)', r'\1{}\2'.format(insert_field), json_information_text)
                print ("***********POST body*************")
                print (m)

                temp_data = json.loads(m)
                json_source = temp_data["_source"]
                json_source = json.dumps(json_source)

                print ("***********json_source*************")
                print (json_source)

                url = 'https://{}:9200/{}/{}/{}'.format(ite_ip_address, data_index, type, id)
                print ("***********post URL*************")
                print (url)

                username = "api"
                password = "index"

                # response = requests.post(url, data=m, auth=('api', 'index'))
                # response = requests.post(url, data=json_source,  auth=HTTPDigestAuth(raw_input("api"), raw_input("index")), verify=True)
                response = requests.post(url, data=json_source, auth=(username, password), verify=False)
                print ("***********post response*************")
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

#################Main test logical#################################.
def main():
    #Open URL with specified web browser.
    browser = OpenWebUrlWithMaxWindow(kibana_url)
    time.sleep(12)

    #Find the record elements according to attribute.
    records_path ='//*[@data-test-subj="docTableExpandToggleColumn"]'
    record_elements = browser.find_elements_by_xpath(records_path)
    #Expand some recent records on Kibana.
    ExpandRecentRecordsOnKibana(browser, record_elements, records_path, recent_records_number)

    #Find the json elements according to attribute.
    json_path = '//*[@ng-click="mode=\'JSON\'"]'
    json_elements = browser.find_elements_by_xpath(json_path)
    #Expand some recent Json on Kibana records.
    ExpandRecentJsonOnKibanaRecords(browser, json_elements, json_path, recent_records_number)

    #Find the json elements according to attribute.
    json_value_path = '//*[@class="ace_content"]'
    json_text_elements = browser.find_elements_by_xpath(json_value_path)

    #Post customized data to recent Kibana record with the same test path name.
    #output_file_name = "output_response.txt"
    #file = open(output_file_name, "r")
    #insert_field = file.read()
    insert_field = sys.argv[1]
    #insert_field = '"testCustomedField": {},\\n    '.format(testCustomizedField)
    PostCustomizedDataToLatestRecord(browser, json_text_elements, json_value_path, recent_records_number, target_test_case_name, insert_field)

#Call main function.
if __name__ == "__main__":
    main()














