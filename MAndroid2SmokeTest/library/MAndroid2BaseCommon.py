import json
import sys
from os import listdir
from time import sleep

import pytest
import xlsxwriter
import os
from datetime import datetime

from MAndroid2SmokeTest.library.MAndroid2BaseAPI import endBasicVoiceCall, placeBasicVoiceCall, receiveBasicVoiceCall, \
    getMAndroid2Version
from MAndroid2SmokeTest.library.MAndroid2BaseExcel import OperateReport
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def connectTestUsers(testEnvironment, userFlag):
    # Connect available test handset on mcloud from specified IMSI.
    mcloud = MCloudControl()

    # Set test environment variables.
    mcloud.mcloudBaseUrl = testEnvironment['MCloud']['baseUrl']
    mcloud.mcloudLoginUser = testEnvironment['Login']['User']
    mcloud.mcloudLoginToken = testEnvironment['Login']['accessToken']

    if (userFlag == "MO"):
        testEnvironment['testUsers']['MO']['handsetID'] = mcloud.connectToMcloudUser(
            testEnvironment['testUsers']['MO']['IMSI'])
        assert (testEnvironment['testUsers']['MO']['handsetID'] != None)
        print("MO Handset ID is {}".format(testEnvironment['testUsers']['MO']['handsetID']))
        # Get MAndroid2 version info.
        testEnvironment['testUsers']['MO']['versions'] = getMAndroid2Version(testEnvironment['testUsers']['MO']['handsetID'])
    elif (userFlag == "MT"):
        testEnvironment['testUsers']['MT']['handsetID'] = mcloud.connectToMcloudUser(
            testEnvironment['testUsers']['MT']['IMSI'])
        assert (testEnvironment['testUsers']['MT']['handsetID'] != None)
        print("MT Handset ID is {}".format(testEnvironment['testUsers']['MT']['handsetID']))
        # Get MAndroid2 version info.
        testEnvironment['testUsers']['MT']['versions'] = getMAndroid2Version(testEnvironment['testUsers']['MT']['handsetID'])

    elif (userFlag == "MOMT"):
        testEnvironment['testUsers']['MO']['handsetID'] = mcloud.connectToMcloudUser(
            testEnvironment['testUsers']['MO']['IMSI'])
        assert (testEnvironment['testUsers']['MO']['handsetID'] != None)
        print("MO Handset ID is {}".format(testEnvironment['testUsers']['MO']['handsetID']))
        testEnvironment['testUsers']['MT']['handsetID'] = mcloud.connectToMcloudUser(
            testEnvironment['testUsers']['MT']['IMSI'])
        assert (testEnvironment['testUsers']['MT']['handsetID'] != None)
        print("MT Handset ID is {}".format(testEnvironment['testUsers']['MT']['handsetID']))
        # Get MAndroid2 version info.
        testEnvironment['testUsers']['MO']['versions'] = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'], testEnvironment['testUsers']['MO']['handsetID'])
        testEnvironment['testUsers']['MT']['versions'] = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'], testEnvironment['testUsers']['MT']['handsetID'])

    else:
        print("Cannot recognize userFlag {}".format(userFlag))

    return testEnvironment

def disconnectTestUsers():
    # Disconnect connected devices.
    mcloud = MCloudControl()
    print("deviceSerialList to be disconnected is {}".format(mcloud.deviceSerialList))
    mcloud.tearDownUsingDevices(mcloud.deviceSerialList)


def addJsonReportMetaData(json_metadata, testEnvironment, testParameters, testCaseInfo, testResults):
    json_metadata['testEnvironment'] = testEnvironment
    json_metadata['testParameters'] = testParameters
    json_metadata['testCaseInfo'] = testCaseInfo
    json_metadata['testResults'] = testResults

def checkTestEnvironmentConfig(testEnvironment):
    # Check test environment information from configuration file.
    assert ("MCloud" in testEnvironment)
    assert ("baseUrl" in testEnvironment['MCloud'])
    assert ("Login" in testEnvironment)
    assert ("User" in testEnvironment['Login'])
    assert ("accessToken" in testEnvironment['Login'])
    assert ("MAndroid2AgentPath" in testEnvironment)

    assert ("testUsers" in testEnvironment)
    assert ("MO" in testEnvironment['testUsers'])
    assert ("IMSI" in testEnvironment['testUsers']['MO'])
    assert ("MSISDN" in testEnvironment['testUsers']['MO'])

    assert ("MT" in testEnvironment['testUsers'])
    assert ("IMSI" in testEnvironment['testUsers']['MT'])
    assert ("MSISDN" in testEnvironment['testUsers']['MT'])

def checkTestParametersConfig(testParameters, testCaseKey):
    # Check test parameters from configuration file.
    if (testCaseKey == 'VoiceCall'):
        assert ("VoiceCall" in testParameters)
        assert ("Duration" in testParameters['VoiceCall'])
        print("Voice call duration is {}".format(testParameters['VoiceCall']['Duration']))

def checkTestCaseInfoConfig(testCaseInfo):
    # Check test case info from configuration file.
    assert ("TestCaseID" in testCaseInfo)
    assert ("Description" in testCaseInfo)
    assert ("Precondition" in testCaseInfo)
    assert ("TestSteps" in testCaseInfo)
    assert ("CheckPoints" in testCaseInfo)


def executeTestLogic(testEnvironment, testCaseInfo, testCaseKey, testParameters):
    responseList = []

    if (testCaseKey == 'VoiceCall'):
        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Place voice call.'):
                placeResponse = placeBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                    testEnvironment['testUsers']['MO']['handsetID'],
                                                    testEnvironment['testUsers']['MT']['MSISDN'])
                response['placeVoiceCall'] = placeResponse
            elif (testStep == 'Receive voice call.'):
                receiveResponse = receiveBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                        testEnvironment['testUsers']['MT']['handsetID'])
                response['receiveVoiceCall'] = receiveResponse
            elif (testStep == 'Wait for call duraton.'):
                if (testParameters['VoiceCall']['Duration'] > 0):
                        sleep(testParameters['VoiceCall']['Duration'])
            elif (testStep == 'End voice call.'):
                endResponse = endBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                testEnvironment['testUsers']['MO']['handsetID'])
                response['endVoiceCall'] = endResponse
            else:
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    return responseList

def verifyTestCaseResult(testCaseInfo, testCaseKey, responseList):
    testResults = []
    testResult = {}

    if (testCaseKey == 'VoiceCall'):
        checkPoints = testCaseInfo['CheckPoints']
        for checkPoint in checkPoints:
            testResult = {}
            testResult['checkPointResult'] = "failed"
            verifiedCheckPointFlag = False
            if (checkPoint == 'Place voice call successfully.'):
                for response in responseList:
                    if 'placeVoiceCall' in response:
                        testResult = verifyPlaceVoiceCallResponse(response['placeVoiceCall'])
                        verifiedCheckPointFlag = True
            elif (checkPoint == 'Receive voice call successfully.'):
                for response in responseList:
                    if 'receiveVoiceCall' in response:
                        testResult = verifyReceiveVoiceCallResponse(response['receiveVoiceCall'])
                        verifiedCheckPointFlag = True
            elif (checkPoint == 'End voice call successfully.'):
                for response in responseList:
                    if 'endVoiceCall' in response:
                        testResult = verifyEndVoiceCallResponse(response['endVoiceCall'])
                        verifiedCheckPointFlag = True

            if (verifiedCheckPointFlag == False):
                testResult['failedReason'] = "Cannot verify this check point in test case."
                testResult['command'] = response['command']
                testResult['response'] = response['response']

            testResult['checkPoint'] = checkPoint
            testResults. append(testResult)

    return testResults

def verifyPlaceVoiceCallResponse(response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    if ('isSuccess' in response['response']):
        if ((response['response']['isSuccess'] == True) or (response['response']['isSuccess'] == 'true')):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['failedReason'] = "Failed to place voice call."
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyReceiveVoiceCallResponse(response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    if ('isSuccess' in response['response']):
        if ((response['response']['isSuccess'] == True) or (response['response']['isSuccess'] == 'true')):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['failedReason'] = "Failed to receive voice call."
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyEndVoiceCallResponse(response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    if ('isSuccess' in response['response']):
        if ((response['response']['isSuccess'] == True) or (response['response']['isSuccess'] == 'true')):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['failedReason'] = "Failed to end voice call."
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def createExcelTestReport(excelReportPath):

    # Get current time.
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reportFileName = "{}MAndroid2TestReport_{}.xlsx".format(excelReportPath, timeStamp)

    # Create an excel report.
    workbook = xlsxwriter.Workbook(reportFileName)
    summarySheet = workbook.add_worksheet("TestSummary")
    detailSheet = workbook.add_worksheet("TestDetail")
    excelReport = OperateReport(wd=workbook)

    return excelReport, summarySheet, detailSheet


def initializeExcelSummary(testCaseSummary):

    testCaseSummary['sum'] = 0
    testCaseSummary['pass'] = 0
    testCaseSummary['fail'] = 0

    testCaseSummary['MAndroid2AgentVersion'] = "None"
    testCaseSummary['testingDate'] = "None"
    testCaseSummary['testDuration'] = "0 s"

    return testCaseSummary

def writeExcelTestReportSummary(testCaseSummary, testResults, testEnvironment):

    testCaseResult = True
    for result in testResults:
        if (result['checkPointResult'] != "passed"):
            testCaseResult = False
            break

    testCaseSummary['sum'] = testCaseSummary['sum'] + 1
    if (testCaseResult == True):
        testCaseSummary['pass'] = testCaseSummary['pass'] + 1
    else:
        testCaseSummary['fail'] = testCaseSummary['fail'] + 1

    testCaseSummary['MAndroid2AgentVersion'] = testEnvironment['testUsers']['MO']['versions']['MAndroid2Agent']

    return testCaseSummary

def writeExcelTestReportDetail(testCaseDetailList, testEnvironment, testParameters, testCaseInfo, testResults):

    # Initialization.
    testCaseDetail = {}
    testCaseResult = True

    # Fill information.
    testCaseDetail['TestCaseID'] = testCaseInfo['TestCaseID']
    testCaseDetail['Description'] = testCaseInfo['Description']

    testCaseDetail['moInfo'] = json.dumps(testEnvironment['testUsers']['MO'])
    testCaseDetail['mtInfo'] = json.dumps(testEnvironment['testUsers']['MT'])
    testCaseDetail['testParameters'] = json.dumps(testParameters)

    testCaseDetail['Precondition'] = '\n'.join(testCaseInfo['Precondition'])
    testCaseDetail['TestSteps'] = '\n'.join(testCaseInfo['TestSteps'])
    testCaseDetail['CheckPoints'] = '\n'.join(testCaseInfo['CheckPoints'])

    testCaseDetail['testResultList'] = '\n'.join(json.dumps(element) for element in testResults)

    for result in testResults:
        if (result['checkPointResult'] != "passed"):
            testCaseResult = False
            break
    if (testCaseResult == True):
        testCaseDetail['testResult'] = "passed"
    else:
        testCaseDetail['testResult'] = "failed"

    testCaseDetailList.append(testCaseDetail)

    return testCaseDetailList