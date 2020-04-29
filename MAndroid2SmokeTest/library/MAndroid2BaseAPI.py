import json
import subprocess
import sys
from os import listdir

import xlsxwriter
import os
from datetime import datetime
from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MAndroid2SmokeTest.library.MAndroid2BaseMCloud import MCloudControl

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

PLACE_VOICE_CALL_CODE = '3010'
RECEIVE_VOICE_CALL_CODE = '3011'
END_VOICE_CALL_CODE = '3012'
GET_MANDROID2_VERSION_CODE = '9001'
GET_MANDROID2_AGENT_VERSION_CODE = '9002'
GET_MANDROID2_PLUGIN_VERSION_CODE = '9003'

def getMAndroid2Version(MAndroid2AgentPath, handsetId):
    # Initialization
    version = {}

    # Construct command
    command = "java -jar {} {} {}".format(MAndroid2AgentPath,
                                          handsetId,
                                          GET_MANDROID2_VERSION_CODE)
    # Execute command
    response = json.loads(subprocess.check_output(command.split()))
    assert ('version' in response)

    # Record version info
    version['MAndroid2'] = response['version']

    # Construct command
    command = "java -jar {} {} {}".format(MAndroid2AgentPath,
                                          handsetId,
                                          GET_MANDROID2_AGENT_VERSION_CODE)
    # Execute command
    response = json.loads(subprocess.check_output(command.split()))
    assert ('version' in response)

    # Record version info
    version['MAndroid2Agent'] = response['version']

    # Construct command
    command = "java -jar {} {} {}".format(MAndroid2AgentPath,
                                          handsetId,
                                          GET_MANDROID2_PLUGIN_VERSION_CODE)
    # Execute command
    response = json.loads(subprocess.check_output(command.split()))
    assert ('version' in response)

    # Record version info
    version['MAndroid2Plugin'] = response['version']

    return version

def placeBasicVoiceCall(MAndroid2AgentPath, handsetId, calledUserNumber):

    # Initialization
    dicResponse = {}

    # Construct command
    command = "java -jar {} {} {} call_phonenum {}".format(MAndroid2AgentPath,
                                                                         handsetId,
                                                                         PLACE_VOICE_CALL_CODE,
                                                                         calledUserNumber)
    print("Command of placing basic voice call is: ", command)
    # response = os.system(placeVoiceCallCommand)

    # process = subprocess.Popen(['java', '-jar', MAndroid2AgentPath, handsetId, PLACE_VOICE_CALL_CODE, 'call_phonenum', calledUserNumber],
    #                            stdout=subprocess.PIPE,
    #                            universal_newlines=True)
    # response = process.communicate()[0]

    # response = subprocess.check_output(['java', '-jar', MAndroid2AgentPath, handsetId, PLACE_VOICE_CALL_CODE, 'call_phonenum', calledUserNumber])

    # Execute command
    response = subprocess.check_output(command.split())
    print("Response of placing basic voice call is: ", json.loads(response))

    # Record command and response
    dicResponse['command'] = command
    dicResponse['response'] = json.loads(response)

    return dicResponse

def receiveBasicVoiceCall(MAndroid2AgentPath, handsetId):

    # Initialization
    dicResponse = {}

    # Construct command
    command = "java -jar {} {} {} ".format(MAndroid2AgentPath,
                                                           handsetId,
                                                           RECEIVE_VOICE_CALL_CODE)
    print("Command of receiving basic voice call is: ", command)

    # Execute command
    response = subprocess.check_output(command.split())
    print("Response of receiving basic voice call is: ", json.loads(response))

    # Record command and response
    dicResponse['command'] = command
    dicResponse['response'] = json.loads(response)

    return dicResponse

def endBasicVoiceCall(MAndroid2AgentPath, handsetId):

    # Initialization
    dicResponse = {}

    # Construct command
    command = "java -jar {} {} {}".format(MAndroid2AgentPath,
                                                          handsetId,
                                                          END_VOICE_CALL_CODE)
    print("Command of receiving basic voice call is: ", command)

    # Execute command
    response = subprocess.check_output(command.split())
    print("Response of ending basic voice call is: ", json.loads(response))

    # Record command and response
    dicResponse['command'] = command
    dicResponse['response'] = json.loads(response)

    return dicResponse


