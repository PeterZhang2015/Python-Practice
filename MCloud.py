import sys
import os
import requests
import json
import time
import subprocess


class MCloudControl(object):
    # Define basic information on MCloud.
    mcloud_rest_api_base = "http://mcloud.matrium.com.au:7100/api/v1"
    mcloud_login_user_email = "Peter.Zhang@matrium.com.au"
    mcloud_token = "Bearer 6fc22b08ce00468fa56cc53a22384012e16d1ac9ab12403abeaaa5e14496239e"
    deviceSerialList = []

    def _url(self, path):
        return self.mcloud_rest_api_base + path

    def requestDevice(self, deviceSerial):

        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloud_token, "Content-Type": "application/json"}
        # Set device serial as the REST API POST body.
        data = {"serial": deviceSerial}

        # Call REST API to use the device on mcloud.
        print("##########Calling REST API to use device {} on MCloud.".format(deviceSerial))
        resp = requests.post(self._url('/user/devices'),
                             headers=headers,
                             data=json.dumps(data),)

        print (self._url('/user/devices'))

        if resp.status_code == 200:
            # Check REST API response.
            dictResponse = json.loads(resp.content)
            print(dictResponse)

            self.deviceSerialList.append(deviceSerial)

            return True
        else:
            print('[!] HTTP {0} calling [{1}]'.format(resp.status_code, self._url('/user/devices')))
            return False



    def remoteConnect(self, deviceSerial):
        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloud_token, "Content-Type": "application/json"}
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
        headers = {"Authorization": self.mcloud_token}

        # Call REST API to release the use of the testing device.
        print("##########Calling REST API to release device {} on MCloud.".format(deviceSerial))
        resp = requests.delete(self._url('/user/devices/' + deviceSerial),
                             headers=headers)
        print(self._url('/user/devices/' + deviceSerial))

        if resp.status_code == 200:
            # Check REST API response.
            dictResponse = json.loads(resp.content)
            print(dictResponse)
            return True
        else:
            print('[!] HTTP {0} calling [{1}]'.format(self._url('/user/devices/' + deviceSerial)))
            return False


    def getDeviceSerialByImsi(self, userIMSI):
        # Initialize return value.
        device_serial = None

        # Set authorization Token to acces mCloud through REST API.
        headers = {"Authorization": self.mcloud_token}

        # Call REST API to get the devices list on mcloud.
        print("##########Calling REST API to get devices list on MCloud.")
        resp = requests.get(self._url('/devices'),
                             headers=headers)

        print (self._url('/devices'))
        dictResponse = json.loads(resp.content)
        print(dictResponse)

        if resp.status_code == 200:
            # Check REST API response.
            # Get device list from response body.
            devices_list = dictResponse['devices']

            # Check whether any handset is connected on mcloud.
            if (len(devices_list) == 0):
                raise SystemExit("There is not handset connected to the mcloud.")

            # Loop to check the device that can be matched with the testing user IMSI.
            for device in devices_list:
                # Only check the present handsets.
                if ((device['present'] != True) or (device['phone']['imsi'] == None)):
                    continue

                # Get the device serial of the matched IMSI.
                if (device['phone']['imsi'] == userIMSI):
                    device_serial = device['serial']
                    break

            # Check that whether the device has been occupied by someone else
            if (device['owner'] != None):
                current_device_owner_email = device['owner']['email']

            if (device['owner'] == None):
                print("Handset with IMSI {} has not been occupied.".format(userIMSI))

            elif (current_device_owner_email == self.mcloud_login_user_email):
                self.releaseDevice(device_serial)
                print("Handset with IMSI {} has been occupied by myself {}.".format(userIMSI,
                                                                                    self.mcloud_login_user_email))

            else:
                print("Handset with IMSI {} has been occupied by mcloud user {}.".format(userIMSI,
                                                                                         device['owner']['email']))
                return None

            return device_serial
        else:
            print('[!] HTTP {0} calling [{1}]'.format(self._url('/devices')))
            return None



    def connectToMcloudUser(self, userIMSI):
        # Try to find the device serial of the matched IMSI.
        device_serial = self.getDeviceSerialByImsi(userIMSI)

        if (device_serial == None):
            print ("Cannot find the matched IMSI {} on mcloud".format(userIMSI))
            return None
        else:
            print("Find the matched IMSI {} on mcloud".format(userIMSI))

        # Use the device on mcloud.
        result = self.requestDevice(device_serial)
        if (result == False):
            print("Failed to use the device {} on mcloud.".format(device_serial))
            return None

        # Get the device remote control url.
        resp = self.remoteConnect(device_serial)
        # Abort the execution if failed to call the API.
        if (resp == None):
            print ("Fail to remoteConnect {} on mcloud".format(userIMSI))
            return None

        dictResponse = json.loads(resp.content)

        # Abort the execution if it cannot get the remote control url of the testing device.
        if (dictResponse['success'] != True):
            print ("Fail to remoteConnect {} on mcloud".format(userIMSI))
            return None
        else:
            print ("connect {} on mcloud successfully".format(userIMSI))

        # ADB connect to the device on mCloud.
        process = subprocess.Popen(['adb', 'connect', dictResponse['remoteConnectUrl']],
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        print ("remoteConnectUrl is ", dictResponse['remoteConnectUrl'])

        return dictResponse['remoteConnectUrl']

    def tearDownUsingDevices(self, deviceSerialList):
        # release all used devices.
        for device_serial in deviceSerialList:
            print ("released device_serial is {}".format(device_serial))
            result = self.releaseDevice(device_serial)
            if (result == False):
                sys.exit("Failed to release device ", device_serial)

        # ADB disconnect to all devices.
        subprocess.call("adb disconnect")

if __name__ == '__main__':
    testIMSI = '505025504563848'
    mcloud = MCloudControl()
    handset_id = mcloud.connectToMcloudUser(testIMSI)

    time.sleep (5)
    mcloud.tearDownUsingDevices(mcloud.deviceSerialList)



