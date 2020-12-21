import os
import subprocess
import sys

# from ..library.MAndroid2BaseYaml import getYam
# from ..library.MAndroid2BaseMCloud import MCloudControl
from datetime import datetime, timedelta
from os import listdir
from time import sleep

import pytest

from pytest_reportportal import RPLogger, RPLogHandler

from distutils.dir_util import copy_tree

from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl
from MAndroid2SmokeTest.library.MAndroid2BaseCommon import addJsonReportMetaData, executeTestLogic, \
    verifyTestCaseResult, connectTestUsers, checkTestEnvironmentConfig, checkTestParametersConfig, \
    checkTestCaseInfoConfig, createExcelTestReport, writeExcelTestReportSummary, initializeExcelSummary, \
    writeExcelTestReportDetail, executeTestCase, getAllAvailableDevicesUnderDifferentEnvironment, checkTestReportConfig
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

@pytest.mark.allAvailableDeviceSmokeTest

class TestMAndroid2TestCases():
    # Initialize variables.
    testEnvironmentPath = "../configuration/testEnvironment/"
    testReportConfigPath = "../configuration/testReportConfig/testReportConfig.yaml"
    voiceCallTestParametersPath = "../configuration/testParameters/voiceCall/testParameters1.yaml"
    smsTestParametersPath = "../configuration/testParameters/SMS/testParameters1.yaml"
    mmsTestParametersPath = "../configuration/testParameters/MMS/testParameters1.yaml"
    webBrowsingTestParametersPath = "../configuration/testParameters/webBrowsing/testParameters1.yaml"
    httpDownloadTestParametersPath = "../configuration/testParameters/httpDownload/testParameters1.yaml"
    testEnvironmentName = "testEnvironment"
    testParametersName = "testParameters"
    testReportConfigName = "testReportConfig"

    testCaseSummary = {}
    testCaseDetailList = []
    voiceCallTestParameters = []
    smsTestParameters = []
    mmsTestParameters = []
    webBrowsingTestParameters = []
    httpDownloadTestParameters = []

    testEnvironments = getAllConfigureInfo(testEnvironmentPath, testEnvironmentName)
    assert (testEnvironments != None)

    reportConfig = checkTestReportConfig(testReportConfigPath, testReportConfigName)

    parameters = getConfigureInfo(voiceCallTestParametersPath, testParametersName)
    assert (parameters != None)
    voiceCallTestParameters.append(parameters)

    parameters = getConfigureInfo(smsTestParametersPath, testParametersName)
    assert (parameters != None)
    smsTestParameters.append(parameters)

    parameters = getConfigureInfo(mmsTestParametersPath, testParametersName)
    assert (parameters != None)
    mmsTestParameters.append(parameters)

    parameters = getConfigureInfo(webBrowsingTestParametersPath, testParametersName)
    assert (parameters != None)
    webBrowsingTestParameters.append(parameters)

    parameters = getConfigureInfo(httpDownloadTestParametersPath, testParametersName)
    assert (parameters != None)
    httpDownloadTestParameters.append(parameters)

    testEnvironmentCombinations = getAllAvailableDevicesUnderDifferentEnvironment(testEnvironments)

    print("testEnvironmentCombinations is: {}".format(testEnvironmentCombinations))

    @classmethod
    def setup_class(cls):
        print("------ Setup before class TestMAndroid2TestCases ------")
        # Check excel report directory exist.
        if (os.path.exists(os.path.abspath(cls.reportConfig["reportPath"]["excelReportPath"])) == False):
            os.makedirs(cls.reportConfig["reportPath"]["excelReportPath"])

        # Create excel report and initialize test case summary.
        cls.excelReport, cls.summarySheet, cls.detailSheet = createExcelTestReport(cls.reportConfig["reportPath"]["excelReportPath"])
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
        formatedDiff = str(timedelta(seconds=diff.seconds))
        cls.testCaseSummary['testDuration'] = "{}".format(formatedDiff)

        # Write excel test report.
        cls.excelReport.summary(cls.summarySheet, cls.testCaseSummary)
        print ("testCaseDetailList is {}".format(cls.testCaseDetailList))
        cls.excelReport.detail(cls.detailSheet, cls.testCaseDetailList)
        cls.excelReport.close()

    # tempList = ["1", "2", "3", "4", "5"]
    # @pytest.mark.parametrize("tempParameter", tempList)
    # def test_MAndroid2_Temp(self, rp_logger, tempParameter):
    #     rp_logger.info("Running temp test case with parameter {}.".format(tempParameter))
    #     print("Running temp test case.")

    # def test_MAndroid2_Temp1(self, rp_logger):
    #     rp_logger.info("Running temp test case1.")
    #     print("Running temp test case.")
    #
    # def test_MAndroid2_Temp2(self, rp_logger):
    #     rp_logger.info("Running temp test case2.")
    #     print("Running temp test case.")
    #
    # def test_MAndroid2_Temp3(self, rp_logger):
    #     rp_logger.info("Running temp test case3.")
    #     print("Running temp test case.")
    #
    # def test_MAndroid2_Temp4(self, rp_logger):
    #     rp_logger.info("Running temp test case4.")
    #     print("Running temp test case.")
    #
    # def test_MAndroid2_Temp5(self, rp_logger):
    #     rp_logger.info("Running temp test case5.")
    #     print("Running temp test case.")

    @pytest.mark.parametrize("testEnvironment", testEnvironmentCombinations)
    @pytest.mark.parametrize("testParameters", voiceCallTestParameters)
    def test_MAndroid2_VoiceCall(self, rp_logger, json_metadata, testEnvironment, testParameters):
        # Define test case variables.
        testCaseKey = 'VoiceCall'
        userFlag = 'MOMT'

        # Get and check test case info.
        testCaseInfo = checkTestCaseInfoConfig(testCaseKey)
        rp_logger.info("Test case info: {}.".format(testCaseInfo))
        rp_logger.info("Test environment: {}.".format(testEnvironment))
        rp_logger.info("Test testParameters: {}.".format(testParameters))

        # Execute test case.
        rp_logger.info("Executing test logic.")
        testResults = executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters,
                                      testCaseInfo, self.testCaseSummary, self.testCaseDetailList)

        # Write test case summary and test case detail.
        writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
                                                             testCaseInfo, testResults)

        # Assert test result.
        rp_logger.info("Test result: {}.".format(testResults))
        for result in testResults:
            assert (result['checkPointResult'] == "passed")

        # Add some time interval for each run. Otherwise if forwarding result to realtime analysis reportportal, it will get interrupted status as test result.
        sleep(5)

    @pytest.mark.parametrize("testEnvironment", testEnvironmentCombinations)
    @pytest.mark.parametrize("testParameters", smsTestParameters)
    def test_MAndroid2_SMS(self, rp_logger, json_metadata, testEnvironment, testParameters):
        # Define test case variables.
        testCaseKey = 'SMS'
        userFlag = 'MOMT'

        # Get and check test case info.
        testCaseInfo = checkTestCaseInfoConfig(testCaseKey)
        rp_logger.info("Test case info: {}.".format(testCaseInfo))
        rp_logger.info("Test environment: {}.".format(testEnvironment))
        rp_logger.info("Test testParameters: {}.".format(testParameters))

        # Execute test case.
        rp_logger.info("Executing test logic.")
        testResults = executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters,
                                      testCaseInfo, self.testCaseSummary, self.testCaseDetailList)

        # Write test case summary and test case detail.
        writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
                                                             testCaseInfo, testResults)

        # Assert test result.
        rp_logger.info("Test result: {}.".format(testResults))
        for result in testResults:
            assert (result['checkPointResult'] == "passed")

        # Add some time interval for each run. Otherwise if forwarding result to realtime analysis reportportal, it will get interrupted status as test result.
        sleep(5)

    @pytest.mark.parametrize("testEnvironment", testEnvironmentCombinations)
    @pytest.mark.parametrize("testParameters", mmsTestParameters)
    def test_MAndroid2_MMS(self, rp_logger, json_metadata, testEnvironment, testParameters):
        # Define test case variables.
        testCaseKey = 'MMS'
        userFlag = 'MOMT'

        # Get and check test case info.
        testCaseInfo = checkTestCaseInfoConfig(testCaseKey)
        rp_logger.info("Test case info: {}.".format(testCaseInfo))
        rp_logger.info("Test environment: {}.".format(testEnvironment))
        rp_logger.info("Test testParameters: {}.".format(testParameters))

        # Execute test case.
        rp_logger.info("Executing test logic.")
        testResults = executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters,
                                      testCaseInfo, self.testCaseSummary, self.testCaseDetailList)

        # Write test case summary and test case detail.
        writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
                                                             testCaseInfo, testResults)

        # Assert test result.
        rp_logger.info("Test result: {}.".format(testResults))
        for result in testResults:
            assert (result['checkPointResult'] == "passed")

        # Add some time interval for each run. Otherwise if forwarding result to realtime analysis reportportal, it will get interrupted status as test result.
        sleep(5)

    @pytest.mark.parametrize("testEnvironment", testEnvironmentCombinations)
    @pytest.mark.parametrize("testParameters", webBrowsingTestParameters)
    def test_MAndroid2_WebBrowsing(self, rp_logger, json_metadata, testEnvironment, testParameters):

        # Define test case variables.
        testCaseKey = 'WebBrowsing'
        userFlag = 'MO'

        # Get and check test case info.
        testCaseInfo = checkTestCaseInfoConfig(testCaseKey)
        rp_logger.info("Test case info: {}.".format(testCaseInfo))
        rp_logger.info("Test environment: {}.".format(testEnvironment))
        rp_logger.info("Test testParameters: {}.".format(testParameters))

        # Execute test case.
        rp_logger.info("Executing test logic.")
        testResults = executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters,
                                      testCaseInfo, self.testCaseSummary, self.testCaseDetailList)

        # Write test case summary and test case detail.
        writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
                                                             testCaseInfo, testResults)

        # Assert test result.
        rp_logger.info("Test result: {}.".format(testResults))
        for result in testResults:
            assert (result['checkPointResult'] == "passed")

        # Add some time interval for each run. Otherwise if forwarding result to realtime analysis reportportal, it will get interrupted status as test result.
        sleep(5)

    @pytest.mark.parametrize("testEnvironment", testEnvironmentCombinations)
    @pytest.mark.parametrize("testParameters", httpDownloadTestParameters)
    def test_MAndroid2_HTTPDownload(self, rp_logger, json_metadata, testEnvironment, testParameters):
        # Define test case variables.
        testCaseKey = 'HTTPDownload'
        userFlag = 'MO'

        # Get and check test case info.
        testCaseInfo = checkTestCaseInfoConfig(testCaseKey)
        rp_logger.info("Test case info: {}.".format(testCaseInfo))
        rp_logger.info("Test environment: {}.".format(testEnvironment))
        rp_logger.info("Test testParameters: {}.".format(testParameters))

        # Execute test case.
        rp_logger.info("Executing test logic.")
        testResults = executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters,
                                      testCaseInfo, self.testCaseSummary, self.testCaseDetailList)

        # Write test case summary and test case detail.
        # self.testCaseSummary = writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        # self.testCaseDetailList = writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
        #                                                      testCaseInfo, testResults)
        writeExcelTestReportSummary(self.testCaseSummary, testResults, testEnvironment)
        writeExcelTestReportDetail(self.testCaseDetailList, testEnvironment, testParameters,
                                                             testCaseInfo, testResults)
        # Assert test result.
        rp_logger.info("Test result: {}.".format(testResults))
        for result in testResults:
            assert (result['checkPointResult'] == "passed")

        # Add some time interval for each run. Otherwise if forwarding result to realtime analysis reportportal, it will get interrupted status as test result.
        sleep(5)

if __name__ == '__main__':
    # Generate timestamp.
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%S.%f")

    # Get test report config.
    testReportConfigPath = "../configuration/testReportConfig/testReportConfig.yaml"
    testReportConfigName = "testReportConfig"
    reportConfig = checkTestReportConfig(testReportConfigPath, testReportConfigName)

    # Construct report parameters.
    htmlReportPath = reportConfig["reportPath"]["htmlReportPath"]
    jsonReportPath = reportConfig["reportPath"]["jsonReportPath"]
    allureReportPath = reportConfig["reportPath"]["allureReportPath"]

    htmlReport = " --html={}/htmlReport_{}.html".format(htmlReportPath, timestampStr)
    jsonReport = " --json-report --json-report-file {}/jsonReport_{}.json".format(jsonReportPath, timestampStr)
    allureReportDir = "{}/report".format(allureReportPath)
    allureResultDir = "{}/result".format(allureReportPath)
    allureReport = " --alluredir {}".format(allureReportDir)
    reportPortal = " --reportportal"

    # Execute test case.
    baseExecuteCommand = "pytest --reruns 5 --reruns-delay 1 -v test_MAndroid2AllDevices.py"
    executeCommand = baseExecuteCommand
    if (reportConfig["reportType"]["htmlReport"] == "True"):
        executeCommand = executeCommand + htmlReport

    if (reportConfig["reportType"]["jsonReport"] == "True"):
        executeCommand = executeCommand + jsonReport

    if (reportConfig["reportType"]["allureReport"] == "True"):
        executeCommand = executeCommand + allureReport

    if (reportConfig["reportType"]["reportPortalReport"] == "True"):
        executeCommand = executeCommand + reportPortal

    print (executeCommand)

    # executeCommand = "pytest --reruns 5 --reruns-delay 1 -v test_MAndroid2SimpleTestCases.py {} {} {}".format(jsonReport, htmlReport, allureReport)
    # print(executeCommand)

    output3 = os.system(executeCommand)
    # response = subprocess.check_output(generateReportCommand.split())
    # print("Response of test case executing is: ", response)

    if (reportConfig["reportType"]["allureReport"] == "True"):
        # Generate allure result.
        allureCommand = "allure generate --clean  {} -o {}".format(allureReportPath, allureResultDir)
        output4 = os.system(allureCommand)

        # Copy history to allure report.
        if (os.path.exists("{}/history".format(allureResultDir))):
            copy_tree("{}/history".format(allureResultDir), "{}/history".format(allureReportDir))

        # Regenerate allure result with history reports.
        output6 = os.system(allureCommand)

    # Start allure serve.
    # allureServeCommand = "allure serve {}".format(allureReportPath)
    # print(allureServeCommand)
    # print(allureServeCommand.split())
    # output4 = os.system(allureServeCommand)
    # response = subprocess.check_output(allureServeCommand.split())
    # print("Response of start allure serve is: ", response)


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
