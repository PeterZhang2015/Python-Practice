import os
import subprocess
import sys
import unittest

# import pytest

import appiumLibrary

from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from MCloud import MCloudControl

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestMAndroid2TestCases():
    platformName = 'Android'
    deviceName = 'SAMSUNG'
    appPackage = 'com.matrium.mandroid2'
    appActivity = '.MainActivity'
    handset_id = 'ce071607a2e74a1a05'

    @classmethod
    def setup_class(self):
        mcloud = MCloudControl()
        #handset_id = mcloud.connectToMcloudUser(testIMSI)
        handset_id = self.handset_id
        print (handset_id)
        desired_caps = self.getDesiredCaps(self, handset_id)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    @classmethod
    def teardown_class(self):
        mcloud = MCloudControl()

        mcloud.tearDownUsingDevices(mcloud.deviceSerialList)

    def getDesiredCaps(self, handset_id):
        desired_caps = {}
        desired_caps['platformName'] = self.platformName

        # ADB connect to the device on mCloud.
        process = subprocess.Popen(['adb', '-s', handset_id, "shell", "getprop", "ro.build.version.release"],
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        platformVersion = process.stdout.read().strip()
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = self.deviceName
        desired_caps['udid'] = handset_id
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity

        print (desired_caps)

        return desired_caps




    def test_MAndroid2_Relogin(self):

        # Confirm the five permission for MAndroid2.
        permissionAllowButtonId = "com.android.packageinstaller:id/permission_allow_button"
        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the first permission")
            sys.exit("Cannot find the first permission")

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the second permission")
            sys.exit("Cannot find the second permission")

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the third permission")
            sys.exit("Cannot find the third permission")

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the fourth permission")
            sys.exit("Cannot find the fourth permission")

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the fifth permission")
            sys.exit("Cannot find the fifth permission")

        sleep(2)

        logoutButtonId = "com.matrium.mandroid2:id/userLogout"
        self.wait.until(presence_of_element_located((By.ID, logoutButtonId)))

        # Logout.
        logOut = self.driver.find_element_by_id(logoutButtonId)
        if (appiumLibrary.isElement(self, "id", logoutButtonId)):
            self.driver.find_element_by_id(logoutButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the logout button.")
            sys.exit("Cannot find the logout button.")

        # sleep(2)

        loginButtonId = "com.matrium.mandroid2:id/loginButton"
        self.wait.until(presence_of_element_located((By.ID, loginButtonId)))

        if (appiumLibrary.isElement(self, "id", loginButtonId)):
            print("LogOut successfully!")
        else:
            print("Failed to logOut!")
            sys.exit("Failed to logOut!")

        # Login.
        loginMail = "peter.zhang@matrium.com.au"
        loginPassword = "matrium123"

        emailTextId = "com.matrium.mandroid2:id/textEmail"
        if (appiumLibrary.isElement(self, "id", emailTextId)):
            self.driver.find_element_by_id(emailTextId).send_keys(loginMail)
        # sleep(2)
        else:
            print("Cannot find the email text input.")
            sys.exit("Cannot find the email text input.")

        passwordTextId = "com.matrium.mandroid2:id/textPwd"
        if (appiumLibrary.isElement(self, "id", passwordTextId)):
            self.driver.find_element_by_id(passwordTextId).send_keys(loginPassword)
        # sleep(2)
        else:
            print("Cannot find the password text input.")
            sys.exit("Cannot find the password text input.")

        if (appiumLibrary.isElement(self, "id", loginButtonId)):
            self.driver.find_element_by_id(loginButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the login button.")
            sys.exit("Cannot find the login button.")

        self.wait.until(presence_of_element_located((By.ID, logoutButtonId)))

        # Check login successfully.
        if (appiumLibrary.isElement(self, "id", logoutButtonId)):
            print("Login successfully!")
        else:
            print("Failed to login!")
            sys.exit("Failed to login!")

    def test_MAndroid2_logout(self):

        # Confirm the five permission for MAndroid2.
        permissionAllowButtonId = "com.android.packageinstaller:id/permission_allow_button"
        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the first permission")
            sys.exit("Cannot find the first permission")


        logoutButtonId = "com.matrium.mandroid2:id/userLogout"
        self.wait.until(presence_of_element_located((By.ID, logoutButtonId)))

        # Logout.
        logOut = self.driver.find_element_by_id(logoutButtonId)
        if (appiumLibrary.isElement(self, "id", logoutButtonId)):
            self.driver.find_element_by_id(logoutButtonId).click()
        # sleep(2)
        else:
            print("Cannot find the logout button.")
            sys.exit("Cannot find the logout button.")

        # sleep(2)

if __name__ == '__main__':
    # pytest.main('-q test_MAndroid2TestCases.py')

    #pytest.main(["-v","test_MAndroid2TestCases.py",'--alluredir','result'])

    # pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_MAndroid2TestCases.py'])

    #Generate json report
    executeCommand = "pytest -s -q --alluredir report/result test_MAndroid2TestCases.py"
    output1 = os.system(executeCommand)
    print ("Generate json report command response", output1)

    # Change to report path.
    reportPath = "C:\\Work\\Projects\\Python-Practice\\report"
    output2 = os.chdir(reportPath)
    print("Change to report path command response", output2)
    print(os.getcwd())

    # Change json format to html format.
    changeToHtmlCommand = "allure generate ./result/ -o ./report/html --clean"
    output3 = os.system(changeToHtmlCommand)
    print("Change json format to html format command response", output3)

