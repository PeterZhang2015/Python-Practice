import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


#Set testing url
url = "https://www.google.com.au"

#Open URL with specified web browser.
browser = webdriver.Chrome()
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

#Define mail address information.
loginMail = "PythonPracticeMail@gmail.com"

#username_element.click()
email_address_element.send_keys(loginMail)


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

#Define login password.
password_content = "woshinibaba"

password_element.send_keys(password_content)

#set next button xpath
next_button_xpath = '//span[text()="Next"]'
next_button_element = browser.find_element_by_xpath(next_button_xpath)

#Go to the next linked page.
next_button_element.click()


#Needs to sleep sometime after web page transfer
time.sleep(6)

#Start to make a new mail.
new_mail_button_xpath = '//div[text()="COMPOSE"]'

new_mail_button_element = browser.find_element_by_xpath(new_mail_button_xpath)

#Click new mail button.
new_mail_button_element.click()


#set next button xpath
to_text_xpath = '//*[@aria-label="To"]'
subject_text_xpath = '//*[@aria-label="Subject"]'
#message_body_text_xpath = '//*[@aria-label="Message Body"]'
#message_body_text_xpath = '//*[@class="Ar Au"]'


#define mail content
to_content = "zhangchongzheng@gmail.com"
subject_content = "Test from python practice"
message_body_content = "Simple mail test"


#Find web element by related Xpath.
to_text_element = browser.find_element_by_xpath(to_text_xpath)
subject_text_element = browser.find_element_by_xpath(subject_text_xpath)
#message_body_text_element = browser.find_element_by_xpath(message_body_text_xpath)
#message_body_text_element = browser.findElement(By.xpath("//iframe[@class='Am Al editable']"))


#Fill content to related web element.
to_text_element.send_keys(to_content)
subject_text_element.send_keys(subject_content)



#Perform a "Tab" key in order to focus on message body element.
subject_text_element.send_keys(Keys.TAB)
time.sleep(2)

message_body_element=browser.switch_to.active_element
message_body_element.send_keys(message_body_content)

time.sleep(10)

#Set send button xpath.
send_button_xpath = '//div[text()="Send"]'

#Find send button.
send_button_element = browser.find_element_by_xpath(send_button_xpath)

#Click send button to send the email.
send_button_element.click()


#end of test case.

























