# -*- coding:utf-8 -*-
import json
import sys
from os import listdir

import yaml
from yaml.scanner import ScannerError
import os


def getYam(path):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.safe_load(f)
            print (x)
            return [True, x]

    except FileNotFoundError:
        print("==Test Case configuration file not exit!==")
        return [False, {}]

    except yaml.scanner.ScannerError:
        print("==Test case configuration file format error==")
        return [False, {}]

def getAllConfigureInfo(configurePath, name):
    # Initialization.
    parametersList = []

    # Check all configure files.
    configurationFileList = listdir(configurePath)
    assert (len(configurationFileList) != 0)

    # Get all test data list from configuration files.
    for filename in configurationFileList:
        testDataPath = configurePath + filename
        yaml = getYam(testDataPath)

        if (yaml[0] == False):
            print("Failed to read test configuration yaml file {} from {}".format(filename, testDataPath))
            sys.exit("Failed to read test configuration yaml file {} from {}".format(filename, testDataPath))
        else:
            print("Read test configuration yaml file {} from {} successfully.".format(filename, testDataPath))
            assert (name in yaml[1])
            print("{}: {}".format(name, yaml[1][name]))
            parametersList.append(yaml[1][name])

    return parametersList

def getConfigureInfo(fileName, keyName):

    # Get specified configure info from configuration files.
    yaml = getYam(fileName)

    if (yaml[0] == False):
        print("Failed to read test configuration yaml file {}".format(fileName))
        sys.exit("Failed to read test configuration yaml file {}".format(fileName))
    else:
        print("Read test configuration yaml file {} successfully.".format(fileName))
        assert keyName in yaml[1], "Cannot find {} in {}.".format(keyName, fileName)

    return yaml[1][keyName]


if __name__ == '__main__':
    import os

    RELPATH = lambda p: os.path.relpath(
        os.path.join(os.path.dirname(__file__), p)
    )

    path = RELPATH("../configuration/testUsers/testUser1.yaml")
    print(path)
    Info = getYam(path)
    print(Info)

    # port = str(random.randint(4700, 4900))
    # bpport = str(random.randint(4700, 4900))
    # devices = "DU2TAN15AJ049163"
    #
    # cmd1 = "appium --session-override  -p %s -bp %s -U %s" % (port, bpport, devices)
    # print(cmd1)
    # os.popen(cmd1)
