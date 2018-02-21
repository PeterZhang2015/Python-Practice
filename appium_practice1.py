"""
Simple iOS tests for change region settings in iOS simulator.
NOTE: This is throwaway code to help testers get started with iOS automation
"""
import unittest
import os
from appium import webdriver
from time import sleep


class iosSettingTest(unittest.TestCase):
    def setUp(self):
        # Set up appium
        # app = os.path.join(os.path.dirname(__file__),
        #  'TableSearchwithUISearchController/Swift',
        #                    'Search.swift.app')
        # app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'app': 'settings',
                'platformName': 'iOS',
                'platformVersion': '11.0',
                'deviceName': 'iPhone Simulator',
                'bundleId': 'com.apple.Preferences',

            })

    def test_change_region_setting(self):
        # Getting the following python code by Appium inspector recorder.

        el1 = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"General\"]")
        el1.click()
        el2 = self.driver.find_element_by_xpath("//XCUIElementTypeCell[@name=\"Language & Region\"]")
        el2.click()
        el3 = self.driver.find_element_by_xpath("//XCUIElementTypeCell[@name=\"Region\"]")
        el3.click()
        el4 = self.driver.find_element_by_xpath("(//XCUIElementTypeOther[@name=\"table index\"])[2]")
        el4.click()

        #el5 = self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Australia\"]")
        el5 = self.driver.find_element_by_accessibility_id("American Samoa")
        el5.click()
        el6 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Settings\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable")
        el6.click()
        el7 = self.driver.find_element_by_xpath(
            "//XCUIElementTypeApplication[@name=\"Settings\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable")
        el7.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(iosSettingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)