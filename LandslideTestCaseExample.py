import json
import os
import sys
import unittest

from LandslideBaseYaml import getYam

ABSPATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

RELPATH = lambda p: os.path.relpath(
    os.path.join(os.path.dirname(__file__), p)
)


class Voice3G(unittest.TestCase):

    # path = RELPATH("../YMAL/LandslideTestCaseYamlExample.yaml")
    # path = RELPATH("YMAL/LandslideTestCaseYamlExample.yaml")
    path = RELPATH("LandslideTestCaseYamlExample.yaml")

    def __init__(self, **kwargs):

        yaml = getYam(self.path)
        if (yaml[0] == False):
            print("Failed to read test configuration yaml file from {}".format(self.path))
            sys.exit("Failed to read test configuration yaml file from {}".format(self.path))
        else:
            print("Read test configuration yaml file from {} successfully.".format(self.path))

        self.testInfoList = yaml[1]["testinfo"]
        self.testparametersList = yaml[1]["testparameters"]
        self.checkMetricList = yaml[1]["checkMetric"]
        print ("testInfo: ", self.testInfoList)
        print("testparameters: ", self.testparametersList)
        print("checkMetric: ", self.checkMetricList)

        # for testInfo in self.testInfoList:
        #     if (testInfo["description"] == "3G voice"):
        #         print('checkPoint is "{}" for test case "{}"'.format(testInfo["checkPoint"], testInfo["description"]))
        #         print('test result is "{}" for test case "{}"'.format(testInfo["checkPoint"], testInfo["description"]))
        testInfo = self.testInfoList
        if (testInfo["description"] == "3G voice"):
            print('checkPoint is "{}" for test case "{}"'.format(testInfo["checkPoint"], testInfo["description"]))
            print('test result is "{}" for test case "{}"'.format(testInfo["checkPoint"], testInfo["description"]))

if __name__ == '__main__':
   # unittest.main
   Voice3G = Voice3G()
   testData = {'title': '4G', 'id': '1', 'info': '4G voice test'}
   testData['result'] = 'Passed'

   print (testData)