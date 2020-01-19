import os
import unittest
from appium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException


def isElement(self, identifyBy, identity):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    sleep(1)
    flag=None
    try:
        if identifyBy == "id":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_id(identity)
        elif identifyBy == "xpath":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath(identity)
        elif identifyBy == "class":
            self.driver.find_element_by_class_name(identity)
        elif identifyBy == "link text":
            self.driver.find_element_by_link_text(identity)
        elif identifyBy == "partial link text":
            self.driver.find_element_by_partial_link_text(identity)
        elif identifyBy == "name":
            self.driver.find_element_by_name(identity)
        elif identifyBy == "tag name":
            self.driver.find_element_by_tag_name(identity)
        elif identifyBy == "css selector":
            self.driver.find_element_by_css_selector(identity)
        flag = True
    except NoSuchElementException as e:
        flag = False
    finally:
        return flag

def setUp(self, platformName, platformVersion, deviceName, appPackage, appActivity):
    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity

    self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

def tearDown(self):
    self.driver.quit()






