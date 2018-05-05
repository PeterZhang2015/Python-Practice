from selenium import webdriver

import time
import sys
import Selenium2Library
import json, ast
import re

#Set testing url
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



n = '{"_index": "report-v700-2018.03.16-000029",\n  "_type": "report",\n  "_id": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n  "_version": 6,\n  "_score": null,\n  "_source": {\n    "agentHost": "192.168.32.1",\n    "agentId": "4f2c40c2-4ebf-4056-b5d3-c0be21df5285",\n    "agentName": "Peter-Zhang",\n    "callbackURL": null,\n    "createTime": 1525393698190,\n    "detailLevel": "ALL_ISSUES_ALL_STEPS",\n    "dispatchTime": "1525393698442",\n    "domain": "ldap",\n    "endTime": "1525393698943",\n    "executionLastUnsatisfiedCondition": "CAN_EXECUTE",\n    "failureReason": null,\n    "fsIdentifier": null,\n    "ignoredRequirements": [],\n    "discardReport": false,\n    "latestUpdateTime": "1525393698960",\n    "mergedRequirements": [\n      {\n        "name": "language",\n        "value": "itest"\n      }\n    ],\n    "oldPk": 0,\n    "parameterFilePath": "main/d_Base/parameter_files/parameters.ffpt",\n    "parameters": [],\n    "parentReportId": null,\n    "parentStepIndex": null,\n    "percentageComplete": "100.0",\n    "reportFileCompressionType": "NONE",\n    "reportFileSource": "ELASTIC",\n    "reportFormat": "NONE",\n    "reportId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "reportIdPath": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "reportVersion": "7.0",\n    "requirements": [],\n    "reservationId": null,\n    "result": "PASS",\n    "runlistGuid": null,\n    "runlistItemId": null,\n    "runlistPath": null,\n    "sessionId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "startTime": "1525393698520",\n    "status": "COMPLETED",\n    "tags": [],\n    "testCategory": "STANDARD",\n    "testId": null,\n    "testPath": "main/Temp/test_cases/temp.fftc",\n    "token": null,\n    "topologyId": null,\n    "topologyName": null,\n    "topologyPath": null,\n    "topologyReservationId": null,\n    "topologyVersionId": null,\n    "userId": "peter",\n    "isRunlistFirst": false,\n    "isReservationBySvc": "false",\n    "isRunlistLast": false\n  },\n  "fields": {\n    "dispatchTime": [\n      1525393698442\n    ],\n    "createTime": [\n      1525393698190\n    ],\n    "latestUpdateTime": [\n      1525393698960\n    ],\n    "startTime": [\n      1525393698520\n    ],\n    "endTime": [\n      1525393698943\n    ]\n  },\n  "sort": [\n    1525393698520\n  ]\n}'
print ("***********n*************8")
print (n)

data = json.loads(n)
index = data["_source"]["testPath"]
print ("***********index*************8")
print (index)


#json_information_text = 'u\'{\\n  "_index": "report-v700-2018.03.16-000029",\\n  "_type": "report",\\n  "_id": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\\n  "_version": 6,\\n  "_score": null,\\n  "_source": {\\n    "agentHost": "192.168.32.1",\\n    "agentId": "4f2c40c2-4ebf-4056-b5d3-c0be21df5285",\\n    "agentName": "Peter-Zhang",\\n    "callbackURL": null,\\n    "createTime": 1525393698190,\\n    "detailLevel": "ALL_ISSUES_ALL_STEPS",\\n    "dispatchTime": "1525393698442",\\n    "domain": "ldap",\\n    "endTime": "1525393698943",\\n    "executionLastUnsatisfiedCondition": "CAN_EXECUTE",\\n    "failureReason": null,\\n    "fsIdentifier": null,\\n    "ignoredRequirements": [],\\n    "discardReport": false,\\n    "latestUpdateTime": "1525393698960",\\n    "mergedRequirements": [\\n      {\\n        "name": "language",\\n        "value": "itest"\\n      }\\n    ],\\n    "oldPk": 0,\\n    "parameterFilePath": "main/d_Base/parameter_files/parameters.ffpt",\\n    "parameters": [],\\n    "parentReportId": null,\\n    "parentStepIndex": null,\\n    "percentageComplete": "100.0",\\n    "reportFileCompressionType": "NONE",\\n    "reportFileSource": "ELASTIC",\\n    "reportFormat": "NONE",\\n    "reportId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\\n    "reportIdPath": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\\n    "reportVersion": "7.0",\\n    "requirements": [],\\n    "reservationId": null,\\n    "result": "PASS",\\n    "runlistGuid": null,\\n    "runlistItemId": null,\\n    "runlistPath": null,\\n    "sessionId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\\n    "startTime": "1525393698520",\\n    "status": "COMPLETED",\\n    "tags": [],\\n    "testCategory": "STANDARD",\\n    "testId": null,\\n    "testPath": "main/Temp/test_cases/temp.fftc",\\n    "token": null,\\n    "topologyId": null,\\n    "topologyName": null,\\n    "topologyPath": null,\\n    "topologyReservationId": null,\\n    "topologyVersionId": null,\\n    "userId": "peter",\\n    "isRunlistFirst": false,\\n    "isReservationBySvc": "false",\\n    "isRunlistLast": false\\n  },\\n  "fields": {\\n    "dispatchTime": [\\n      1525393698442\\n    ],\\n    "createTime": [\\n      1525393698190\\n    ],\\n    "latestUpdateTime": [\\n      1525393698960\\n    ],\\n    "startTime": [\\n      1525393698520\\n    ],\\n    "endTime": [\\n      1525393698943\\n    ]\\n  },\\n  "sort": [\\n    1525393698520\\n  ]\\n}\''
#insert_field = '"testCustomedField": "test",\\n    '
#m = re.sub(r'(.*)("agentId":)', r'\1{}\2'.format(insert_field), json_information_text)
#print (m)

#json_information_text = 'u\'{\n  "_index": "report-v700-2018.03.16-000029",\n  "_type": "report",\n  "_id": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n  "_version": 6,\n  "_score": null,\n  "_source": {\n    "agentHost": "192.168.32.1",\n    "agentId": "4f2c40c2-4ebf-4056-b5d3-c0be21df5285",\n    "agentName": "Peter-Zhang",\n    "callbackURL": null,\n    "createTime": 1525393698190,\n    "detailLevel": "ALL_ISSUES_ALL_STEPS",\n    "dispatchTime": "1525393698442",\n    "domain": "ldap",\n    "endTime": "1525393698943",\n    "executionLastUnsatisfiedCondition": "CAN_EXECUTE",\n    "failureReason": null,\n    "fsIdentifier": null,\n    "ignoredRequirements": [],\n    "discardReport": false,\n    "latestUpdateTime": "1525393698960",\n    "mergedRequirements": [\n      {\n        "name": "language",\n        "value": "itest"\n      }\n    ],\n    "oldPk": 0,\n    "parameterFilePath": "main/d_Base/parameter_files/parameters.ffpt",\n    "parameters": [],\n    "parentReportId": null,\n    "parentStepIndex": null,\n    "percentageComplete": "100.0",\n    "reportFileCompressionType": "NONE",\n    "reportFileSource": "ELASTIC",\n    "reportFormat": "NONE",\n    "reportId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "reportIdPath": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "reportVersion": "7.0",\n    "requirements": [],\n    "reservationId": null,\n    "result": "PASS",\n    "runlistGuid": null,\n    "runlistItemId": null,\n    "runlistPath": null,\n    "sessionId": "8778ac27-1cac-4f86-8a87-0b9fb4df1242",\n    "startTime": "1525393698520",\n    "status": "COMPLETED",\n    "tags": [],\n    "testCategory": "STANDARD",\n    "testId": null,\n    "testPath": "main/Temp/test_cases/temp.fftc",\n    "token": null,\n    "topologyId": null,\n    "topologyName": null,\n    "topologyPath": null,\n    "topologyReservationId": null,\n    "topologyVersionId": null,\n    "userId": "peter",\n    "isRunlistFirst": false,\n    "isReservationBySvc": "false",\n    "isRunlistLast": false\n  },\n  "fields": {\n    "dispatchTime": [\n      1525393698442\n    ],\n    "createTime": [\n      1525393698190\n    ],\n    "latestUpdateTime": [\n      1525393698960\n    ],\n    "startTime": [\n      1525393698520\n    ],\n    "endTime": [\n      1525393698943\n    ]\n  },\n  "sort": [\n    1525393698520\n  ]\n}\''
json_information_text = u'{\n  "_index": "report-v700-2018.03.16-000030",\n  "_type": "report",\n  "_id": "1dc9ff38-c52d-4553-a69a-b7194aec9586",\n  "_version": 6,\n  "_score": null,\n  "_source": {\n    "agentHost": "192.168.32.1",\n    "agentId": "4f2c40c2-4ebf-4056-b5d3-c0be21df5285",\n    "agentName": "Peter-Zhang",\n    "callbackURL": null,\n    "createTime": 1525411213348,\n    "detailLevel": "ALL_ISSUES_ERROR_STEPS",\n    "dispatchTime": "1525411213628",\n    "domain": "ldap",\n    "endTime": "1525411227046",\n    "executionLastUnsatisfiedCondition": "CAN_EXECUTE",\n    "failureReason": null,\n    "fsIdentifier": null,\n    "ignoredRequirements": [],\n    "discardReport": false,\n    "latestUpdateTime": "1525411227191",\n    "mergedRequirements": [\n      {\n        "name": "language",\n        "value": "itest"\n      }\n    ],\n    "oldPk": 0,\n    "parameterFilePath": "main/d_Base/parameter_files/parameters.ffpt",\n    "parameters": [],\n    "parentReportId": null,\n    "parentStepIndex": null,\n    "percentageComplete": "100.0",\n    "reportFileCompressionType": "NONE",\n    "reportFileSource": "ELASTIC",\n    "reportFormat": "NONE",\n    "reportId": "1dc9ff38-c52d-4553-a69a-b7194aec9586",\n    "reportIdPath": "1dc9ff38-c52d-4553-a69a-b7194aec9586",\n    "reportVersion": "7.0",\n    "requirements": [],\n    "reservationId": null,\n    "result": "PASS",\n    "runlistGuid": null,\n    "runlistItemId": null,\n    "runlistPath": null,\n    "sessionId": "1dc9ff38-c52d-4553-a69a-b7194aec9586",\n    "startTime": "1525411213599",\n    "status": "COMPLETED",\n    "tags": [],\n    "testCategory": "STANDARD",\n    "testId": null,\n    "testPath": "main/TAAS/test_cases/TAAS-2~getHandsetInfo.fftc",\n    "token": null,\n    "topologyId": null,\n    "topologyName": null,\n    "topologyPath": null,\n    "topologyReservationId": null,\n    "topologyVersionId": null,\n    "userId": "peter",\n    "isRunlistFirst": false,\n    "isReservationBySvc": "false",\n    "isRunlistLast": false\n  },\n  "fields": {\n    "dispatchTime": [\n      1525411213628\n    ],\n    "createTime": [\n      1525411213348\n    ],\n    "latestUpdateTime": [\n      1525411227191\n    ],\n    "startTime": [\n      1525411213599\n    ],\n    "endTime": [\n      1525411227046\n    ]\n  },\n  "sort": [\n    1525411213599\n  ]\n}'


print ("**********json_information_text**************8")
print (json_information_text)

insert_field = '"testCustomedField": "test",\\n    '
m = re.sub(r'(.*)("agentId":)', r'\1{}\2'.format(insert_field), json_information_text)

print ("***********POST body*************8")
print (m)

temp_data = json.loads(m)

json_source = temp_data["_source"]
#json_source = json_source.encode("ascii", "replace")
json_source = json.dumps(json_source)
print ("***********json_source*************8")
print (json_source)



