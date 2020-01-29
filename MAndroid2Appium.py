from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#Get Parameters calling this python script
# management_ip = sys.argv[1]
# print ("***********management_ip*************")
# print(management_ip)
#

# Define basic information on MCloud.
mcloud_rest_api_base = "http://mcloud.matrium.com.au:7100/api/v1"
mcloud_login_user_email = "Peter.Zhang@matrium.com.au"
mcloud_token = "fc22b08ce00468fa56cc53a22384012e16d1ac9ab12403abeaaa5e14496239e"


class MAndroid2Appium(object):

    def __init__(self, desired_caps):
        self.platformName = desired_caps.platformName
        self.platformVersion = desired_caps.platformVersion
        self.deviceName = desired_caps.deviceName
        self.udid = desired_caps.udid
        self.appPackage = desired_caps.appPackage
        self.appActivity = desired_caps.appActivity

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = self.platformName
        desired_caps['platformVersion'] = self.platformVersion
        desired_caps['deviceName'] = self.deviceName
        desired_caps['udid'] = self.udid
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.wait = WebDriverWait(self.driver, 10)