# -*- coding: utf-8 -*-
from selenium import webdriver

import time
import re
import sys


src_language_detected = "Chinese - detected"

src_language = re.search(r'(.*)( - detected)', src_language_detected).group(0)

print src_language

src_language = re.search(r'(.*)( - detected)', src_language_detected).group(1)




print src_language