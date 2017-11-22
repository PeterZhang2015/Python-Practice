import time
import sys

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


def Login_Gmail_Box(browser, login_Mail, login_password):

    #Set testing url
    url = "https://www.google.com.au"

    #Open URL with specified web browser.
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

    #username_element.click()
    email_address_element.send_keys(login_Mail)

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
    password_element.send_keys(login_password)

    #set next button xpath
    next_button_xpath = '//span[text()="Next"]'
    next_button_element = browser.find_element_by_xpath(next_button_xpath)

    #Go to the next linked page.
    next_button_element.click()

    #Needs to sleep sometime after web page transfer
    time.sleep(6)


#end of def Login_Gmail_Box(login_Mail, login_password):.

def Send_Mail(browser, mail_to, mail_subject, mail_content):
    # Start to make a new mail.
    new_mail_button_xpath = '//div[text()="COMPOSE"]'

    new_mail_button_element = browser.find_element_by_xpath(new_mail_button_xpath)

    # Click new mail button.
    new_mail_button_element.click()

    # set next button xpath
    to_text_xpath = '//*[@aria-label="To"]'
    subject_text_xpath = '//*[@aria-label="Subject"]'

    # Find web element by related Xpath.
    to_text_element = browser.find_element_by_xpath(to_text_xpath)
    subject_text_element = browser.find_element_by_xpath(subject_text_xpath)

    # Fill content to related web element.
    to_text_element.send_keys(mail_to)
    subject_text_element.send_keys(mail_subject)

    # Perform a "Tab" key in order to focus on message body element.
    subject_text_element.send_keys(Keys.TAB)
    time.sleep(2)

    message_body_element = browser.switch_to.active_element
    message_body_element.send_keys(mail_content)

    time.sleep(10)

    # Set send button xpath.
    send_button_xpath = '//div[text()="Send"]'

    # Find send button.
    send_button_element = browser.find_element_by_xpath(send_button_xpath)

    # Click send button to send the email.
    send_button_element.click()

#end of def Send_Mail(browser, mail_to, mail_subject, mail_content):.


def Reply_Unread_Mail(browser, mail_sender, reply_content):

    #Get the unread mail elements.
    unread_mail_elements_from_target_sender_xpath = '//*[@class="zA zE"]//div[not(contains(text(), "unread"))]/*[@email="%s"]' % mail_sender

    unread_mail_elements = browser.find_elements_by_xpath(unread_mail_elements_from_target_sender_xpath)

    unread_mail_number = len(unread_mail_elements)

    if unread_mail_number == 0:
        print("There is no unread mail from %s now." % mail_sender)

    reply_xpath = '//span[text()="Reply" and @role="link"]'
    send_button_xpath = '//*[text()="Send"]'

    inbox_xpath = '//*[contains(@aria-label,"Inbox") and contains(@aria-label,"unread")]'

    avoid_dead_loop_counter = 100

    # loop all unread mail and reply only for target mail sender.
    while unread_mail_number > 0 and avoid_dead_loop_counter > 0:

        print("Find an unread Email from %s." % mail_sender)

        # Get the first found element.
        unread_mail_element = unread_mail_elements[0]
        unread_mail_element.click()

        # Reply the mail.
        reply_element = browser.find_element_by_xpath(reply_xpath)
        reply_element.click()
        new_reply_element = browser.switch_to.active_element
        new_reply_element.send_keys(reply_content)

        # Send reply
        send_button_element = browser.find_element_by_xpath(send_button_xpath)
        send_button_element.click()
        print("Have replied to Email from %s automatically." % mail_sender)

        # It is import to set waiting time when the webpage changes by some actions.
        time.sleep(5)

        # click inbox
        inbox_unread_elements = browser.find_elements_by_xpath(inbox_xpath)
        inbox_unread_number = len(inbox_unread_elements)
        if inbox_unread_number == 0:
            inbox_xpath = '//*[@title="Inbox"]'
            inbox_unread_element = browser.find_element_by_xpath(inbox_xpath)
        else:
            inbox_unread_element = inbox_unread_elements[0]

        inbox_unread_element.click()

        # Re-find the remaining unread mail.
        unread_mail_elements = browser.find_elements_by_xpath(unread_mail_elements_from_target_sender_xpath)
        unread_mail_number = len(unread_mail_elements)
        if unread_mail_number == 0:
            inbox_xpath = '//*[@title="Inbox"]'

        time.sleep(5)

        avoid_dead_loop_counter = avoid_dead_loop_counter - 1


#end of test case.

























