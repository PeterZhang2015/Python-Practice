import os
import subprocess
import sys

# from ..library.MAndroid2BaseYaml import getYam
# from ..library.MAndroid2BaseMCloud import MCloudControl
from datetime import datetime

import pytest

from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

RELPATH = lambda p: os.path.relpath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestMAndroid2TestCases():
    # Initialize variables.
    mo = {}
    mt = {}

    @classmethod
    def setup_class(self):
        # Get test parameters.
        self.getTestParameters(self)
        self.mo['IMSI'] = self.testparametersList['MO']['IMSI']
        self.mt['IMSI'] = self.testparametersList['MT']['IMSI']

        # Connect available test handset on mcloud from specified IMSI.
        mcloud = MCloudControl()
        self.mo['handsetID'] = mcloud.connectToMcloudUser(self.mo['IMSI'])
        print("Handset ID is {}".format(self.mo['handsetID']))

        assert (self.mo['handsetID'] != None)


    @classmethod
    def teardown_class(self):
        # Disconnect connected devices.
        mcloud = MCloudControl()
        mcloud.tearDownUsingDevices(mcloud.deviceSerialList)


    def getTestParameters(self):
        self.path = RELPATH("../configuration/MAndroid2SmokeTestParameters.yaml")
        yaml = getYam(self.path)

        if (yaml[0] == False):
            print("Failed to read test configuration yaml file from {}".format(self.path))
            sys.exit("Failed to read test configuration yaml file from {}".format(self.path))
        else:
            print("Read test configuration yaml file from {} successfully.".format(self.path))

        self.testInfoList = yaml[1]['testinfo']
        self.testparametersList = yaml[1]['testparameters']
        self.checkMetricList = yaml[1]['checkMetric']
        # print ("testInfo: ", self.testInfoList)
        # print("testparameters: ", self.testparametersList)
        # print("checkMetric: ", self.checkMetricList)

    def test_MAndroid2_VoiceCall(self, json_metadata):
        print ("Test")
        self.addJsonReportMetaData(json_metadata)

    def addJsonReportMetaData(self, json_metadata):
        json_metadata['mo'] = self.mo
        json_metadata['mt'] = self.mt



if __name__ == '__main__':

    # Generate timestamp.
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d_%b_%Y_%H_%M_%S.%f")

    # Construct report parameters.
    reportPath = RELPATH("../reports")
    htmlReport = "--html={}/html/htmlReport_{}.html".format(reportPath, timestampStr)
    jsonReport = "--json-report --json-report-file {}/json/jsonReport_{}.json".format(reportPath, timestampStr)
    print (jsonReport)

    # Execute test case.
    generateReportCommand = "pytest -q -r test_MAndroid2TestCases.py {} {}".format(jsonReport, htmlReport)
    print(generateReportCommand)
    output3 = os.system(generateReportCommand)

    # Execute test cases and generate reports. Not sure why it is not working for json report.
    # pytest.main(["-q", "-r", "test_MAndroid2TestCases.py", jsonReport, htmlReport])
    # pytest.main(["-q", "-r", "test_MAndroid2TestCases.py", jsonReport])

    #pytest.main(["-v","test_MAndroid2TestCases.py",'--alluredir','result'])

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

