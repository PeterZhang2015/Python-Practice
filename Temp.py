# -*- coding: utf-8 -*-
from selenium import webdriver

import time
import re
import sys

inputList = [5,2,7,2,1,8,3,2,4,6,7]
inputList = " ".join([str(i) for i in inputList])
#inputList = " ".join(map(str, inputList))
print inputList


#src_language_detected = "Chinese - detected"

#src_language = re.search(r'(.*)( - detected)', src_language_detected).group(0)

#print src_language

#src_language = re.search(r'(.*)( - detected)', src_language_detected).group(1)


#print src_language