import os
import subprocess
import sys

# from ..library.MAndroid2BaseYaml import getYam
# from ..library.MAndroid2BaseMCloud import MCloudControl
from datetime import datetime
from os import listdir
from time import sleep

import pytest

from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl
from MAndroid2SmokeTest.library.MAndroid2BaseCommon import connectToTestUsers, addJsonReportMetaData, executeTestLogic, \
    verifyTestCaseResult
from MAndroid2SmokeTest.library.MAndroid2BaseCommon import disconnectTestUsers
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getAllConfigureInfo
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getConfigureInfo

from MAndroid2SmokeTest.library.MAndroid2BaseAPI import placeBasicVoiceCall
from MAndroid2SmokeTest.library.MAndroid2BaseAPI import receiveBasicVoiceCall
from MAndroid2SmokeTest.library.MAndroid2BaseAPI import endBasicVoiceCall

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

RELPATH = lambda p: os.path.relpath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestMAndroid2TestCases():
    # Initialize variables.
    testEnvironmentPath = "../configuration/testEnvironment/"
    testEnvironmentName = "testEnvironment"
    testUserPath = "../configuration/testUsers/"
    testUserName = "testUsers"
    testParametersPath = "../configuration/testParameters/voiceCall/"
    testParametersName = "testParameters"


    testEnvironment = getAllConfigureInfo(testEnvironmentPath, testEnvironmentName)
    testUsers = getAllConfigureInfo(testUserPath, testUserName)
    testParameters = getAllConfigureInfo(testParametersPath, testParametersName)

    @pytest.mark.parametrize("testEnvironment", testEnvironment)
    @pytest.mark.parametrize("testUsers", testUsers)
    @pytest.mark.parametrize("testParameters", testParameters)
    def test_MAndroid2_VoiceCall(self, json_metadata, testEnvironment, testUsers, testParameters):
        # Initialization
        self.testEnvironment = testEnvironment
        self.testUsers = testUsers
        self.testParameters = testParameters
        self.responseList = []
        self.testResults = []
        testCaseKey = 'VoiceCall'
        testCaseInfoFileName = "../configuration/testCaseInfo/testCaseInfo.yaml"
        testCaseInfoName = "VoiceCallTestCaseInfo"

        # Read test case info.
        self.testCaseInfo = getConfigureInfo(testCaseInfoFileName, testCaseInfoName)

        # Checking Test parameters.
        self.checkConfiguration(testEnvironment, testUsers)
        assert ("VoiceCall" in self.testParameters)
        assert ("Duration" in self.testParameters['VoiceCall'])
        print("Voice call duration is {}".format(testParameters['VoiceCall']['Duration']))

        # Connect available test handset on mcloud from specified IMSI.
        mcloud = MCloudControl()

        # Set test environment variables.
        mcloud.mcloudBaseUrl = self.testEnvironment['MCloud']['baseUrl']
        mcloud.mcloudLoginUser = self.testEnvironment['Login']['User']
        mcloud.mcloudLoginToken = self.testEnvironment['Login']['accessToken']

        self.testUsers['MO']['handsetID'] = mcloud.connectToMcloudUser(self.testUsers['MO']['IMSI'])
        print("MO Handset ID is {}".format(self.testUsers['MO']['handsetID']))

        self.testUsers['MT']['handsetID'] = mcloud.connectToMcloudUser(self.testUsers['MT']['IMSI'])
        print("MT Handset ID is {}".format(self.testUsers['MT']['handsetID']))

        # Starting test logic.
        print("Starting voice call test case.")
        self.responseList = executeTestLogic(self.testEnvironment, self.testUsers, self.testCaseInfo, testCaseKey, self.testParameters)

        # Disconnect testing users.
        print("deviceSerialList to be disconnected is {}".format(mcloud.deviceSerialList))
        mcloud.tearDownUsingDevices(mcloud.deviceSerialList)

        # Verify test result.
        self.testResults = verifyTestCaseResult(self.testCaseInfo, testCaseKey, self.responseList)

        # Adding information to json report.
        addJsonReportMetaData(json_metadata, self.testEnvironment, self.testUsers, self.testParameters, self.testCaseInfo, self.testResults)

        # Assert test result.
        for result in self.testResults:
            assert (result['checkPointResult'] == "passed")


    def test_example(self):
        print ("***************************test Example************************************")

    def checkConfiguration(self, testEnvironment, testUsers):
        # Check test environment information from configuration file.
        assert ("MCloud" in testEnvironment)
        assert ("baseUrl" in testEnvironment['MCloud'])
        assert ("Login" in testEnvironment)
        assert ("User" in testEnvironment['Login'])
        assert ("accessToken" in testEnvironment['Login'])
        assert ("MAndroid2AgentPath" in testEnvironment)

        # Check test users information from configuration file.
        assert ("MO" in testUsers)
        assert ("IMSI" in testUsers['MO'])
        assert ("MSISDN" in testUsers['MO'])

        assert ("MT" in testUsers)
        assert ("IMSI" in testUsers['MT'])
        assert ("MSISDN" in testUsers['MT'])







if __name__ == '__main__':
    # Generate timestamp.
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%S.%f")

    # Construct report parameters.
    reportPath = RELPATH("../reports")
    htmlReport = "--html={}/html/htmlReport_{}.html".format(reportPath, timestampStr)
    jsonReport = "--json-report --json-report-file {}/json/jsonReport_{}.json".format(reportPath, timestampStr)
    print(jsonReport)

    # Execute test case.
    generateReportCommand = "pytest -q -r test_MAndroid2TestCases.py {} {}".format(jsonReport, htmlReport)
    print(generateReportCommand)
    output3 = os.system(generateReportCommand)

    # Execute test cases and generate reports. Not sure why it is not working for json report.
    # pytest.main(["-q", "-r", "test_MAndroid2TestCases.py", jsonReport, htmlReport])
    # pytest.main(["-q", "-r", "test_MAndroid2TestCases.py", jsonReport])

    # pytest.main(["-v","test_MAndroid2TestCases.py",'--alluredir','result'])

    # pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_MAndroid2TestCases.py'])

    # #Generate json report
    # executeCommand = "pytest -s -q --alluredir report/result test_MAndroid2TestCases.py"
    # output1 = os.system(executeCommand)
    # print ("Generate json report command response", output1)
    #
    # # Change to report path.
    # reportPath = "C:\\Work\\Projects\\Python-Practice\\report"
    # output2 = os.chdir(reportPath)
    # print("Change to report path command response", output2)
    # print(os.getcwd())
    #
    # # Change json format to html format.
    # changeToHtmlCommand = "allure generate ./result/ -o ./report/html --clean"
    # output3 = os.system(changeToHtmlCommand)
    # print("Change json format to html format command response", output3)
