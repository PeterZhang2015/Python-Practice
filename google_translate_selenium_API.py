# -*- coding: utf-8 -*-
from selenium import webdriver

import time
import re
import sys
import json

import codecs


#Get Parameters calling this python script
#text_for_translating = sys.argv[1]
text_for_translating = codecs.open('translating_text.txt', encoding="utf8").readlines()

#print(text_for_translating)

translating_to_language = sys.argv[1]
#print ("***********Translating to language*************")
#print(translating_to_language)

#################Main test logical#################################.
def main():
    google_translate_url = "https://translate.google.com.au"

    # Open URL with specified web browser.
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(google_translate_url)
    time.sleep(5)

    # Find the src language text area element.
    src_text_path = '//textarea[@id="source"]'
    src_text_element = browser.find_element_by_xpath(src_text_path)
    src_text_element.send_keys(text_for_translating)

    time.sleep(2)

    # Get translated languate.
    dest_text_path = '//*[@id="gt-res-dir-ctr"]'
    dest_text_element = browser.find_element_by_xpath(dest_text_path)
    dest_text=dest_text_element.text

    #print ("***********Translated text*************")
    #print(dest_text)

    # Get source language.
    src_language_path = '//*[contains(text(), "- detected")][@role="button"]'
    src_language_element = browser.find_element_by_xpath(src_language_path)
    src_language_detected = src_language_element.text

    src_language = re.search(r'(.*)( - detected)', src_language_detected).group(1)

    #print ("***********Source Language*************")
    #print(src_language)

    # Set return as a Python object (dict):
    returnVal = {
        "translated_text": dest_text,
        "translating_source_language": src_language
    }

    # convert into JSON:
    returnVal = json.dumps(returnVal)

    print(returnVal)



# Call main function.
if __name__ == "__main__":
    main()