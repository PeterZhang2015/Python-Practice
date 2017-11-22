import My_Selenium_Library

from selenium import webdriver

#Define the sending mail information
mail_account = "PythonPracticeMail@gmail.com"
mail_password = "woshinibaba"

mail_sender = "zhangchongzheng@gmail.com"
reply_content = "Simple mail test"

#Define web browser.
browser = webdriver.Chrome()

#Login Gmail
My_Selenium_Library.Login_Gmail_Box(browser, mail_account, mail_password)

#Reply unread gmail
My_Selenium_Library.Reply_Unread_Mail(browser, mail_sender, reply_content)

#End of the test case.




