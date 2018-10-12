# -*- coding: utf-8 -*-
from selenium import webdriver

import time
import re
import sys


google_translate_url = "https://translate.google.com.au"
language_for_translating = u"我来自中国"

# Open URL with specified web browser.
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
browser.get(google_translate_url)
time.sleep(5)

# Find the src language text area element.
src_language_path = '//textarea[@id="source"]'
src_language_element = browser.find_element_by_xpath(src_language_path)
src_language_element.send_keys(language_for_translating)

time.sleep(2)

# Get translated languate.
dest_language_path = '//*[@id="gt-res-dir-ctr"]'
dest_language_element = browser.find_element_by_xpath(dest_language_path)
dest_language=dest_language_element.text

print dest_language