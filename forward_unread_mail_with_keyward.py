import My_Selenium_Library

from selenium import webdriver

#Define keyword
keyword = "urgent" #use lower case inorder to match insentive for text.

#Define target mail address
target_mail = "chongzhengzhang@gmail.com"

#Define added message body
message_body = "Please help me check this urgent mail, I am not available at this moment.\nThank you very much!\n"

print("Message body is: %s" % message_body)

# Set testing url
url = "https://www.google.com.au"

# Open URL with specified web browser.
browser = webdriver.Chrome()
browser.get(url)

#Forward unread mail with this keyword to the target mail.
My_Selenium_Library.Forward_Unread_Mails_With_Keyword(browser, keyword, target_mail, message_body)