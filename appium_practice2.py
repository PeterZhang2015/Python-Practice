import os
import unittest
import appiumLibrary

from appium import webdriver
from time import sleep
 
# Returns abs path relative to this file and not cwd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
 
class MAndroid2Tests(unittest.TestCase):
    # def __init__(self, platformName, platformVersion, deviceName, udid, appPackage, appActivity):
    #     self.platformName = platformName
    #     self.platformVersion = platformVersion
    #     self.deviceName = deviceName
    #     self.udid = udid
    #     self.appPackage = appPackage
    #     self.appActivity = appActivity

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'SM-G930F'
        desired_caps['udid'] = 'ce071607a2e74a1a05'
        desired_caps['appPackage'] = 'com.matrium.mandroid2'
        desired_caps['appActivity'] = '.MainActivity'
 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.wait = WebDriverWait(self.driver, 10)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_relogin(self):

        # Confirm the five permission for MAndroid2.
        permissionAllowButtonId = "com.android.packageinstaller:id/permission_allow_button"
        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the first permission")
            return

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the second permission")
            return

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the third permission")
            return

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the fourth permission")
            return

        self.wait.until(presence_of_element_located((By.ID, permissionAllowButtonId)))

        if (appiumLibrary.isElement(self, "id", permissionAllowButtonId)):
            self.driver.find_element_by_id(permissionAllowButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the fifth permission")
            return

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
            return

        #sleep(2)

        loginButtonId = "com.matrium.mandroid2:id/loginButton"
        self.wait.until(presence_of_element_located((By.ID, loginButtonId)))

        if (appiumLibrary.isElement(self, "id", loginButtonId)):
            print("LogOut successfully!")
        else:
            print("Failed to logOut!")

        # Login.
        loginMail = "peter.zhang@matrium.com.au"
        loginPassword = "matrium123"

        emailTextId = "com.matrium.mandroid2:id/textEmail"
        if (appiumLibrary.isElement(self, "id", emailTextId)):
            self.driver.find_element_by_id(emailTextId).send_keys(loginMail)
           # sleep(2)
        else:
            print("Cannot find the email text input.")
            return

        passwordTextId = "com.matrium.mandroid2:id/textPwd"
        if (appiumLibrary.isElement(self, "id", passwordTextId)):
            self.driver.find_element_by_id(passwordTextId).send_keys(loginPassword)
           # sleep(2)
        else:
            print("Cannot find the password text input.")
            return

        if (appiumLibrary.isElement(self, "id", loginButtonId)):
            self.driver.find_element_by_id(loginButtonId).click()
           # sleep(2)
        else:
            print("Cannot find the login button.")
            return

        self.wait.until(presence_of_element_located((By.ID, logoutButtonId)))

        # Check login successfully.
        if (appiumLibrary.isElement(self, "id", logoutButtonId)):
            print("Login successfully!")
        else:
            print("Failed to login!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MAndroid2Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
