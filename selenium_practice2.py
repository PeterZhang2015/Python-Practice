import time

from selenium import webdriver


#Set testing url
url = "https://www.google.com.au"

#Open URL with specified web browser.
browser = webdriver.Firefox()
browser.get(url)

#define select text
element = browser.find_elements_by_link_text("Gmail")

#Click to Gmail link
element[0].click()

#Fill in username.
#set Email address xpath
#xpath = '//*[@id="identifierId"]'
email_address_xpath = '//*[@aria-label="Email or phone"]'
email_address_element = browser.find_element_by_xpath(email_address_xpath)

#username_element.click()
email_address_element.send_keys("test@gmail.com.au")


#set next button xpath
next_button_xpath = '//span[text()="Next"]'
next_button_element = browser.find_element_by_xpath(next_button_xpath)

#Go to the next linked page.
next_button_element.click()

#Needs to sleep sometime after web page transfer
time.sleep(2)

#Fill in password.
password_xpath = '//*[@aria-label="Enter your password"]'

password_element = browser.find_element_by_xpath(password_xpath)

password_content = "1234567"
password_element.send_keys(password_content)

#set next button xpath
next_button_xpath = '//span[text()="Next"]'
next_button_element = browser.find_element_by_xpath(next_button_xpath)

#Go to the next linked page.
next_button_element.click()














