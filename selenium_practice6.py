import time
import sys

import My_Selenium_Library

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select


#Set testing url
url = "https://www.google.com.au"

#Open URL with specified web browser.
browser = webdriver.Chrome()
browser.get(url)

#define select text
element = browser.find_elements_by_link_text("Gmail")

element_len = len(element)

if element_len > 0:
    # Click to Gmail link
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


keyword = "urgent"

#Please note  that translate attribute fuctions can be used for case insensitive text match.
#Importance of using "" in xpath.
#unread_mail_with_keyword_elements_xpath = '//*[@class="zA zE"]//*[@role="link"]//*[contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "%s")]' % keyword
#unread_mail_with_keyword_elements = browser.find_elements_by_xpath(unread_mail_with_keyword_elements_xpath)


base_xpath = '//*[@class="zA zE"]//*[@role="link"]//'
text = "urgent"

unread_mail_with_keyword_elements_xpath = "%s%s" % (base_xpath, text)

unread_mail_with_keyword_elements = My_Selenium_Library.Find_Elements_By_Case_Insensitive_Text(browser, base_xpath, text)
unread_mail_with_keyword_number = len(unread_mail_with_keyword_elements)
print("There are %s unread email with keyword %s" % (unread_mail_with_keyword_number,keyword))


dropdown_menu_xpath = '//*[@aria-label="More"]'



inbox_xpath = '//*[contains(@aria-label,"Inbox") and contains(@aria-label,"unread")]'

avoid_dead_loop_counter = 100

# loop all unread mail and reply only for target mail sender.
while unread_mail_with_keyword_number > 0 and avoid_dead_loop_counter > 0:

    print("Find an unread Email with %s keyword." % keyword)

    #Get the first found element.
    unread_mail_element_with_keyword = unread_mail_with_keyword_elements[0]
    unread_mail_element_with_keyword.click()

    time.sleep(2)

    #Forword the mail to another user.
    drop_down_menu = browser.find_element_by_xpath(dropdown_menu_xpath)
    drop_down_menu.click()

    forward_xpath = '//*[text()="Forward"]'
    forward_element = browser.find_element_by_xpath(forward_xpath)
    forward_element.click()

    time.sleep(2)

    #Fill the forwarded target mail address.
    forward_target_mail = "chongzhengzhang@gmail.com"
    forward_target_mail_element = browser.switch_to.active_element
    forward_target_mail_element.click()
    forward_target_mail_element.send_keys(forward_target_mail)

    time.sleep(2) #Importace for the sleeping time between some operations, especially for actions after the focus transfer

    #Fill the forwarded mail body.
    message_body = "Please help me check this urgent mail, I am not available at this moment. Thank you very much."
    # Perform two "Tab" key in order to focus on message body element.
    forward_target_mail_element.send_keys(Keys.TAB)
    time.sleep(1)

    current_foucus = browser.switch_to.active_element
    current_foucus.send_keys(Keys.TAB)

    time.sleep(1)
    message_body_element = browser.switch_to.active_element
    message_body_element.send_keys(message_body)

    #Forward button
    send_button_xpath = '//*[text()="Send"]'
    send_button_element = browser.find_element_by_xpath(send_button_xpath)
    send_button_element.click()
    print("Have forwarded an urgent unread mail to %s automatically." % forward_target_mail)

    #It is import to set waiting time when the webpage changes by some actions.
    time.sleep(5)

    #click inbox
    inbox_unread_elements = browser.find_elements_by_xpath(inbox_xpath)
    inbox_unread_number = len(inbox_unread_elements)
    if inbox_unread_number == 0:
        inbox_xpath = '//*[@title="Inbox"]'
        inbox_unread_element = browser.find_element_by_xpath(inbox_xpath)
    else:
        inbox_unread_element = inbox_unread_elements[0]

    inbox_unread_element.click()

    time.sleep(2)

    #Re-find the remaining unread mail.
    unread_mail_with_keyword_elements = My_Selenium_Library.Find_Elements_By_Case_Insensitive_Text(browser, base_xpath, text)

    unread_mail_with_keyword_number = len(unread_mail_with_keyword_elements)
    #if unread_mail_with_keyword_number == 0:
     #   inbox_xpath = '//*[@title="Inbox"]'

    if unread_mail_with_keyword_number == 0:
        print("It has forwarded all unread mail with keyword %s to %s" % (keyword, forward_target_mail))

    time.sleep(5)

    avoid_dead_loop_counter = avoid_dead_loop_counter - 1
    #end of while unread_mail_number > 0 and avoid_dead_loop_counter > 0:.

#end of test case.

























