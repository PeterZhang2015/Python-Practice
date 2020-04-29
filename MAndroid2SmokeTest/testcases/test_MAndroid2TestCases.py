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
from MAndroid2SmokeTest.library.MAndroid2BaseCommon import addJsonReportMetaData, executeTestLogic, \
    verifyTestCaseResult, connectTestUsers, checkTestEnvironmentConfig, checkTestParametersConfig, \
    checkTestCaseInfoConfig, createExcelTestReport, writeExcelTestReportSummary, initializeExcelSummary, \
    writeExcelTestReportDetail
from MAndroid2SmokeTest.library.MAndroid2BaseCommon import disconnectTestUsers
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getAllConfigureInfo
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getConfigureInfo

from MAndroid2SmokeTest.library.MAndroid2BaseAPI import placeBasicVoiceCall, getMAndroid2Version
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
    testParametersPath = "../configuration/testParameters/voiceCall/"
    testParametersName = "testParameters"
    excelReportPath = "../reports/excel/"
    testCaseSummary = {}
    testCaseDetailList = []

    testEnvironment = getAllConfigureInfo(testEnvironmentPath, testEnvironmentName)
    testParameters = getAllConfigureInfo(testParametersPath, testParametersName)

    @classmethod
    def setup_class(cls):
        print("------ Setup before class TestMAndroid2TestCases ------")
        # Check excel report directory exist.
        if (os.path.exists(os.path.abspath(cls.excelReportPath)) == False):
            os.makedirs(cls.excelReportPath)

        # Create excel report and initialize test case summary.
        cls.excelReport, cls.summarySheet, cls.detailSheet = createExcelTestReport(cls.excelReportPath)
        cls.testCaseSummary = initializeExcelSummary(cls.testCaseSummary)

        # Get test case starting date.
        cls.testSuiteStartingTime = datetime.now()
        cls.testCaseSummary['testingDate'] = cls.testSuiteStartingTime.strftime("%d/%b/%Y_%H:%M:%S.%f")


    @classmethod
    def teardown_class(cls):
        print("------ Teardown after class TestMAndroid2TestCases ------")

        # Get test case ending date.
        cls.testSuiteEndTime = datetime.now()
        diff = cls.testSuiteEndTime - cls.testSuiteStartingTime  # the result is a datetime.timedelta object
        cls.testCaseSummary['testDuration'] = "{} s".format(diff.total_seconds())

        # Write excel test report.
        cls.excelReport.summary(cls.summarySheet, cls.testCaseSummary)
        print ("testCaseDetailList is {}".format(cls.testCaseDetailList))
        cls.excelReport.detail(cls.detailSheet, cls.testCaseDetailList)
        cls.excelReport.close()

    @pytest.mark.parametrize("testEnvironment", testEnvironment)
    @pytest.mark.parametrize("testParameters", testParameters)
    def test_MAndroid2_VoiceCall(self, json_metadata, testEnvironment, testParameters):
        # Initialization
        responseList = []
        testResults = []
        testCaseKey = 'VoiceCall'
        testCaseInfoFileName = "../configuration/testCaseInfo/testCaseInfo.yaml"

        # Checking Test parameters.
        checkTestEnvironmentConfig(testEnvironment)
        checkTestParametersConfig(testParameters, testCaseKey)

        # Read test case info.
        testCaseInfo = getConfigureInfo(testCaseInfoFileName, testCaseKey)
        checkTestCaseInfoConfig(testCaseInfo)

        # ConnectTestUsers.
        connectTestUsers(testEnvironment, "MOMT")

        # Starting test logic.
        print("Starting voice call test case.")
        responseList = executeTestLogic(testEnvironment, testCaseInfo, testCaseKey, testParameters)

        # Disconnect testing users.
        disconnectTestUsers()

        # Verify test result.
        testResults = verifyTestCaseResult(testCaseInfo, testCaseKey, responseList)

        # Adding information to json report.
        addJsonReportMetaData(json_metadata, testEnvironment, testParameters, testCaseInfo, testResults)

        # Write test case summary and test case detail.
        self.testCaseSummary = writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        self.testCaseDetailList = writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters, testCaseInfo, testResults)

        # Assert test result.
        for result in testResults:
            assert (result['checkPointResult'] == "passed")


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
