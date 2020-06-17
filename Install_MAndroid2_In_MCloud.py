import requests
import json


# Define basic information on MCloud.
mcloudBaseUrl = "http://mcloud.matrium.com.au:7100/api/v1"
mcloudLoginUser = "Peter.Zhang@matrium.com.au"
mcloudLoginToken = "Bearer 6fc22b08ce00468fa56cc53a22384012e16d1ac9ab12403abeaaa5e14496239e"


def _url(path):
    return mcloudBaseUrl + path

def listAllAvailableDevices(testUser):
    # Initialization.
    availableDeviceList = []

    # Set authorization Token to acces mCloud through REST API.
    headers = {"Authorization": mcloudLoginToken}

    # Call REST API to get the devices list on mcloud.
    print("##########Calling REST API to get devices list on MCloud.")
    resp = requests.get(_url('/devices'),
                        headers=headers)
    print(_url('/devices'))
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

            if ((device["present"] == True) and (device["ready"] == True) and (
                    (device["owner"] == None) or (device["owner"]["email"] == testUser)) and (
                    device["phone"]["imsi"] != None) and (phoneNumber != None) and (
                    device["phone"]["network"] != "UNKNOWN")):
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
        print('[!] HTTP {0} calling [{1}]'.format(_url('/devices')))
        return None

if __name__ == '__main__':
    availableDeviceList = listAllAvailableDevices(mcloudLoginUser)
    print(len(availableDeviceList))
    print (availableDeviceList)