import My_Selenium_Library

from selenium import webdriver

#Define keyword
keyword = "Urgent"

#Define target mail address
target_mail = "chongzhengzhang@gmail.com"

# Set testing url
url = "https://www.google.com.au"

# Open URL with specified web browser.
browser = webdriver.Chrome()
browser.get(url)

#Forward unread mail with this keyword to the target mail.
My_Selenium_Library.Forward_Unread_Mails_With_Keyword(browser, keyword, target_mail)