from selenium import webdriver

import time
import sys
import Selenium2Library
import json, ast
import re

#Set testing url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


output_file_name = "json_data.txt"
file = open(output_file_name, "r")
json_information_text = file.read()

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



