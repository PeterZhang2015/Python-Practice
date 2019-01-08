# -*- coding: utf-8 -*-
from selenium import webdriver

import time
import re
import sys
import json

try:
  import crypto
except ImportError:
    print("Not installed.")
else:
    print("Installed.")

result = {
  "largest_value": "22",
  "type": "test"
}

largest_value = result["largest_value"]
print largest_value
type = result["type"]
print type

# json_str = json.dumps(result)
# print json_str
# largest_value = json_str["largest_value"]
# print largest_value

inputList = [5,2,7,2,1,8,3,2,4,6,7]
inputList = " ".join([str(i) for i in inputList])
#inputList = " ".join(map(str, inputList))
print inputList


# src_language_detected = "Chinese - detected"
#
# src_language = re.search(r'(.*)( - detected)', src_language_detected).group(0)
#
# print src_language
#
# src_language = re.search(r'(.*)( - detected)', src_language_detected).group(1)
#
#
# print src_language