import os
import unittest
from appium import webdriver
from time import sleep
 
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
 
class MAndroid2Tests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Galaxy S7'
        desired_caps['udid'] = 'ce071607a2e74a1a05'
        desired_caps['appPackage'] = 'com.matrium.mandroid2'
        desired_caps['appActivity'] = '.MainActivity'
 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_relogin(self):

        # Confirm the five permission for MAndroid2.
        el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button");
        el.click()
        sleep(2)
        e2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button");
        e2.click()
        sleep(2)
        e3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button");
        e3.click()
        sleep(2)
        e4 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button");
        e4.click()
        sleep(2)
        e5 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button");
        e5.click()
        sleep(2)

        # Logout.
        logOut = self.driver.find_element_by_id("com.matrium.mandroid2:id/userLogout");
        logOut.click()

        sleep(2)

        # Login.
        email = self.driver.find_element_by_id("com.matrium.mandroid2:id/textEmail");
        email.send_keys("peter.zhang@matrium.com.au");
        sleep(2)
        password = self.driver.find_element_by_id("com.matrium.mandroid2:id/textPwd");
        password.send_keys("matrium123");
        sleep(2)

        logIn = self.driver.find_element_by_id("com.matrium.mandroid2:id/loginButton");
        logIn.click()
        sleep(10)
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MAndroid2Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
