import sys
import os
import requests
import json
import time
import subprocess
import re

from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getConfigureInfo

class MCloudControl(object):
    # Define basic information on MCloud.
    mcloudBaseUrl = "http://mcloud.matrium.com.au:7100/api/v1"
    mcloudLoginUser = "Peter.Zhang@matrium.com.au"
    mcloudLoginToken = "Bearer 6fc22b08ce00468fa56cc53a22384012e16d1ac9ab12403abeaaa5e14496239e"
    deviceSerialList = []

    # testEnvironmentPath = "../configuration/testEnvironment/"
    # testEnvironmentName = "testEnvironment"
    # testEnvironment = getConfigureInfo(testEnvironmentPath, testEnvironmentName)
    # mcloudBaseUrl = testEnvironment['MCloud']['baseUrl']
    # mcloudLoginToken = testEnvironment['MCloud']['accessToken']
    # mcloudLoginUser = testEnvironment['tester']
    # deviceSerialList = []

    def _url(self, path):
        return self.mcloudBaseUrl + path

    def requestDevice(self, deviceSerial):

        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken, "Content-Type": "application/json"}
        # Set device serial as the REST API POST body.
        data = {"serial": deviceSerial}

        # Call REST API to use the device on mcloud.
        print("##########Calling REST API to use device {} on MCloud.".format(deviceSerial))
        resp = requests.post(self._url('/user/devices'),
                             headers=headers,
                             data=json.dumps(data),)

        print (self._url('/user/devices'))
        print(json.dumps(data))
        print(headers)
        print(resp)

        if resp.status_code == 200:
            # Check REST API response.
            dictResponse = json.loads(resp.content)
            print(dictResponse)

            self.deviceSerialList.append(deviceSerial)
            print("Adding {} to deviceSerialList".format(deviceSerial))

            return True
        else:
            print('[!] HTTP {0} calling [{1}]'.format(resp.status_code, self._url('/user/devices')))
            return False



    def remoteConnect(self, deviceSerial):
        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken, "Content-Type": "application/json"}
        # Set device serial as the REST API POST body.
        data = {"serial": deviceSerial}

        # Call REST API to get the remote debug URL of the testing device for further adb control.
        print("##########Calling REST API to get the remote debug URL of the testing device {} on MCloud.".format(deviceSerial))
        resp = requests.post(self._url('/user/devices/{}/remoteConnect'.format(deviceSerial)),
                             data=json.dumps(data),
                             headers=headers)

        print(self._url('/user/devices/{}/remoteConnect'.format(deviceSerial)))

        if resp.status_code == 200:
            # Check REST API response.
            dictResponse = json.loads(resp.content)
            print(dictResponse)
            return resp
        else:
            print('[!] HTTP {0} calling [{1}]'.format(self._url('/user/devices/{}/remoteConnect'.format(deviceSerial))))
            return None



    def releaseDevice(self, deviceSerial):
        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken}

        # Call REST API to release the use of the testing device.
        print("##########Calling REST API to release device {} on MCloud.".format(deviceSerial))
        resp = requests.delete(self._url('/user/devices/' + deviceSerial),
                             headers=headers)
        print(self._url('/user/devices/' + deviceSerial))
        print("resp.status_code is {}".format(resp.status_code))

        if resp.status_code == 200:
            # Check REST API response.
            dictResponse = json.loads(resp.content)
            print(dictResponse)
            if (deviceSerial in self.deviceSerialList):
                self.deviceSerialList.remove(deviceSerial)
            return True
        else:
            print('[!] HTTP {0} calling [{1}]'.format(self._url('/user/devices/' + deviceSerial)))
            return False

    def listDevices(self):
        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken}

        # Call REST API to get the devices list on mcloud.
        print("##########Calling REST API to get devices list on MCloud.")
        resp = requests.get(self._url('/devices'),
                             headers=headers)
        print (self._url('/devices'))
        dictResponse = json.loads(resp.content)
        # print(dictResponse)

        if resp.status_code == 200:
            return dictResponse['devices']
        else:
            print('[!] HTTP {0} calling [{1}]'.format(self._url('/devices')))
            return None

    def listAllAvailableDevices(self, testUser):
        # Initialization.
        availableDeviceList = []

        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken}

        # Call REST API to get the devices list on mcloud.
        print("##########Calling REST API to get devices list on MCloud.")
        resp = requests.get(self._url('/devices'),
                            headers=headers)
        print(self._url('/devices'))
        dictResponse = json.loads(resp.content)
        # print(dictResponse)

        if resp.status_code == 200:
            # Check REST API response.
            # Get device list from response body.
            devicesList = dictResponse['devices']

            # Check whether any handset is connected on mcloud.
            if (len(devicesList) == 0):
                print('There is no handset connected to the mcloud.')
                return None

            # Loop to check the device that can be matched with the testing user IMSI.
            for device in devicesList:
                # Only check the present handsets.
                phoneNumber = device["phone"]["phoneNumber"]
                if (phoneNumber == None) and ("notes" in device) and (device["notes"] != ""):
                    phoneNumber = device["notes"]

                # if ((device["present"] == True) and (device["ready"] == True) and (
                #         (device["owner"] == None) or (device["owner"]["email"] == testUser)) and (
                #         device["phone"]["imsi"] != None) and (phoneNumber != None) and (
                #         device["phone"]["network"] != "UNKNOWN")):
                if ((device["present"] == True) and (device["ready"] == True) and (
                        (device["owner"] == None) or (device["owner"]["email"] == testUser))
                        and (device["serial"] != None)
                        and (phoneNumber != None) and (device["phone"]["network"] != "UNKNOWN")):
                    availableDevice = {}
                    availableDevice["serial"] = device["serial"]
                    availableDevice["imsi"] = device["phone"]["imsi"]
                    availableDevice["phoneNumber"] = phoneNumber
                    availableDeviceList.append(availableDevice)

            if (len(availableDeviceList) == 0):
                print('There is no available device on MCloud.')
                return None
            else:
                return availableDeviceList
        else:
            print('[!] HTTP {0} calling [{1}]'.format(resp.status_code, self._url('/devices')))
            return None

    def getDeviceSerialByImsi(self, userIMSI):
        # Initializaation.
        result = {}
        result['failedFlag'] = False
        result['failedReason'] = None
        result['deviceSerial'] = None

        # Initialize return value.
        deviceSerial = None

        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloudLoginToken}

        # Call REST API to get the devices list on mcloud.
        print("##########Calling REST API to get devices list on MCloud.")
        resp = requests.get(self._url('/devices'),
                             headers=headers)

        print (self._url('/devices'))
        dictResponse = json.loads(resp.content)
        # print(dictResponse)

        if resp.status_code == 200:
            # Check REST API response.
            # Get device list from response body.
            devicesList = dictResponse['devices']

            # Check whether any handset is connected on mcloud.
            if (len(devicesList) == 0):
                result['failedFlag'] = True
                result['failedReason'] = "There is no handset connected to the mcloud."
                print(result['failedReason'])
                return result
            # Loop to check the device that can be matched with the testing user IMSI.
            for device in devicesList:
                # Only check the present handsets.
                if ((device['present'] != True) or (device['phone']['imsi'] == None)):
                    continue

                # Get the device serial of the matched IMSI.
                if (device['phone']['imsi'] == userIMSI):
                    deviceSerial = device['serial']
                    break


            if (deviceSerial) == None:
                result['failedFlag'] = True
                result['failedReason'] = "There is no device that can be matched with the testing user IMSI."
                print(result['failedReason'])

                return result

            # Check that whether the device has been occupied by someone else
            if (device['owner'] != None):
                currentDeviceOwner = device['owner']['email']

            if (device['owner'] == None):
                print("Handset with IMSI {} has not been occupied.".format(userIMSI))
                print("Corresponding device serial is {}.".format(deviceSerial))

            elif (currentDeviceOwner == self.mcloudLoginUser):
                self.releaseDevice(deviceSerial)
                print("Handset with IMSI {} has been occupied by myself {}.".format(userIMSI,
                                                                                    self.mcloudLoginUser))

            else:
                result['failedFlag'] = True
                result['failedReason'] = "Handset with IMSI {} has been occupied by mcloud user {}.".format(userIMSI, device['owner']['email'])
                print(result['failedReason'])

                return result

            result['deviceSerial'] = deviceSerial
            return result
        else:

            result['failedFlag'] = True
            result['failedReason'] = '[!] HTTP {0} calling [{1}]'.format(self._url('/devices'))
            print(result['failedReason'])

            return result

    def connectToMcloudUser(self, userSerial):
        # Initializaation.
        result = {}
        result['failedFlag'] = False
        result['failedReason'] = None
        result['remoteConnectUrl'] = None

        # # Try to find the device serial of the matched IMSI.
        # resultGetDeviceSerialByImsi = self.getDeviceSerialByImsi(userIMSI)
        #
        # if (resultGetDeviceSerialByImsi['failedFlag'] == True or resultGetDeviceSerialByImsi['deviceSerial'] == None):
        #     result['failedFlag'] = True
        #     result['failedReason'] = "Cannot find the matched IMSI {} on mcloud".format(userIMSI)
        #     print(result['failedReason'])
        #     return result
        # else:
        #     print("Find the matched IMSI {} on mcloud".format(userIMSI))

        # Use the device on mcloud.
        resultRequestDevice = self.requestDevice(userSerial)
        if (resultRequestDevice == False):
            # Trying to release and request the occupied device.
            resultReleaseDevice = self.releaseDevice(userSerial)
            if (resultReleaseDevice == False):
                result['failedFlag'] = True
                result['failedReason'] = "Failed to release occupied device {} on mcloud.".format(userSerial)
                print(result['failedReason'])
                return result

            resultRequestDevice = self.requestDevice(userSerial)
            if (resultRequestDevice == False):
                result['failedFlag'] = True
                result['failedReason'] = "Failed to use the device {} on mcloud.".format(userSerial)
                print(result['failedReason'])
                return result

        # Get the device remote control url.
        resp = self.remoteConnect(userSerial)
        # Abort the execution if failed to call the API.
        if (resp == None):
            result['failedFlag'] = True
            result['failedReason'] = "Fail to remoteConnect {} on mcloud".format(userSerial)
            print(result['failedReason'])
            return result

        dictResponse = json.loads(resp.content)

        # Abort the execution if it cannot get the remote control url of the testing device.
        if (dictResponse['success'] != True):
            result['failedFlag'] = True
            result['failedReason'] = "Fail to remoteConnect {} on mcloud according to response".format(userSerial)
            print(result['failedReason'])
            return result
        else:
            print ("connect {} on mcloud successfully".format(userSerial))
            print ("remoteConnectUrl is ", dictResponse['remoteConnectUrl'])

        # adb connect
        command = "adb connect {}".format(dictResponse['remoteConnectUrl'])

        response = subprocess.check_output(command.split())
        print("Response of adb connect {} is: {}".format(dictResponse['remoteConnectUrl'], response))

        # Check adb connect result by adb devices after waiting 5 seconds.
        time.sleep(5)
        command = "adb devices"
        response = subprocess.check_output(command.split()).decode('utf-8')
        print("Response of adb devices is: {}".format(response))

        findResult = re.findall(r"(.+)\t+device", response)
        print(findResult)
        if dictResponse['remoteConnectUrl'] in findResult:
            result['remoteConnectUrl'] = dictResponse['remoteConnectUrl']
            return result
        else:
            result['failedFlag'] = True
            result['failedReason'] = "Cannot find device {} after adb connect".format(dictResponse['remoteConnectUrl'])
            print(result['failedReason'])
            return result

    def tearDownUsingDevices(self, deviceSerialList):
        # ADB disconnect to all devices.
        subprocess.call("adb disconnect")

        # release all used devices.
        tempList = deviceSerialList.copy()
        for deviceSerial in tempList:
            result = self.releaseDevice(deviceSerial)
            if (result == False):
                print("Failed to release device ", deviceSerial)
            print("Remaining released deviceSerialList is {}".format(deviceSerialList))

        # ADB disconnect to all devices.
        subprocess.call("adb disconnect")


if __name__ == '__main__':
    # testIMSI = '505025504563848'
    # mcloud = MCloudControl()
    # handset_id = mcloud.connectToMcloudUser(testIMSI)
    #
    # time.sleep (5)
    # mcloud.tearDownUsingDevices(mcloud.deviceSerialList)


    testUser = "Peter.Zhang@matrium.com.au"
    apkPath = "C://Work//Mandroid2//app-debug.apk"
    mcloud = MCloudControl()
    availableDeviceList = mcloud.listAllAvailableDevices(testUser)
    print(len(availableDeviceList))
    print("Connected handset ID: {}".format(availableDeviceList))

    for availableDevice in availableDeviceList:
        result = mcloud.connectToMcloudUser(availableDevice["serial"])
        print("Connected handset ID: {}".format(availableDeviceList))

        if result["failedFlag"] == True or result["remoteConnectUrl"] == None:
            print("Cannot connect to user: {}".format(availableDevice["imsi"]))
            continue
        else:
            handset_id = result["remoteConnectUrl"]
            # Re-install latest MAndroid2 APK.
            # Construct command
            command = "adb -s {} install -r {}".format(handset_id, apkPath)

            response = subprocess.check_output(command.split())
            print("Response of adb install for {} is: {}".format(handset_id, response))

    mcloud.tearDownUsingDevices(mcloud.deviceSerialList)


