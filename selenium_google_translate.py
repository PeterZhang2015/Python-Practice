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


dest_language='French'
# Set destination language.
dest_language_menu_path = "//*[@id='gt-tl-gms'][@role='listbox']"
dest_language_menu_element = browser.find_element_by_xpath(dest_language_menu_path)
dest_language_menu_element.send_keys(dest_language)
time.sleep(2)


# Find the src language text area element.
src_text_path = '//textarea[@id="source"]'
src_text_element = browser.find_element_by_xpath(src_text_path)
src_text_element.send_keys(language_for_translating)

time.sleep(2)





# Get translated language.
#dest_text_path = '//*[@id="gt-res-dir-ctr"]'
#dest_text_element = browser.find_element_by_xpath(dest_text_path)
#dest_text=dest_text_element.text

# Get source language.
#src_language_path = '//*[contains(text(), "- detected")][@role="button"]'
#src_language_element = browser.find_element_by_xpath(src_language_path)
#src_language_detected=src_language_element.text

#src_language = re.search(r'(.*)( - detected)', src_language_detected).group(1)


#print src_language