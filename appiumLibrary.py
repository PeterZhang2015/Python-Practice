import os
import unittest
from appium import webdriver
from time import sleep


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






