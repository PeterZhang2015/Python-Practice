from selenium import webdriver

import time

import urllib2
import re


#Set variables
usr = "api"
pwd = "index"

elasticsearch_url = "https://{}:{}@192.168.32.75:9200/_cat/indices?v".format(usr, pwd)

#Open URL with specified web browser.
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get(elasticsearch_url)

time.sleep(5)

#Get all report indexes
elasticSearch_index_list = browser.page_source

#print elasticSearch_index_list

#sorted_index = re.sub(r'(.*)(report-v700-)', r'\1{}\2'.format(insert_field), json_information_text)
regExpressionToGetAllReportIndexes = "^report-v700-.+$"
#sorted_index = re.sub(regExpressionToGetAllReportIndexes)
sorted_index = re.findall('report-v700-[^ ]+', elasticSearch_index_list)
print sorted_index
