from selenium import webdriver

#Set testing url
url = "http://inventwithpython.com"

#Open URL with specified web browser.
browser = webdriver.Firefox()
browser.get(url)

#Find the element according to CSS name.
css_name = "bookcover"

#Continue the program even if not found the element by specified css name.
try:
    element = browser.find_element_by_class_name(css_name)
    print("Find related element %s by CSS name %s on %s" % (element.tag_name, css_name, url))
except:
    print("Cannot find related element by CSS name %s on %s" % (css_name, url))


#define link element
link_element = browser.find_elements_by_link_text("Read It Online")

#Click the link element
link_element[0].click()



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
#set xpath
xpath = '//*[@id="identifierId"]'


username_element = browser.find_element_by_xpath(xpath)

username_element[0].send_keys("test@gmail.com.au")







