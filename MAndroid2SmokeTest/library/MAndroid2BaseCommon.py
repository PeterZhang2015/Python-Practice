import json
import sys
from os import listdir
from time import sleep

import pytest
import xlsxwriter
import os
from datetime import datetime

from MAndroid2SmokeTest.library.MAndroid2BaseAPI import endBasicVoiceCall, placeBasicVoiceCall, receiveBasicVoiceCall, \
    getMAndroid2Version, sendSMS, receiveSMS, getMMSUrl, unlockHandsetScreen, sendMMS, receiveMMS
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
    elif (testCaseKey == 'SMS'):
        assert ("SMS" in testParameters)
        assert ("Duration" in testParameters['SMS'])
        assert ("smsBody" in testParameters['SMS'])
    elif (testCaseKey == 'MMS'):
        assert ("MMS" in testParameters)
        assert ("Duration" in testParameters['MMS'])
        assert ("mmsBody" in testParameters['MMS'])

def checkTestCaseInfoConfig(testCaseInfo):
    # Check test case info from configuration file.
    assert ("TestCaseID" in testCaseInfo)
    assert ("Description" in testCaseInfo)
    assert ("Precondition" in testCaseInfo)
    assert ("TestSteps" in testCaseInfo)
    assert ("CheckPoints" in testCaseInfo)


def executeTestLogic(testEnvironment, testCaseInfo, testCaseKey, testParameters):

    # Variables initialization.
    responseList = []

    # Test logic for voice call.
    if (testCaseKey == 'VoiceCall'):
        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Place voice call.'):
                placeVoiceCallResponse = placeBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                    testEnvironment['testUsers']['MO']['handsetID'],
                                                    testEnvironment['testUsers']['MT']['MSISDN'])
                response['placeVoiceCall'] = placeVoiceCallResponse
            elif (testStep == 'Receive voice call.'):
                receiveVoiceCallResponse = receiveBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                        testEnvironment['testUsers']['MT']['handsetID'])
                response['receiveVoiceCall'] = receiveVoiceCallResponse
            elif (testStep == 'Wait for call duraton.'):
                if (testParameters['VoiceCall']['Duration'] > 0):
                        sleep(testParameters['VoiceCall']['Duration'])
            elif (testStep == 'End voice call.'):
                endVoiceCallResponse = endBasicVoiceCall(testEnvironment['MAndroid2AgentPath'],
                                                testEnvironment['testUsers']['MO']['handsetID'])
                response['endVoiceCall'] = endVoiceCallResponse
            else:
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    # Test logic for SMS.
    elif (testCaseKey == 'SMS'):
        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Send SMS.'):
                sendSMSResponse = sendSMS(testEnvironment['MAndroid2AgentPath'],
                                                    testEnvironment['testUsers']['MO']['handsetID'],
                                                    testEnvironment['testUsers']['MT']['MSISDN'],
                                                    testParameters['SMS']['smsBody'])
                response['sendSMS'] = sendSMSResponse
            elif (testStep == 'Wait for SMS duraton.'):
                if (testParameters['SMS']['Duration'] > 0):
                        sleep(testParameters['SMS']['Duration'])
            elif (testStep == 'Receive SMS.'):
                receiveSMSResponse = receiveSMS(testEnvironment['MAndroid2AgentPath'],
                                                testEnvironment['testUsers']['MT']['handsetID'])
                response['receiveSMS'] = receiveSMSResponse
            else:
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    # Test logic for MMS.
    elif (testCaseKey == 'MMS'):

        testPreconditions = testCaseInfo['Precondition']
        for testPrecondition in testPreconditions:
            response = {}
            if (testPrecondition == 'Get a file as MMS url by 1033 API.'):
                mmsUrl = getMMSUrl(testEnvironment['MAndroid2AgentPath'],
                          testEnvironment['testUsers']['MO']['handsetID'])

        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Unlock handset screen.'):
                unlockHandsetScreenResponse = unlockHandsetScreen(testEnvironment['MAndroid2AgentPath'],
                                          testEnvironment['testUsers']['MO']['handsetID'])
                response['unlockHandsetScreen'] = unlockHandsetScreenResponse
            elif (testStep == 'Send MMS.'):
                sendSMSResponse = sendMMS(testEnvironment['MAndroid2AgentPath'],
                                          testEnvironment['testUsers']['MO']['handsetID'],
                                          testEnvironment['testUsers']['MT']['MSISDN'],
                                          testParameters['MMS']['mmsBody'],
                                          mmsUrl)
                response['sendMMS'] = sendSMSResponse
            elif (testStep == 'Wait for SMS duraton.'):
                if (testParameters['SMS']['Duration'] > 0):
                        sleep(testParameters['SMS']['Duration'])
            elif (testStep == 'Receive SMS.'):
                receiveSMSResponse = receiveSMS(testEnvironment['MAndroid2AgentPath'],
                                                testEnvironment['testUsers']['MT']['handsetID'])
                response['receiveSMS'] = receiveSMSResponse
            else:
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)


    return responseList

def verifyTestCaseResult(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList):

    # Variables initialization.
    testResults = []
    testResult = {}


    if (testCaseKey == 'VoiceCall'):
        # Verify test case result for voice call.
        testResults = verifyVoiceCall(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList)

    elif (testCaseKey == 'SMS'):
        # Verify test case result for SMS.
        testResults = verifySMS(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList)

    elif (testCaseKey == 'MMS'):
        # Verify test case result for SMS.
        testResults = verifyMMS(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList)


    return testResults

def verifyVoiceCall(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList):
    # Variables initialization.
    testResults = []

    # Verify voice call result with test case check points.
    checkPoints = testCaseInfo['CheckPoints']
    for checkPoint in checkPoints:
        testResult = {}
        testResult['checkPointResult'] = "failed"
        verifiedCheckPointFlag = False
        if (checkPoint == 'Place voice call successfully.'):
            for response in responseList:
                if 'placeVoiceCall' in response:
                    testResult = verifyPlaceVoiceCallResponse(testEnvironment, testParameters, response['placeVoiceCall'])
                    verifiedCheckPointFlag = True
        elif (checkPoint == 'Receive voice call successfully.'):
            for response in responseList:
                if 'receiveVoiceCall' in response:
                    testResult = verifyReceiveVoiceCallResponse(testEnvironment, testParameters, response['receiveVoiceCall'])
                    verifiedCheckPointFlag = True
        elif (checkPoint == 'End voice call successfully.'):
            for response in responseList:
                if 'endVoiceCall' in response:
                    testResult = verifyEndVoiceCallResponse(testEnvironment, testParameters, response['endVoiceCall'])
                    verifiedCheckPointFlag = True

        if (verifiedCheckPointFlag == False):
            testResult['failedReason'] = "Cannot verify this check point in test case."
            testResult['command'] = response['command']
            testResult['response'] = response['response']

        testResult['checkPoint'] = checkPoint
        testResults.append(testResult)

    return testResults

def verifySMS(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList):
    # Variables initialization.
    testResults = []

    # Verify SMS result with test case check points.
    checkPoints = testCaseInfo['CheckPoints']
    for checkPoint in checkPoints:
        testResult = {}
        testResult['checkPointResult'] = "failed"
        verifiedCheckPointFlag = False
        if (checkPoint == 'Send SMS successfully.'):
            for response in responseList:
                if 'sendSMS' in response:
                    testResult = verifySendSMSResponse(testEnvironment, testParameters, response['sendSMS'])
                    verifiedCheckPointFlag = True
        elif (checkPoint == 'Receive SMS successfully.'):
            for response in responseList:
                if 'receiveSMS' in response:
                    testResult = verifyReceiveSMSResponse(testEnvironment, testParameters, response['receiveSMS'])
                    verifiedCheckPointFlag = True

        if (verifiedCheckPointFlag == False):
            testResult['failedReason'] = "Cannot verify this check point in test case."
            testResult['command'] = response['command']
            testResult['response'] = response['response']

        testResult['checkPoint'] = checkPoint
        testResults.append(testResult)

    return testResults

def verifyMMS(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList):
    # Variables initialization.
    testResults = []

    # Verify MMS result with test case check points.
    checkPoints = testCaseInfo['CheckPoints']
    for checkPoint in checkPoints:
        testResult = {}
        testResult['checkPointResult'] = "failed"
        verifiedCheckPointFlag = False
        if (checkPoint == 'Unlock handset screen successfully.'):
            for response in responseList:
                if 'unlockHandsetScreen' in response:
                    testResult = verifyUnlockHandsetScreenResponse(testEnvironment, testParameters, response['unlockHandsetScreen'])
                    verifiedCheckPointFlag = True
        elif (checkPoint == 'Send MMS successfully.'):
            for response in responseList:
                if 'sendMMS' in response:
                    testResult = verifySendMMSResponse(testEnvironment, testParameters, response['sendMMS'])
                    verifiedCheckPointFlag = True
        elif (checkPoint == 'Receive MMS successfully.'):
            for response in responseList:
                if 'receiveMMS' in response:
                    testResult = verifyReceiveMMSResponse(testEnvironment, testParameters, response['receiveMMS'])
                    verifiedCheckPointFlag = True

        if (verifiedCheckPointFlag == False):
            testResult['failedReason'] = "Cannot verify this check point in test case."
            testResult['command'] = response['command']
            testResult['response'] = response['response']

        testResult['checkPoint'] = checkPoint
        testResults.append(testResult)

    return testResults

def verifyPlaceVoiceCallResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to place voice call."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyReceiveVoiceCallResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to receive voice call."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyEndVoiceCallResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to end voice call."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifySendSMSResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to send SMS."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyReceiveSMSResponse(testEnvironment, testParameters, response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    # Verification for 'isSuccess'.
    if ('isSuccess' in response['response']):
        if ((response['response']['isSuccess'] == True) or (response['response']['isSuccess'] == 'true')):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to receive SMS."
            return testResult
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."
        return testResult

    # Verification for 'smsFrom'.
    if ('smsFrom' in response['response']):
        if (response['response']['smsFrom'] == testEnvironment['testUsers']['MO']['MSISDN']):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Latest SMS is from {} rather than {}.".format(response['response']['smsFrom'], testEnvironment['testUsers']['MT']['MSISDN'])
            return testResult
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'smsFrom' in the response."
        return testResult

    # Verification for 'smsBody'.
    if ('smsBody' in response['response']):
        if (response['response']['smsBody'] == testParameters['SMS']['smsBody']):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to receive SMS with SMS body {}.".format(testParameters['SMS']['smsBody'])
            return testResult
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'smsBody' in the response."
        return testResult

    # Return result.
    return testResult

def verifyUnlockHandsetScreenResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to unlock handset screen."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifySendMMSResponse(testEnvironment, testParameters, response):
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
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to send MMS."
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."

    # Return result.
    return testResult

def verifyReceiveMMSResponse(testEnvironment, testParameters, response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    # Verification for 'isSuccess'.
    if ('isSuccess' in response['response']):
        if ((response['response']['isSuccess'] == True) or (response['response']['isSuccess'] == 'true')):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to receive MMS."
            return testResult
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."
        return testResult

    # Verification for 'mmsFrom'.
    if ('mmsFrom' in response['response']):
        if (response['response']['mmsFrom'] == testEnvironment['testUsers']['MO']['MSISDN']):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Latest MMS is from {} rather than {}.".format(response['response']['mmsFrom'], testEnvironment['testUsers']['MT']['MSISDN'])
            return testResult
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'mmsFrom' in the response."
        return testResult

    # Verification for 'mmsBody'.
    if ('mmsBody' in response['response']):
        if (response['response']['mmsBody'] == testParameters['MMS']['mmsBody']):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "Failed to receive MMS with MMS body {}.".format(testParameters['MMS']['mmsBody'])
            return testResult
    else:
        testResult['checkPointResult'] = "failed"
        testResult['failedReason'] = "Cannot find 'mmsBody' in the response."
        return testResult

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