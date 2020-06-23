import json
import sys
from os import listdir
from time import sleep

import pytest
import xlsxwriter
import os
from datetime import datetime

from MAndroid2SmokeTest.library.MAndroid2BaseAPI import endBasicVoiceCall, placeBasicVoiceCall, receiveBasicVoiceCall, \
    getMAndroid2Version, sendSMS, receiveSMS, getMMSUrl, unlockHandsetScreen, sendMMS, receiveMMS, webBrowsing, \
    startHTTPDownload, getFileInfo
from MAndroid2SmokeTest.library.MAndroid2BaseExcel import OperateReport
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam, getConfigureInfo
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

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

    testCaseDetail['Preconditions'] = '\n'.join(testCaseInfo['Preconditions'])
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

def writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment, testParameters, testCaseInfo):
    # Initialization.
    testCaseDetail = {}

    # Write test case detail.
    testCaseDetail['TestCaseID'] = testCaseInfo['TestCaseID']
    testCaseDetail['Description'] = testCaseInfo['Description']

    testCaseDetail['moInfo'] = json.dumps(testEnvironment['testUsers']['MO'])
    testCaseDetail['mtInfo'] = json.dumps(testEnvironment['testUsers']['MT'])
    testCaseDetail['testParameters'] = json.dumps(testParameters)

    testCaseDetail['Preconditions'] = '\n'.join(testCaseInfo['Preconditions'])
    testCaseDetail['TestSteps'] = '\n'.join(testCaseInfo['TestSteps'])
    testCaseDetail['CheckPoints'] = '\n'.join(testCaseInfo['CheckPoints'])

    testCaseDetail['testResultList'] = failedReason
    testCaseDetail['testResult'] = "failed"

    testCaseDetailList.append(testCaseDetail)

    # Write test case summary.
    testCaseSummary['sum'] = testCaseSummary['sum'] + 1
    testCaseSummary['fail'] = testCaseSummary['fail'] + 1
    testCaseSummary['MAndroid2AgentVersion'] = testEnvironment['testUsers']['MO']['versions']['MAndroid2Agent']





def connectTestUsers(testEnvironment, userFlag, testParameters, testCaseInfo, testCaseSummary, testCaseDetailList):
    # Connect available test handset on mcloud from specified IMSI.
    mcloud = MCloudControl()

    # Set test environment variables.
    mcloud.mcloudBaseUrl = testEnvironment['MCloud']['baseUrl']
    mcloud.mcloudLoginUser = testEnvironment['Login']['User']
    mcloud.mcloudLoginToken = testEnvironment['Login']['accessToken']

    if (userFlag == "MO"):
        testEnvironment['testUsers']['MO']['handsetID'] = mcloud.connectToMcloudUser(testEnvironment['testUsers']['MO']['IMSI'])

        if testEnvironment['testUsers']['MO']['handsetID'] == None:
            failedReason = "Cannot connect to user {}".format(testEnvironment['testUsers']['MO']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
        assert (testEnvironment['testUsers']['MO']['handsetID'] != None)
        print("MO Handset ID is {}".format(testEnvironment['testUsers']['MO']['handsetID']))

        # Get MAndroid2 version info.
        version = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'],
                                      testEnvironment['testUsers']['MO']['handsetID'])
        if version != None:
            testEnvironment['testUsers']['MO']['versions'] = version
        else:
            failedReason = "Cannot get MAndroid2 version from {}".format(testEnvironment['testUsers']['MO']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
    elif (userFlag == "MT"):
        testEnvironment['testUsers']['MT']['handsetID'] = mcloud.connectToMcloudUser(testEnvironment['testUsers']['MT']['IMSI'])

        if testEnvironment['testUsers']['MT']['handsetID'] == None:
            failedReason = "Cannot connect to user {}".format(testEnvironment['testUsers']['MT']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
        assert (testEnvironment['testUsers']['MT']['handsetID'] != None)
        print("MT Handset ID is {}".format(testEnvironment['testUsers']['MT']['handsetID']))

        # Get MAndroid2 version info.
        version = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'],
                                      testEnvironment['testUsers']['MT']['handsetID'])
        if version != None:
            testEnvironment['testUsers']['MT']['versions'] = version
        else:
            failedReason = "Cannot get MAndroid2 version from {}".format(testEnvironment['testUsers']['MT']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)

    elif (userFlag == "MOMT"):
        testEnvironment['testUsers']['MO']['handsetID'] = mcloud.connectToMcloudUser(testEnvironment['testUsers']['MO']['IMSI'])

        if testEnvironment['testUsers']['MO']['handsetID'] == None:
            failedReason = "Cannot connect to user {}".format(testEnvironment['testUsers']['MO']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
        assert (testEnvironment['testUsers']['MO']['handsetID'] != None)
        print("MO Handset ID is {}".format(testEnvironment['testUsers']['MO']['handsetID']))

        testEnvironment['testUsers']['MT']['handsetID'] = mcloud.connectToMcloudUser(testEnvironment['testUsers']['MT']['IMSI'])
        if testEnvironment['testUsers']['MT']['handsetID'] == None:
            failedReason = "Cannot connect to user {}".format(testEnvironment['testUsers']['MT']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
        assert (testEnvironment['testUsers']['MT']['handsetID'] != None)
        print("MT Handset ID is {}".format(testEnvironment['testUsers']['MT']['handsetID']))
        # Get MAndroid2 version info.
        version = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'],
                                      testEnvironment['testUsers']['MO']['handsetID'])
        if version != None:
            testEnvironment['testUsers']['MO']['versions'] = version
        else:
            failedReason = "Cannot get MAndroid2 version from {}".format(testEnvironment['testUsers']['MO']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)

        version = getMAndroid2Version(testEnvironment['MAndroid2AgentPath'],
                                      testEnvironment['testUsers']['MT']['handsetID'])
        if version != None:
            testEnvironment['testUsers']['MT']['versions'] = version
        else:
            failedReason = "Cannot get MAndroid2 version from {}".format(testEnvironment['testUsers']['MT']['handsetID'])
            writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                       testParameters, testCaseInfo)
    else:
        print("Cannot recognize userFlag {}".format(userFlag))


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
    elif (testCaseKey == 'WebBrowsing'):
        assert ("WebBrowsing" in testParameters)
        assert ("webUrl" in testParameters['WebBrowsing'])
    elif (testCaseKey == 'HTTPDownload'):
        assert ("HTTPDownload" in testParameters)
        assert ("downloadUrl" in testParameters['HTTPDownload'])
        assert ("Duration" in testParameters['HTTPDownload'])

def checkTestCaseInfoConfig(testCaseKey):
    # Get test case info configuration.
    testCaseInfoFileName = "../configuration/testCaseInfo/testCaseInfo.yaml"
    testCaseInfo = getConfigureInfo(testCaseInfoFileName, testCaseKey)

    # Check test case info from configuration file.
    assert ("TestCaseID" in testCaseInfo)
    assert ("Description" in testCaseInfo)
    assert ("Preconditions" in testCaseInfo)
    assert ("TestSteps" in testCaseInfo)
    assert ("CheckPoints" in testCaseInfo)

    # Return
    return testCaseInfo

def executeTestCase(testCaseKey, userFlag, json_metadata, testEnvironment, testParameters, testCaseInfo, testCaseSummary, testCaseDetailList):

    # Initialization
    responseList = []
    testResults = []

    # Checking Test parameters.
    checkTestEnvironmentConfig(testEnvironment)
    checkTestParametersConfig(testParameters, testCaseKey)

    # ConnectTestUsers.
    connectTestUsers(testEnvironment, userFlag, testParameters, testCaseInfo, testCaseSummary, testCaseDetailList)

    # Starting test logic.
    responseList = executeTestLogic(testEnvironment, testCaseInfo, testCaseKey, testParameters, testCaseSummary, testCaseDetailList)

    # Disconnect testing users.
    disconnectTestUsers()

    # Verify test result.
    testResults = verifyTestCaseResult(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList)

    # Adding information to json report.
    addJsonReportMetaData(json_metadata, testEnvironment, testParameters, testCaseInfo, testResults)

    return testResults

def executeTestLogic(testEnvironment, testCaseInfo, testCaseKey, testParameters, testCaseSummary, testCaseDetailList):

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
                failedReason = "Test step {} cannot be recognized in test case.".format(testStep)
                writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                           testParameters, testCaseInfo)
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
                failedReason = "Test step {} cannot be recognized in test case.".format(testStep)
                writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                           testParameters, testCaseInfo)
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    # Test logic for MMS.
    elif (testCaseKey == 'MMS'):

        testPreconditions = testCaseInfo['Preconditions']
        for testPrecondition in testPreconditions:
            response = {}
            if (testPrecondition == 'Get a file as MMS url by 1033 API.'):
                mmsUrl = getMMSUrl(testEnvironment['MAndroid2AgentPath'],
                          testEnvironment['testUsers']['MO']['handsetID'])
                if mmsUrl == None:
                    failedReason = "Cannot get MMS URL on {}.".format(testEnvironment['testUsers']['MO']['handsetID'])
                    writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                               testParameters, testCaseInfo)
                    assert ("Cannot get MMS URL on {}.".format(testEnvironment['testUsers']['MO']['handsetID']))

        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Unlock handset screen.'):
                unlockHandsetScreenResponse = unlockHandsetScreen(testEnvironment['MAndroid2AgentPath'],
                                          testEnvironment['testUsers']['MO']['handsetID'])
                response['unlockHandsetScreen'] = unlockHandsetScreenResponse
            elif (testStep == 'Wait for screen unlock.'):
                if (testParameters['MMS']['ScreenUnlockDuration'] > 0):
                        sleep(testParameters['MMS']['ScreenUnlockDuration'])
            elif (testStep == 'Send MMS.'):
                sendMMSResponse = sendMMS(testEnvironment['MAndroid2AgentPath'],
                                          testEnvironment['testUsers']['MO']['handsetID'],
                                          testEnvironment['testUsers']['MT']['MSISDN'],
                                          testParameters['MMS']['mmsBody'],
                                          mmsUrl)
                response['sendMMS'] = sendMMSResponse
            elif (testStep == 'Wait for MMS duraton.'):
                if (testParameters['MMS']['Duration'] > 0):
                        sleep(testParameters['MMS']['Duration'])
            elif (testStep == 'Receive MMS.'):
                receiveMMSResponse = receiveMMS(testEnvironment['MAndroid2AgentPath'],
                                                testEnvironment['testUsers']['MT']['handsetID'])
                response['receiveMMS'] = receiveMMSResponse
            else:
                failedReason = "Test step {} cannot be recognized in test case.".format(testStep)
                writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                           testParameters, testCaseInfo)
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    # Test logic for web browsing.
    elif (testCaseKey == 'WebBrowsing'):
        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Web Browsing.'):
                webBrowsingResponse = webBrowsing(testEnvironment['MAndroid2AgentPath'],
                                                    testEnvironment['testUsers']['MO']['handsetID'],
                                                    testParameters['WebBrowsing']['webUrl'])
                response['webBrowsing'] = webBrowsingResponse
            else:
                failedReason = "Test step {} cannot be recognized in test case.".format(testStep)
                writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                           testParameters, testCaseInfo)
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    # Test logic for HTTP Download.
    elif (testCaseKey == 'HTTPDownload'):
        testSteps = testCaseInfo['TestSteps']
        for testStep in testSteps:
            response = {}
            if (testStep == 'Start HTTP download.'):
                startHTTPDownloadResponse = startHTTPDownload(testEnvironment['MAndroid2AgentPath'],
                                                              testEnvironment['testUsers']['MO']['handsetID'],
                                                              testParameters['HTTPDownload']['downloadUrl'])
                response['startHTTPDownload'] = startHTTPDownloadResponse
                if ('downloadFile' in response['startHTTPDownload']):
                    downloadedFileInfoResponse = getFileInfo(testEnvironment['MAndroid2AgentPath'],
                                                             testEnvironment['testUsers']['MO']['handsetID'],
                                                             response['startHTTPDownload']['downloadFile'])
                    response['downloadedFileInfo'] = downloadedFileInfoResponse

            elif (testStep == 'Wait for HTTP download completion.'):
                if (testParameters['HTTPDownload']['Duration'] > 0):
                        sleep(testParameters['HTTPDownload']['Duration'])

            else:
                failedReason = "Test step {} cannot be recognized in test case.".format(testStep)
                writeExcelFailedTestReport(failedReason, testCaseSummary, testCaseDetailList, testEnvironment,
                                           testParameters, testCaseInfo)
                assert ("Test step {} cannot be recognized in test case.".format(testStep))

            responseList.append(response)
    return responseList

def verifyTestCaseResult(testEnvironment, testParameters, testCaseInfo, testCaseKey, responseList):

    # Variables initialization.
    testResults = []
    testResult = {}


    if (testCaseKey == 'VoiceCall'):
        # Verify test case result for voice call.
        testResults = verifyVoiceCall(testEnvironment, testParameters, testCaseInfo, responseList)

    elif (testCaseKey == 'SMS'):
        # Verify test case result for SMS.
        testResults = verifySMS(testEnvironment, testParameters, testCaseInfo, responseList)

    elif (testCaseKey == 'MMS'):
        # Verify test case result for MMS.
        testResults = verifyMMS(testEnvironment, testParameters, testCaseInfo, responseList)

    elif (testCaseKey == 'WebBrowsing'):
        # Verify test case result for web browsing.
        testResults = verifyWebBrowsing(testEnvironment, testParameters, testCaseInfo, responseList)

    elif (testCaseKey == 'HTTPDownload'):
        # Verify test case result for HTTP downloading.
        testResults = verifyHTTPDownload(testEnvironment, testParameters, testCaseInfo, responseList)


    return testResults

def verifyVoiceCall(testEnvironment, testParameters, testCaseInfo, responseList):
    # Variables initialization.
    testResults = []

    # Verify result with test case check points.
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

def verifySMS(testEnvironment, testParameters, testCaseInfo, responseList):
    # Variables initialization.
    testResults = []

    # Verify result with test case check points.
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

def verifyMMS(testEnvironment, testParameters, testCaseInfo, responseList):
    # Variables initialization.
    testResults = []

    # Verify result with test case check points.
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

def verifyWebBrowsing(testEnvironment, testParameters, testCaseInfo, responseList):
    # Variables initialization.
    testResults = []

    # Verify result with test case check points.
    checkPoints = testCaseInfo['CheckPoints']
    for checkPoint in checkPoints:
        testResult = {}
        testResult['checkPointResult'] = "failed"
        verifiedCheckPointFlag = False
        if (checkPoint == 'Web browsing successfully.'):
            for response in responseList:
                if 'webBrowsing' in response:
                    testResult = verifyWebBrowsingResponse(testEnvironment, testParameters, response['webBrowsing'])
                    verifiedCheckPointFlag = True

        if (verifiedCheckPointFlag == False):
            testResult['failedReason'] = "Cannot verify this check point in test case."
            testResult['command'] = response['command']
            testResult['response'] = response['response']

        testResult['checkPoint'] = checkPoint
        testResults.append(testResult)

    return testResults

def verifyHTTPDownload(testEnvironment, testParameters, testCaseInfo, responseList):
    # Variables initialization.
    testResults = []

    # Verify result with test case check points.
    checkPoints = testCaseInfo['CheckPoints']
    for checkPoint in checkPoints:
        testResult = {}
        testResult['checkPointResult'] = "failed"
        verifiedCheckPointFlag = False
        if (checkPoint == 'HTTP download successfully.'):
            for response in responseList:
                if 'startHTTPDownload' in response:
                    testResult = verifyStartHTTPDownloadResponse(testEnvironment, testParameters, response['startHTTPDownload'])
                    verifiedCheckPointFlag = True

                if 'getDownloadedFileInfo' in response:
                    testResult = verifyDownloadedFileInfoResponse(testEnvironment, testParameters, response['downloadedFileInfo'])
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

def verifyWebBrowsingResponse(testEnvironment, testParameters, response):
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
            testResult['failedReason'] = "Failed to browse web url."
            return testResult
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."
        return testResult

    # Return result.
    return testResult

def verifyStartHTTPDownloadResponse(testEnvironment, testParameters, response):
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
            testResult['failedReason'] = "Failed to HTTP download."
            return testResult
    else:
        testResult['failedReason'] = "Cannot find 'isSuccess' in the response."
        return testResult

    # Verification for 'downloadFile'.
    if ('downloadFile' in response['response']):
        if (len(response['response']['downloadFile']) > 0):
            testResult['checkPointResult'] = "passed"
        else:
            testResult['checkPointResult'] = "failed"
            testResult['failedReason'] = "There is no 'downloadFile' value in the response."
            return testResult
    else:
        testResult['failedReason'] = "Cannot find 'downloadFile' in the response."
        return testResult

    # Return result.
    return testResult

def verifyDownloadedFileInfoResponse(testEnvironment, testParameters, response):
    # Initialization.
    testResult = {}
    testResult['checkPointResult'] = "failed"
    testResult['failedReason'] = "none"
    testResult['command'] = response['command']
    testResult['response'] = response['response']

    # Verification.
    if (len(response['response']) == 8):
        fileSize = response['response'][4]
        filePath = response['response'][-1]
        if ((fileSize > 0) and (len(filePath) > 0)):
            testResult['checkPointResult'] = "passed"
    else:
        testResult['failedReason'] = "Incorrect response length of checking download file info."
        return testResult

    # Return result.
    return testResult





