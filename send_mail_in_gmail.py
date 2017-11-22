import My_Selenium_Library

from selenium import webdriver

#Define the sending mail information
mail_account = "PythonPracticeMail@gmail.com"
mail_password = "woshinibaba"

mail_to = "zhangchongzheng@gmail.com"
mail_subject = "Test from python practice"
mail_content = "Simple mail test"

#Define web browser.
browser = webdriver.Chrome()

#Login Gmail
My_Selenium_Library.Login_Gmail_Box(browser, mail_account, mail_password)

#Send Gmail
My_Selenium_Library.Send_Mail(browser, mail_to, mail_subject, mail_content)


#End of the test case.




