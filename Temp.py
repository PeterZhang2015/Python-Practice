# -*- coding: utf-8 -*-
import ipaddress
import os
import subprocess
from datetime import datetime
from decimal import Decimal

from ipaddress import ip_interface, ip_network


from selenium import webdriver

import time
import re
import sys
import json

# try:
#   import crypto
# except ImportError:
#     print("Not installed.")
# else:
#     print("Installed.")
#
# result = {
#   "largest_value": "22",
#   "type": "test"
# }

# largest_value = result["largest_value"]
# print largest_value
# type = result["type"]
# print type

# json_str = json.dumps(result)
# print json_str
# largest_value = json_str["largest_value"]
# print largest_value

# inputList = [5,2,7,2,1,8,3,2,4,6,7]
# inputList = " ".join([str(i) for i in inputList])
# #inputList = " ".join(map(str, inputList))
# print inputList


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


# import datetime;
# ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# print(ts)

# import json
#
# #json.loads({"success":true,"devices":[{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":73,"scale":100,"source":"usb","status":"charging","temp":26.7,"voltage":4.037},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":true,"system":false,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":true},"channel":"mw9jfEL5+pdnvws887fgnwdiu4g=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.545Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7420","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":false,"failover":false,"roaming":false,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802093412107","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.768Z","present":false,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"1ca45f2e0e027ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.027Z","usage":null,"usageChangedAt":"2019-02-26T05:16:06.723Z","version":"8.0.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.4,"voltage":3.946},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"wTLQIlQINPTkW1GB6ZsENwG/1Vw=","cpuPlatform":"exynos5","createdAt":"2018-11-20T01:52:00.253Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":true,"size":5.059174060821533,"url":"ws://mcloud.matrium.com.au:7464","width":1440,"xdpi":580.5709838867188,"ydpi":580.5709838867188},"manufacturer":"SAMSUNG","model":"SM-G920F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"LTE","type":"MOBILE"},"notes":"","openGLESVersion":"3.1","operator":null,"owner":null,"phone":{"iccid":"8961025717529312634","imei":"358992070798372","imsi":"505025703492762","network":"HSPAP","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-04-11T23:53:03.505Z","present":false,"product":"zerofltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"031603b240b91601","status":3,"statusChangedAt":"2019-04-11T23:26:35.749Z","usage":"02:7d:cf:95:5c:1f:10:29:a3:e7:65:bb:2f:3f:db:00","usageChangedAt":"2019-04-11T23:44:21.789Z","version":"6.0.1","using":false},{"abi":"armeabi-v7a","airplaneMode":false,"battery":{"health":"good","level":98,"scale":100,"source":"usb","status":"charging","temp":32.3,"voltage":4.277},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"55Vl/Uczyzg9I8fW7iCCTCGSGeg=","cpuPlatform":"msm8974","createdAt":"2019-03-27T05:34:57.948Z","display":{"density":3,"fps":60,"height":1920,"id":0,"rotation":0,"secure":true,"size":5.200733661651611,"url":"ws://mcloud.matrium.com.au:7556","width":1080,"xdpi":422.0299987792969,"ydpi":424.0690002441406},"manufacturer":"SAMSUNG","model":"SM-G900I","network":{"connected":false,"failover":false,"roaming":false,"subtype":null,"type":null},"openGLESVersion":"3.0","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352919065742079","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-05-12T23:37:45.642Z","present":false,"product":"kltedv","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"1b88d6f0","status":3,"statusChangedAt":"2019-05-09T22:55:28.265Z","usage":null,"usageChangedAt":"2019-05-07T23:16:20.701Z","version":"6.0.1","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":78,"scale":100,"source":"usb","status":"charging","temp":26.6,"voltage":4.09},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":true,"system":false,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":true},"channel":"LdFev4vJa9NYQqvU6B7yxfsWe7U=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.553Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7412","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":false,"failover":false,"roaming":false,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802097622057","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.234Z","present":false,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"215dad1b37057ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.032Z","usage":null,"usageChangedAt":"2019-02-26T10:49:05.184Z","version":"8.0.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.8,"voltage":4.278},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"6W4ZNRI0Kc25YqbnoWaCi6j1CQM=","cpuPlatform":"exynos5","createdAt":"2019-02-20T02:45:00.723Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":true,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7612","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"optus_cx-1, rooted, +61431618629","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508284527f","imei":"358810075103309","imsi":"505025815954246","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-03-09T22:39:03.563Z","present":true,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"9886734d5647434c32","status":3,"statusChangedAt":"2020-03-09T22:39:03.563Z","usage":null,"usageChangedAt":"2020-03-12T23:46:36.816Z","version":"7.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.4,"voltage":4.301},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"jYG1N6ZysL7nwFXXjztwRRkCGkM=","cpuPlatform":"exynos5","createdAt":"2019-09-27T00:51:22.788Z","display":{"density":2.625,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":6.2156219482421875,"url":"ws://mcloud.matrium.com.au:7993","width":1080,"xdpi":397.5644836425781,"ydpi":397.09796142578125},"manufacturer":"SAMSUNG","model":"SM-G965F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"unrooted, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508284535","imei":"355893091540459","imsi":"505025815954247","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-01-16T04:06:02.523Z","present":true,"product":"star2ltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"28","serial":"216a454f17047ece","status":3,"statusChangedAt":"2020-01-16T04:06:02.524Z","usage":null,"usageChangedAt":"2020-03-12T23:46:32.347Z","version":"9","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.5,"voltage":4.357},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"IgpSNtWAWNf34ngUOek/5NoDjhg=","cpuPlatform":"exynos5","createdAt":"2018-10-15T22:34:30.995Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":true,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7572","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"","openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508230124","imei":"357350078314596","imsi":"505025815948806","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-09-18T00:26:37.299Z","present":false,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"9885e6323446425233","status":3,"statusChangedAt":"2019-09-18T00:26:20.842Z","usage":null,"usageChangedAt":"2019-09-18T00:02:04.485Z","version":"6.0.1","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":69,"scale":100,"source":"usb","status":"charging","temp":27,"voltage":4.014},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":true,"system":false,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":true},"channel":"6lFEtQjwuho4/ZqBP3Ve/j7mW38=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.554Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7404","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":false,"failover":false,"roaming":false,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802094388959","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:16.196Z","present":false,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"1cba56ef20047ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.030Z","usage":null,"usageChangedAt":"2019-02-26T05:16:24.360Z","version":"8.0.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.6,"voltage":4.308},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"+6rtoz27n+uzbDtAxmlXo2oSipw=","cpuPlatform":"exynos5","createdAt":"2019-02-06T06:25:13.157Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7608","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"rooted, +61418673947","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025114450127308","imei":"355896090403454","imsi":"505025104559746","network":"LTE","phoneNumber":"+61418673947"},"platform":"Android","presenceChangedAt":"2020-03-04T03:35:24.708Z","present":true,"product":"starltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"25cb81cc6f0d7ece","status":3,"statusChangedAt":"2020-03-04T03:35:24.708Z","usage":null,"usageChangedAt":"2020-03-12T23:46:34.034Z","version":"8.0.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.9,"voltage":4.302},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"knT0EAal7FTzNWf94cUHFsDvfxY=","cpuPlatform":"exynos5","createdAt":"2018-09-26T23:59:20.038Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":true,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7949","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"LTE","type":"MOBILE"},"notes":"rooted, +61431202671","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025515437279196f","imei":"357350078315031","imsi":"505025504563848","network":"HSPAP","phoneNumber":"+61431202671"},"platform":"Android","presenceChangedAt":"2020-02-07T05:30:11.863Z","present":true,"product":"heroltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"9885e649593651384c","status":3,"statusChangedAt":"2020-01-16T03:23:02.001Z","usage":null,"usageChangedAt":"2020-03-13T05:15:08.613Z","version":"7.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":25.9,"voltage":4.257},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"HRqE6wZ+KTQNNTBnMkeqvSTF/3Q=","cpuPlatform":"exynos5","createdAt":"2020-01-16T03:05:40.372Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7917","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"355894091494432","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-01-16T03:05:40.390Z","present":true,"product":"starltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"28","serial":"22a494180a0b7ece","status":3,"statusChangedAt":"2020-01-16T03:05:43.965Z","usage":null,"usageChangedAt":"2020-03-12T23:46:33.201Z","version":"9","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.335},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserMainActivity","name":"Browser","selected":false,"system":true,"type":"samsung-sbrowser","developer":"Samsung"},{"id":"com.android.chrome/com.google.android.apps.chrome.Main","name":"Chrome","selected":false,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":false},"channel":"2NOdXvrLVZgtSlH4vr8z9kXXry0=","cpuPlatform":"exynos5","createdAt":"2018-11-12T05:58:42.413Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":true,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7660","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":false,"failover":false,"roaming":false,"subtype":null,"type":null},"openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025717529312618","imei":"357810082504565","imsi":"505025703492760","network":"LTE","phoneNumber":"+61478101658"},"platform":"Android","presenceChangedAt":"2018-12-03T00:23:01.439Z","present":false,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"ce011711381ab4bb0c","status":3,"statusChangedAt":"2018-11-21T04:05:33.719Z","usage":null,"usageChangedAt":"2018-12-03T00:21:13.243Z","version":"6.0.1","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28,"voltage":4.308},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":true,"system":false,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":true},"channel":"8Vq0xaEvCIVMAfZB1AdrPIeeSkM=","cpuPlatform":"exynos5","createdAt":"2018-10-11T05:15:47.144Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7400","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"LTE","type":"MOBILE"},"notes":"optus_cx-2, unrooted, +61435548032, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025818539139064f","imei":"359039086085482","imsi":"505025814139700","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-11-29T06:21:08.582Z","present":false,"product":"dreamltexx","provider":{"channel":"1ccoa3ywQdWm0c1oVh2kTQ==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"ce051715b4dd583201","status":3,"statusChangedAt":"2019-11-11T02:42:48.405Z","usage":null,"usageChangedAt":"2019-11-22T03:15:34.379Z","version":"7.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":17.6,"voltage":4.3},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"iGSoZn6fI6HOR37o/4aVWVTyyqQ=","cpuPlatform":"exynos5","createdAt":"2018-10-02T06:17:44.164Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":true,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7860","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"optus_cx-3","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508230223","imei":"359042088460679","imsi":"505025815948816","network":"HSUPA","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-10-06T07:48:10.887Z","present":false,"product":"dreamltexx","provider":{"channel":"V09yHuIzSyafTc90Bn899A==","name":"NZ"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"ce07171721f2ca3904","status":3,"statusChangedAt":"2019-09-20T02:38:26.217Z","usage":null,"usageChangedAt":"2019-10-03T11:50:05.491Z","version":"7.0","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":64,"scale":100,"source":"unknown_0","status":"charging","temp":31,"voltage":3.954},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"T38Ztl0HTAXCVsE38kavNVTL8KU=","cpuPlatform":"exynos5","createdAt":"2018-10-08T23:26:41.538Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":true,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7564","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":false,"failover":false,"roaming":false,"subtype":"LTE","type":"MOBILE"},"notes":"RESERVED FOR ZERO RATING","openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025716452371674","imei":"356397084260207","imsi":"505025702398631","network":"LTE","phoneNumber":"+61403499391"},"platform":"Android","presenceChangedAt":"2019-08-07T06:39:17.923Z","present":false,"product":"heroltexx","provider":{"channel":"+LwghACJRRWuLFzH8vyRuA==","name":"d380"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"ce12160cade0d8560c","status":3,"statusChangedAt":"2019-08-05T00:23:55.195Z","usage":null,"usageChangedAt":"2019-08-07T06:07:38.150Z","version":"6.0.1","using":false},{"abi":"arm64-v8a","airplaneMode":false,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.281},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":true,"system":true,"type":"chrome","developer":"Google Inc."}],"selected":true},"channel":"G1RKSg3vE1IO7LJSZrbs6ZqV9qU=","cpuPlatform":"exynos5","createdAt":"2018-10-18T03:59:51.094Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":true,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7632","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":true,"failover":false,"roaming":false,"subtype":"","type":"WIFI"},"notes":"unrooted, +61402537622","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025717529312634","imei":"356397086903259","imsi":"505025703492762","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-03-12T00:11:58.200Z","present":true,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":true,"remoteConnect":false,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"ce12160ccd1f323f05","status":3,"statusChangedAt":"2020-03-12T00:11:58.199Z","usage":null,"usageChangedAt":"2020-03-12T23:46:35.011Z","version":"8.0.0","using":false}]})
#
# #json.loads({"success":True,"devices":[{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":73,"scale":100,"source":"usb","status":"charging","temp":26.7,"voltage":4.037},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"mw9jfEL5+pdnvws887fgnwdiu4g=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.545Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7420","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802093412107","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.768Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"1ca45f2e0e027ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.027Z","usage":null,"usageChangedAt":"2019-02-26T05:16:06.723Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.4,"voltage":3.946},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"wTLQIlQINPTkW1GB6ZsENwG/1Vw=","cpuPlatform":"exynos5","createdAt":"2018-11-20T01:52:00.253Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.059174060821533,"url":"ws://mcloud.matrium.com.au:7464","width":1440,"xdpi":580.5709838867188,"ydpi":580.5709838867188},"manufacturer":"SAMSUNG","model":"SM-G920F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"","openGLESVersion":"3.1","operator":null,"owner":null,"phone":{"iccid":"8961025717529312634","imei":"358992070798372","imsi":"505025703492762","network":"HSPAP","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-04-11T23:53:03.505Z","present":False,"product":"zerofltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"031603b240b91601","status":3,"statusChangedAt":"2019-04-11T23:26:35.749Z","usage":"02:7d:cf:95:5c:1f:10:29:a3:e7:65:bb:2f:3f:db:00","usageChangedAt":"2019-04-11T23:44:21.789Z","version":"6.0.1","using":False},{"abi":"armeabi-v7a","airplaneMode":False,"battery":{"health":"good","level":98,"scale":100,"source":"usb","status":"charging","temp":32.3,"voltage":4.277},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"55Vl/Uczyzg9I8fW7iCCTCGSGeg=","cpuPlatform":"msm8974","createdAt":"2019-03-27T05:34:57.948Z","display":{"density":3,"fps":60,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.200733661651611,"url":"ws://mcloud.matrium.com.au:7556","width":1080,"xdpi":422.0299987792969,"ydpi":424.0690002441406},"manufacturer":"SAMSUNG","model":"SM-G900I","network":{"connected":False,"failover":False,"roaming":False,"subtype":null,"type":null},"openGLESVersion":"3.0","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352919065742079","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-05-12T23:37:45.642Z","present":False,"product":"kltedv","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"1b88d6f0","status":3,"statusChangedAt":"2019-05-09T22:55:28.265Z","usage":null,"usageChangedAt":"2019-05-07T23:16:20.701Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":78,"scale":100,"source":"usb","status":"charging","temp":26.6,"voltage":4.09},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"LdFev4vJa9NYQqvU6B7yxfsWe7U=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.553Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7412","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802097622057","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.234Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"215dad1b37057ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.032Z","usage":null,"usageChangedAt":"2019-02-26T10:49:05.184Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.8,"voltage":4.278},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"6W4ZNRI0Kc25YqbnoWaCi6j1CQM=","cpuPlatform":"exynos5","createdAt":"2019-02-20T02:45:00.723Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7612","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"optus_cx-1, rooted, +61431618629","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508284527f","imei":"358810075103309","imsi":"505025815954246","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-03-09T22:39:03.563Z","present":True,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"9886734d5647434c32","status":3,"statusChangedAt":"2020-03-09T22:39:03.563Z","usage":null,"usageChangedAt":"2020-03-12T23:46:36.816Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.4,"voltage":4.301},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"jYG1N6ZysL7nwFXXjztwRRkCGkM=","cpuPlatform":"exynos5","createdAt":"2019-09-27T00:51:22.788Z","display":{"density":2.625,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":6.2156219482421875,"url":"ws://mcloud.matrium.com.au:7993","width":1080,"xdpi":397.5644836425781,"ydpi":397.09796142578125},"manufacturer":"SAMSUNG","model":"SM-G965F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"unrooted, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508284535","imei":"355893091540459","imsi":"505025815954247","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-01-16T04:06:02.523Z","present":True,"product":"star2ltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"28","serial":"216a454f17047ece","status":3,"statusChangedAt":"2020-01-16T04:06:02.524Z","usage":null,"usageChangedAt":"2020-03-12T23:46:32.347Z","version":"9","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.5,"voltage":4.357},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"IgpSNtWAWNf34ngUOek/5NoDjhg=","cpuPlatform":"exynos5","createdAt":"2018-10-15T22:34:30.995Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7572","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"","openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508230124","imei":"357350078314596","imsi":"505025815948806","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-09-18T00:26:37.299Z","present":False,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"9885e6323446425233","status":3,"statusChangedAt":"2019-09-18T00:26:20.842Z","usage":null,"usageChangedAt":"2019-09-18T00:02:04.485Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":69,"scale":100,"source":"usb","status":"charging","temp":27,"voltage":4.014},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"6lFEtQjwuho4/ZqBP3Ve/j7mW38=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.554Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7404","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":null,"type":null},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"352802094388959","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:16.196Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"1cba56ef20047ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.030Z","usage":null,"usageChangedAt":"2019-02-26T05:16:24.360Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.6,"voltage":4.308},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"+6rtoz27n+uzbDtAxmlXo2oSipw=","cpuPlatform":"exynos5","createdAt":"2019-02-06T06:25:13.157Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7608","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"rooted, +61418673947","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025114450127308","imei":"355896090403454","imsi":"505025104559746","network":"LTE","phoneNumber":"+61418673947"},"platform":"Android","presenceChangedAt":"2020-03-04T03:35:24.708Z","present":True,"product":"starltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"25cb81cc6f0d7ece","status":3,"statusChangedAt":"2020-03-04T03:35:24.708Z","usage":null,"usageChangedAt":"2020-03-12T23:46:34.034Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.9,"voltage":4.302},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"knT0EAal7FTzNWf94cUHFsDvfxY=","cpuPlatform":"exynos5","createdAt":"2018-09-26T23:59:20.038Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7949","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"rooted, +61431202671","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025515437279196f","imei":"357350078315031","imsi":"505025504563848","network":"HSPAP","phoneNumber":"+61431202671"},"platform":"Android","presenceChangedAt":"2020-02-07T05:30:11.863Z","present":True,"product":"heroltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"9885e649593651384c","status":3,"statusChangedAt":"2020-01-16T03:23:02.001Z","usage":null,"usageChangedAt":"2020-03-13T05:15:08.613Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":25.9,"voltage":4.257},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"HRqE6wZ+KTQNNTBnMkeqvSTF/3Q=","cpuPlatform":"exynos5","createdAt":"2020-01-16T03:05:40.372Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7917","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"openGLESVersion":"3.2","operator":null,"owner":null,"phone":{"iccid":null,"imei":"355894091494432","imsi":null,"network":"UNKNOWN","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-01-16T03:05:40.390Z","present":True,"product":"starltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"28","serial":"22a494180a0b7ece","status":3,"statusChangedAt":"2020-01-16T03:05:43.965Z","usage":null,"usageChangedAt":"2020-03-12T23:46:33.201Z","version":"9","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.335},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserMainActivity","name":"Browser","selected":False,"system":True,"type":"samsung-sbrowser","developer":"Samsung"},{"id":"com.android.chrome/com.google.android.apps.chrome.Main","name":"Chrome","selected":False,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":False},"channel":"2NOdXvrLVZgtSlH4vr8z9kXXry0=","cpuPlatform":"exynos5","createdAt":"2018-11-12T05:58:42.413Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7660","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":False,"failover":False,"roaming":False,"subtype":null,"type":null},"openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025717529312618","imei":"357810082504565","imsi":"505025703492760","network":"LTE","phoneNumber":"+61478101658"},"platform":"Android","presenceChangedAt":"2018-12-03T00:23:01.439Z","present":False,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"ce011711381ab4bb0c","status":3,"statusChangedAt":"2018-11-21T04:05:33.719Z","usage":null,"usageChangedAt":"2018-12-03T00:21:13.243Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28,"voltage":4.308},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"8Vq0xaEvCIVMAfZB1AdrPIeeSkM=","cpuPlatform":"exynos5","createdAt":"2018-10-11T05:15:47.144Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7400","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"optus_cx-2, unrooted, +61435548032, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025818539139064f","imei":"359039086085482","imsi":"505025814139700","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-11-29T06:21:08.582Z","present":False,"product":"dreamltexx","provider":{"channel":"1ccoa3ywQdWm0c1oVh2kTQ==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"ce051715b4dd583201","status":3,"statusChangedAt":"2019-11-11T02:42:48.405Z","usage":null,"usageChangedAt":"2019-11-22T03:15:34.379Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":17.6,"voltage":4.3},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"iGSoZn6fI6HOR37o/4aVWVTyyqQ=","cpuPlatform":"exynos5","createdAt":"2018-10-02T06:17:44.164Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7860","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"optus_cx-3","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025819508230223","imei":"359042088460679","imsi":"505025815948816","network":"HSUPA","phoneNumber":null},"platform":"Android","presenceChangedAt":"2019-10-06T07:48:10.887Z","present":False,"product":"dreamltexx","provider":{"channel":"V09yHuIzSyafTc90Bn899A==","name":"NZ"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"24","serial":"ce07171721f2ca3904","status":3,"statusChangedAt":"2019-09-20T02:38:26.217Z","usage":null,"usageChangedAt":"2019-10-03T11:50:05.491Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":64,"scale":100,"source":"unknown_0","status":"charging","temp":31,"voltage":3.954},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"T38Ztl0HTAXCVsE38kavNVTL8KU=","cpuPlatform":"exynos5","createdAt":"2018-10-08T23:26:41.538Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7564","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":False,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"RESERVED FOR ZERO RATING","openGLESVersion":"3.1","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025716452371674","imei":"356397084260207","imsi":"505025702398631","network":"LTE","phoneNumber":"+61403499391"},"platform":"Android","presenceChangedAt":"2019-08-07T06:39:17.923Z","present":False,"product":"heroltexx","provider":{"channel":"+LwghACJRRWuLFzH8vyRuA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"23","serial":"ce12160cade0d8560c","status":3,"statusChangedAt":"2019-08-05T00:23:55.195Z","usage":null,"usageChangedAt":"2019-08-07T06:07:38.150Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.281},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"G1RKSg3vE1IO7LJSZrbs6ZqV9qU=","cpuPlatform":"exynos5","createdAt":"2018-10-18T03:59:51.094Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7632","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"unrooted, +61402537622","openGLESVersion":"3.2","operator":"YES OPTUS","owner":null,"phone":{"iccid":"8961025717529312634","imei":"356397086903259","imsi":"505025703492762","network":"LTE","phoneNumber":null},"platform":"Android","presenceChangedAt":"2020-03-12T00:11:58.200Z","present":True,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":null,"reverseForwards":[],"sdk":"26","serial":"ce12160ccd1f323f05","status":3,"statusChangedAt":"2020-03-12T00:11:58.199Z","usage":null,"usageChangedAt":"2020-03-12T23:46:35.011Z","version":"8.0.0","using":False}]})
#
# devices = json.loads({"success":True,"devices":[{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":73,"scale":100,"source":"usb","status":"charging","temp":26.7,"voltage":4.037},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"mw9jfEL5+pdnvws887fgnwdiu4g=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.545Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7420","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":None,"type":None},"openGLESVersion":"3.2","operator":None,"owner":None,"phone":{"iccid":None,"imei":"352802093412107","imsi":None,"network":"UNKNOWN","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.768Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"26","serial":"1ca45f2e0e027ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.027Z","usage":None,"usageChangedAt":"2019-02-26T05:16:06.723Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.4,"voltage":3.946},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"wTLQIlQINPTkW1GB6ZsENwG/1Vw=","cpuPlatform":"exynos5","createdAt":"2018-11-20T01:52:00.253Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.059174060821533,"url":"ws://mcloud.matrium.com.au:7464","width":1440,"xdpi":580.5709838867188,"ydpi":580.5709838867188},"manufacturer":"SAMSUNG","model":"SM-G920F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"","openGLESVersion":"3.1","operator":None,"owner":None,"phone":{"iccid":"8961025717529312634","imei":"358992070798372","imsi":"505025703492762","network":"HSPAP","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-04-11T23:53:03.505Z","present":False,"product":"zerofltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"23","serial":"031603b240b91601","status":3,"statusChangedAt":"2019-04-11T23:26:35.749Z","usage":"02:7d:cf:95:5c:1f:10:29:a3:e7:65:bb:2f:3f:db:00","usageChangedAt":"2019-04-11T23:44:21.789Z","version":"6.0.1","using":False},{"abi":"armeabi-v7a","airplaneMode":False,"battery":{"health":"good","level":98,"scale":100,"source":"usb","status":"charging","temp":32.3,"voltage":4.277},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"55Vl/Uczyzg9I8fW7iCCTCGSGeg=","cpuPlatform":"msm8974","createdAt":"2019-03-27T05:34:57.948Z","display":{"density":3,"fps":60,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.200733661651611,"url":"ws://mcloud.matrium.com.au:7556","width":1080,"xdpi":422.0299987792969,"ydpi":424.0690002441406},"manufacturer":"SAMSUNG","model":"SM-G900I","network":{"connected":False,"failover":False,"roaming":False,"subtype":None,"type":None},"openGLESVersion":"3.0","operator":None,"owner":None,"phone":{"iccid":None,"imei":"352919065742079","imsi":None,"network":"UNKNOWN","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-05-12T23:37:45.642Z","present":False,"product":"kltedv","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"23","serial":"1b88d6f0","status":3,"statusChangedAt":"2019-05-09T22:55:28.265Z","usage":None,"usageChangedAt":"2019-05-07T23:16:20.701Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":78,"scale":100,"source":"usb","status":"charging","temp":26.6,"voltage":4.09},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"LdFev4vJa9NYQqvU6B7yxfsWe7U=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.553Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7412","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":None,"type":None},"openGLESVersion":"3.2","operator":None,"owner":None,"phone":{"iccid":None,"imei":"352802097622057","imsi":None,"network":"UNKNOWN","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:10.234Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"26","serial":"215dad1b37057ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.032Z","usage":None,"usageChangedAt":"2019-02-26T10:49:05.184Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.8,"voltage":4.278},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"6W4ZNRI0Kc25YqbnoWaCi6j1CQM=","cpuPlatform":"exynos5","createdAt":"2019-02-20T02:45:00.723Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7612","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"optus_cx-1, rooted, +61431618629","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025819508284527f","imei":"358810075103309","imsi":"505025815954246","network":"LTE","phoneNumber":None},"platform":"Android","presenceChangedAt":"2020-03-09T22:39:03.563Z","present":True,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"24","serial":"9886734d5647434c32","status":3,"statusChangedAt":"2020-03-09T22:39:03.563Z","usage":None,"usageChangedAt":"2020-03-12T23:46:36.816Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.4,"voltage":4.301},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"jYG1N6ZysL7nwFXXjztwRRkCGkM=","cpuPlatform":"exynos5","createdAt":"2019-09-27T00:51:22.788Z","display":{"density":2.625,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":6.2156219482421875,"url":"ws://mcloud.matrium.com.au:7993","width":1080,"xdpi":397.5644836425781,"ydpi":397.09796142578125},"manufacturer":"SAMSUNG","model":"SM-G965F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"unrooted, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025819508284535","imei":"355893091540459","imsi":"505025815954247","network":"LTE","phoneNumber":None},"platform":"Android","presenceChangedAt":"2020-01-16T04:06:02.523Z","present":True,"product":"star2ltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"28","serial":"216a454f17047ece","status":3,"statusChangedAt":"2020-01-16T04:06:02.524Z","usage":None,"usageChangedAt":"2020-03-12T23:46:32.347Z","version":"9","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":29.5,"voltage":4.357},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"IgpSNtWAWNf34ngUOek/5NoDjhg=","cpuPlatform":"exynos5","createdAt":"2018-10-15T22:34:30.995Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7572","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"","openGLESVersion":"3.1","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025819508230124","imei":"357350078314596","imsi":"505025815948806","network":"LTE","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-09-18T00:26:37.299Z","present":False,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"23","serial":"9885e6323446425233","status":3,"statusChangedAt":"2019-09-18T00:26:20.842Z","usage":None,"usageChangedAt":"2019-09-18T00:02:04.485Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":69,"scale":100,"source":"usb","status":"charging","temp":27,"voltage":4.014},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"6lFEtQjwuho4/ZqBP3Ve/j7mW38=","cpuPlatform":"exynos5","createdAt":"2019-02-26T04:21:18.554Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7404","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":False,"failover":False,"roaming":False,"subtype":None,"type":None},"openGLESVersion":"3.2","operator":None,"owner":None,"phone":{"iccid":None,"imei":"352802094388959","imsi":None,"network":"UNKNOWN","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-03-04T04:28:16.196Z","present":False,"product":"starltexx","provider":{"channel":"mquPAAtVQyWU1VQtIfVoAQ==","name":"Singtel"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"26","serial":"1cba56ef20047ece","status":3,"statusChangedAt":"2019-02-26T05:13:00.030Z","usage":None,"usageChangedAt":"2019-02-26T05:16:24.360Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.6,"voltage":4.308},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"+6rtoz27n+uzbDtAxmlXo2oSipw=","cpuPlatform":"exynos5","createdAt":"2019-02-06T06:25:13.157Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7608","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"rooted, +61418673947","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025114450127308","imei":"355896090403454","imsi":"505025104559746","network":"LTE","phoneNumber":"+61418673947"},"platform":"Android","presenceChangedAt":"2020-03-04T03:35:24.708Z","present":True,"product":"starltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"26","serial":"25cb81cc6f0d7ece","status":3,"statusChangedAt":"2020-03-04T03:35:24.708Z","usage":None,"usageChangedAt":"2020-03-12T23:46:34.034Z","version":"8.0.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":27.9,"voltage":4.302},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"knT0EAal7FTzNWf94cUHFsDvfxY=","cpuPlatform":"exynos5","createdAt":"2018-09-26T23:59:20.038Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7949","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"rooted, +61431202671","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025515437279196f","imei":"357350078315031","imsi":"505025504563848","network":"HSPAP","phoneNumber":"+61431202671"},"platform":"Android","presenceChangedAt":"2020-02-07T05:30:11.863Z","present":True,"product":"heroltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"24","serial":"9885e649593651384c","status":3,"statusChangedAt":"2020-01-16T03:23:02.001Z","usage":None,"usageChangedAt":"2020-03-13T05:15:08.613Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":25.9,"voltage":4.257},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"HRqE6wZ+KTQNNTBnMkeqvSTF/3Q=","cpuPlatform":"exynos5","createdAt":"2020-01-16T03:05:40.372Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.775477409362793,"url":"ws://mcloud.matrium.com.au:7917","width":1080,"xdpi":428.625,"ydpi":427.1812438964844},"manufacturer":"SAMSUNG","model":"SM-G960F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"openGLESVersion":"3.2","operator":None,"owner":None,"phone":{"iccid":None,"imei":"355894091494432","imsi":None,"network":"UNKNOWN","phoneNumber":None},"platform":"Android","presenceChangedAt":"2020-01-16T03:05:40.390Z","present":True,"product":"starltexx","provider":{"channel":"XV9AV4mUTam5bG6WfGHevA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"28","serial":"22a494180a0b7ece","status":3,"statusChangedAt":"2020-01-16T03:05:43.965Z","usage":None,"usageChangedAt":"2020-03-12T23:46:33.201Z","version":"9","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.335},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserMainActivity","name":"Browser","selected":False,"system":True,"type":"samsung-sbrowser","developer":"Samsung"},{"id":"com.android.chrome/com.google.android.apps.chrome.Main","name":"Chrome","selected":False,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":False},"channel":"2NOdXvrLVZgtSlH4vr8z9kXXry0=","cpuPlatform":"exynos5","createdAt":"2018-11-12T05:58:42.413Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7660","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":False,"failover":False,"roaming":False,"subtype":None,"type":None},"openGLESVersion":"3.1","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025717529312618","imei":"357810082504565","imsi":"505025703492760","network":"LTE","phoneNumber":"+61478101658"},"platform":"Android","presenceChangedAt":"2018-12-03T00:23:01.439Z","present":False,"product":"heroltexx","provider":{"channel":"Ri/LXZMDS9ivt5Z4jjFqCw==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"23","serial":"ce011711381ab4bb0c","status":3,"statusChangedAt":"2018-11-21T04:05:33.719Z","usage":None,"usageChangedAt":"2018-12-03T00:21:13.243Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28,"voltage":4.308},"browser":{"apps":[{"id":"com.sec.android.app.sbrowser/.SBrowserLauncherActivity","name":"Browser","selected":True,"system":False,"type":"samsung-sbrowser","developer":"Samsung"}],"selected":True},"channel":"8Vq0xaEvCIVMAfZB1AdrPIeeSkM=","cpuPlatform":"exynos5","createdAt":"2018-10-11T05:15:47.144Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7400","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"optus_cx-2, unrooted, +61435548032, out of credit","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025818539139064f","imei":"359039086085482","imsi":"505025814139700","network":"LTE","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-11-29T06:21:08.582Z","present":False,"product":"dreamltexx","provider":{"channel":"1ccoa3ywQdWm0c1oVh2kTQ==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"24","serial":"ce051715b4dd583201","status":3,"statusChangedAt":"2019-11-11T02:42:48.405Z","usage":None,"usageChangedAt":"2019-11-22T03:15:34.379Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":17.6,"voltage":4.3},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"iGSoZn6fI6HOR37o/4aVWVTyyqQ=","cpuPlatform":"exynos5","createdAt":"2018-10-02T06:17:44.164Z","display":{"density":3,"fps":60.000003814697266,"height":2220,"id":0,"rotation":0,"secure":True,"size":5.8281049728393555,"url":"ws://mcloud.matrium.com.au:7860","width":1080,"xdpi":422.03021240234375,"ydpi":423.9697570800781},"manufacturer":"SAMSUNG","model":"SM-G950F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"optus_cx-3","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025819508230223","imei":"359042088460679","imsi":"505025815948816","network":"HSUPA","phoneNumber":None},"platform":"Android","presenceChangedAt":"2019-10-06T07:48:10.887Z","present":False,"product":"dreamltexx","provider":{"channel":"V09yHuIzSyafTc90Bn899A==","name":"NZ"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"24","serial":"ce07171721f2ca3904","status":3,"statusChangedAt":"2019-09-20T02:38:26.217Z","usage":None,"usageChangedAt":"2019-10-03T11:50:05.491Z","version":"7.0","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":64,"scale":100,"source":"unknown_0","status":"charging","temp":31,"voltage":3.954},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"T38Ztl0HTAXCVsE38kavNVTL8KU=","cpuPlatform":"exynos5","createdAt":"2018-10-08T23:26:41.538Z","display":{"density":4,"fps":59,"height":2560,"id":0,"rotation":0,"secure":True,"size":5.0935258865356445,"url":"ws://mcloud.matrium.com.au:7564","width":1440,"xdpi":580.5709838867188,"ydpi":575.4329833984375},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":False,"failover":False,"roaming":False,"subtype":"LTE","type":"MOBILE"},"notes":"RESERVED FOR ZERO RATING","openGLESVersion":"3.1","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025716452371674","imei":"356397084260207","imsi":"505025702398631","network":"LTE","phoneNumber":"+61403499391"},"platform":"Android","presenceChangedAt":"2019-08-07T06:39:17.923Z","present":False,"product":"heroltexx","provider":{"channel":"+LwghACJRRWuLFzH8vyRuA==","name":"d380"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"23","serial":"ce12160cade0d8560c","status":3,"statusChangedAt":"2019-08-05T00:23:55.195Z","usage":None,"usageChangedAt":"2019-08-07T06:07:38.150Z","version":"6.0.1","using":False},{"abi":"arm64-v8a","airplaneMode":False,"battery":{"health":"good","level":100,"scale":100,"source":"usb","status":"full","temp":28.4,"voltage":4.281},"browser":{"apps":[{"id":"com.android.chrome/com.google.android.apps.chrome.IntentDispatcher","name":"Chrome","selected":True,"system":True,"type":"chrome","developer":"Google Inc."}],"selected":True},"channel":"G1RKSg3vE1IO7LJSZrbs6ZqV9qU=","cpuPlatform":"exynos5","createdAt":"2018-10-18T03:59:51.094Z","display":{"density":3,"fps":59,"height":1920,"id":0,"rotation":0,"secure":True,"size":5.093525409698486,"url":"ws://mcloud.matrium.com.au:7632","width":1080,"xdpi":435.4282531738281,"ydpi":431.57476806640625},"manufacturer":"SAMSUNG","model":"SM-G930F","network":{"connected":True,"failover":False,"roaming":False,"subtype":"","type":"WIFI"},"notes":"unrooted, +61402537622","openGLESVersion":"3.2","operator":"YES OPTUS","owner":None,"phone":{"iccid":"8961025717529312634","imei":"356397086903259","imsi":"505025703492762","network":"LTE","phoneNumber":None},"platform":"Android","presenceChangedAt":"2020-03-12T00:11:58.200Z","present":True,"product":"heroltexx","provider":{"channel":"uoJvRlY3R+2biQ/S8s99bA==","name":"mcloud"},"ready":True,"remoteConnect":False,"remoteConnectUrl":None,"reverseForwards":[],"sdk":"26","serial":"ce12160ccd1f323f05","status":3,"statusChangedAt":"2020-03-12T00:11:58.199Z","usage":None,"usageChangedAt":"2020-03-12T23:46:35.011Z","version":"8.0.0","using":False}]})
#
# device = devices[0]

# list1 = [{"success":True,"health":"good"}, {"success":False,"health":"bad"}]
# str1 = ''.join(json.dumps(e) for e in list1)
# print (str1)

# excelReportPath = "/reports/excel/"
# print("excelReportPath is {}.".format(excelReportPath))
#
#
# absExcelReportPath = os.path.abspath(excelReportPath)
# print("absExcelReportPath is {}.".format(absExcelReportPath))
#
#
# if (os.path.exists(absExcelReportPath)):
#     print ("{} exists.".format(absExcelReportPath))
# else:
#     print ("{} does not exist.".format(absExcelReportPath))
#     # os.makedirs(absExcelReportPath)
# import shlex
#
# body = "MAndroid2 test example"
#
# strBody = body.translate(str.maketrans({" ":  r"\ "}))
#
# command1 = "echo java -jar sms_body \"{}\"".format(strBody)
#
# print (command1)
#
# command2 = shlex.split(command1)
#
# print (command2)
#
# response = subprocess.check_output(command2)
# print("Response of sending SMS is: ", response)


# from datetime import datetime, timedelta
#
# testSuiteStartTime = datetime.now()
#
# time.sleep(2)
#
# testSuiteEndTime = datetime.now()
#
# diff = testSuiteEndTime - testSuiteStartTime  # the result is a datetime.timedelta object
# formatedDiff = str(timedelta(seconds=diff.seconds))
# print (formatedDiff)

# command = "adb -s ce071607a2e74a1a05 shell ls -la /sdcard/MAndroid2/output/Screenshot/takescreen_20200129_020117.png"
#
# # Execute command
# response = subprocess.check_output(command.split()).decode('utf-8').split()
# print("Response is: ", response)
# print("Size is: ", response[4])
# print("Path is: ", response[-1])


# file = open("response.txt", "r")
# response = file.read()
#
#
# lines = response.splitlines()
#
# print (lines)
# print (len(lines))
# lineNumbers = 8
#
# sections = []
# sectionNumbers = int (len(lines)/lineNumbers)
#
#
# for i in range(0, sectionNumbers):
#     section = []
#     for j in range(0, (i+1)*lineNumbers):
#         section.append(lines[j])
#     sections.append(section)
#
# print (sections)
# print (len(sections))

# count = 1
# for line in response:
#     print(line)
#     section = []
#     section = section.append(line)
#     print("section is {}".format(section))
#     if count > lineNumber and count%lineNumber == 1:
#         sections = sections.append(section)
#         section = []
#
#     count += 1

# print (len(sections))
#
#
#
#
#
# file.close()


# import re
#
# pageValuesList = []
# columnCaptionsList = []
#
# columnCaptions = "Port {Sessions Up} {Sessions Down} {Sessions Not Started} {Sessions Total}"
# pageValues = "{{{Ethernet - 001} 1 0 0 1}}"
#
#
# columnCaptionsList = columnCaptions.replace(" {", ',').replace("} {", ',').replace("}", '').split(',')
# print (columnCaptionsList)
# print (columnCaptionsList[1])
#
# sessionsUpIndex = columnCaptionsList.index("Sessions Up")
# print (sessionsUpIndex)
#
# sessionsTotalIndex = columnCaptionsList.index("Sessions Total")
# print (sessionsTotalIndex)
#
# tempList = pageValues.replace("{{{", '').replace("}}", '').split("} ")
# print (tempList)
# pageValuesList.append(tempList[0])
# pageValuesList = pageValuesList + tempList[1].split()
# print (pageValuesList)
#
# if (sessionsUpIndex < len(pageValuesList)):
#     sessonsUp = pageValuesList[sessionsUpIndex]
#     print (sessonsUp)
#
# if (sessionsTotalIndex < len(pageValuesList)):
#     sessionsTotal = pageValuesList[sessionsTotalIndex]
#     print (sessionsTotal)


# from jinja2 import Environment, FileSystemLoader
#
# env = Environment()
# # template = env.from_string(
# #     """{% if x>0 %}x>0{% else %}x<0{% endif %}"""
# # )
#
#
# # env = Environment(loader=FileSystemLoader('templates'))
# env = Environment(loader=FileSystemLoader('./'))
# template = env.get_template('testTemplate.j2')
#
# Configure1 = template.render(x=1)
# Configure2 = template.render(x=-1)
#
# # to save the results
# filename = "testConfig.cfg"
# try:
#     with open(filename, "w") as fh:
#         fh.write(Configure1)
# except IOError as e:
#     print(f'save failed: unable to write to file {filename}: {e}')
# else:
#     print(Configure1)


# result = dict()
# result = "pseudowire-class MPLS_VPWS_Eth"
# # mlsClass = "pseudowire-class"
# mlsClass = "pseudowire-class"
#
# # m = re.sub(r'(mlsClass) (.*)', r'\1\2{}'.format(className), result)
# # className = re.search(r'{} (.*)'.format(className), result).group(0)
# classNameObj = re.search(r'{} (.*)'.format(mlsClass), result)
# if classNameObj:
#    print("searchObj.group(0) : ", classNameObj.group(0))
#    print("searchObj.group(1) : ", classNameObj.group(1))
# else:
#    print("Nothing found!!")
#
# print(classNameObj)


# f = open("response.txt", "r")
# text=f.read()
# lines=text.split("\n")
# print(lines)
#
# for line in lines:
#
#     line = line.strip()
#
#     if not line:
#     # if line != "":
#         print("Not empty")
#     else:
#         print("Empty")


# mls_wan_interface = "GigabitEthernet4.1"
#
# mls_wan_phy_interface = mls_wan_interface.split(".")[0]
#
# print(mls_wan_phy_interface)

# dhcp_start_ip = ipaddress.IPv4Address('72.0.0.2')
# dhcp_end_ip = ipaddress.IPv4Address('72.0.0.253')
#
# discoveredAddresses = ['72.0.0.2','10.0.0.2','72.0.0.3','72.0.0.4','72.0.0.5','72.0.0.6','72.0.0.7','72.0.0.8','72.0.0.9','72.0.0.10','72.0.0.11']
#
# for ip in discoveredAddresses:
#     dhcp_client_ip = ipaddress.IPv4Address(ip)
#     dhcp_client_ip = ipaddress.IPv4Address(ip)
#     if int(dhcp_client_ip) not in range(int(dhcp_start_ip), int(dhcp_end_ip)):
#         print("{} is not in range".format(dhcp_client_ip))

# from datetime import timedelta
#
#
# delta = timedelta(hours=1, minutes=2, seconds=3)
# total_seconds = delta.total_seconds()
# minutes = int(total_seconds // 60)
# seconds = int(total_seconds % 60)
#
# print('{minutes}:{seconds}'.format(minutes=minutes, seconds=seconds))
#
#
# my_time = '1:2:3'
# factors = (60, 1, 1/60)
#
# t1 = sum(i*j for i, j in zip(map(int, my_time.split(':')), factors))
# print(t1)
#
# import re
# string = '1:2:3'
# pattern = re.compile("^([0-9]+:[0-9]+:[0-9]+)+$")
#
# if re.match(pattern, string):
#     print("Match")
# else:
#     print("Not match")
import json

# className = "CM-NBN-TC4-INTERNET-BE"
# service_policy = {}
#
# print(service_policy)
# if (className == "CM-NBN-TC4-INTERNET-BE") and (not service_policy):
#     print("OK")
# else:
#     print("Wrong")

# cpu_stats = [
#   [
#     0,
#     '9.7'
#   ]
# ]
# # cpus = [int(float(item[1])) for item in cpu_stats]
#
# cpus = [float(item[1]) for item in cpu_stats]
#
# print (cpus)

# max_output_throughput = 7021800.0
# max_input_throughput = 75501608.0
# expected_throughput = 70000000.0
#
# if max_input_throughput >= expected_throughput and max_output_throughput >= expected_throughput:
#   print("expected!")
# else:
#   print("Unexpected!")

# command = "java -jar c:\\tmp\MatriumMAndroid2-release.jar mcloud.matrium.com.au:7986 2005 wifi_switch 0"
#
# response = subprocess.check_output(command.split())
# print("Response of {} is: {}".format(command, response))
#
# command = "adb connect mcloud.matrium.com.au:7986"
#
# response = subprocess.check_output(command.split())
# print("Response of {} is: {}".format(command, response))
#
# command = "java -jar c:\\tmp\MatriumMAndroid2-release.jar mcloud.matrium.com.au:7986 1020"
#
# response = subprocess.check_output(command.split())
# print("Response of {} is: {}".format(command, response))
#
# print (json.loads(response))
# print (json.loads(response)['description'])


# throughputList=[
#   '0',
#   '12791',
#   '20004',
#   '0',
#   '12790',
#   '20004'
# ]
# throughputDownLink = {}
# throughputUpLink = {}
# half = len(throughputList)//2
# throughputDownLinkList=throughputList[:half]
# print(throughputDownLinkList)
# throughputDownLink['min'] = throughputDownLinkList[0]
# throughputDownLink['avg'] = throughputDownLinkList[1]
# throughputDownLink['max'] = throughputDownLinkList[2]
# print("Min downlink throughput on ixload side is {}, average downlink throughput on ixload side is {}, max downlink throughput on ixload side is {}".format(throughputDownLink['min'], throughputDownLink['avg'], throughputDownLink['max']))
#
# throughputUpLinkList=throughputList[half:]
# print(throughputUpLinkList)
# throughputUpLink['min'] = throughputUpLinkList[0]
# throughputUpLink['avg'] = throughputUpLinkList[1]
# throughputUpLink['max'] = throughputUpLinkList[2]
# print("Min uplink throughput on ixload side is {}, average uplink throughput on ixload side is {}, max uplink throughput on ixload side is {}".format(throughputUpLink['min'], throughputUpLink['avg'], throughputUpLink['max']))
#

# utilisation = {
#   "78": {
#     "cpu": [
#       "95.8",
#       "98.5",
#       "99.8",
#       "98.2",
#       "98.3",
#       "98.7",
#       "99.3",
#       "9.5",
#       "99.2",
#       "99.6",
#       "99.5",
#       "98.7",
#       "99.3",
#       "99.9",
#       "7.4",
#       "95.0",
#       "94.6",
#       "94.9",
#       "93.8",
#       "95.0",
#       "95.3",
#       "95.4",
#       "6.4",
#       "93.3",
#       "92.6",
#       "93.3",
#       "91.9",
#       "93.2",
#       "91.3",
#       "6.7",
#       "93.2",
#       "93.8",
#       "92.6",
#       "93.1",
#       "92.2",
#       "93.3",
#       "92.2",
#       "94.5",
#       "92.4",
#       "94.2",
#       "95.4",
#       "83.0",
#       "85.9",
#       "94.2",
#       "6.4",
#       "92.4",
#       "95.2",
#       "92.9",
#       "95.3",
#       "93.8",
#       "94.6",
#       "95.6",
#       "93.9",
#       "93.4",
#       "94.9",
#       "96.3",
#       "94.4",
#       "94.8",
#       "94.4",
#       "6.4",
#       "95.3",
#       "95.6",
#       "94.2",
#       "96.4"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "1261872",
#       "5919960",
#       "6221896",
#       "6230736",
#       "6238600",
#       "6227120",
#       "6244704",
#       "2506952",
#       "5703040",
#       "6186656",
#       "6231400",
#       "6234848",
#       "6230376",
#       "6228936",
#       "4978400",
#       "5768976",
#       "7847576",
#       "7922816",
#       "7926952",
#       "7991512",
#       "7967688",
#       "7934008",
#       "1640632",
#       "8537912",
#       "8971216",
#       "8986416",
#       "8972600",
#       "8951112",
#       "8973232",
#       "4308296",
#       "7238936",
#       "10082976",
#       "10121488",
#       "10200328",
#       "10134064",
#       "10130424",
#       "10136064",
#       "1745832",
#       "10024808",
#       "10281120",
#       "10301424",
#       "1623152",
#       "101440",
#       "9811256",
#       "5419480",
#       "8621536",
#       "10158216",
#       "10194760",
#       "10191552",
#       "10193688",
#       "10187288",
#       "10180192",
#       "5350344",
#       "9839800",
#       "10068984",
#       "10139584",
#       "10179264",
#       "10204688",
#       "10097104",
#       "2878608",
#       "9098952",
#       "10056832",
#       "10153544",
#       "10122616"
#     ],
#     "mean_output_rate": [
#       "2502888",
#       "12334544",
#       "12963240",
#       "12983016",
#       "12967152",
#       "12996344",
#       "12953416",
#       "5226168",
#       "11822208",
#       "12930520",
#       "12980640",
#       "12969320",
#       "12984968",
#       "12984352",
#       "10369120",
#       "8494088",
#       "11334864",
#       "11411936",
#       "11420848",
#       "11374128",
#       "11400888",
#       "11378392",
#       "2276616",
#       "10093248",
#       "10627232",
#       "10628152",
#       "10641312",
#       "10676328",
#       "10681592",
#       "5081896",
#       "7291048",
#       "10209000",
#       "10314952",
#       "10311272",
#       "10299744",
#       "10305064",
#       "10308096",
#       "1772184",
#       "10093272",
#       "10381432",
#       "10380192",
#       "12637040",
#       "13035512",
#       "10514440",
#       "5546888",
#       "8884040",
#       "10435680",
#       "10463440",
#       "10472544",
#       "10473272",
#       "10478072",
#       "10467680",
#       "5540232",
#       "10208272",
#       "10487712",
#       "10499856",
#       "10489552",
#       "10511440",
#       "10498888",
#       "2992544",
#       "9474944",
#       "10446800",
#       "10517480",
#       "10530840"
#     ]
#   },
#   "128": {
#     "cpu": [
#       "99.6",
#       "99.3",
#       "9.3",
#       "100.0",
#       "99.9",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "6.5",
#       "100.0",
#       "99.9",
#       "99.7",
#       "99.5",
#       "99.3",
#       "99.4",
#       "53.8",
#       "99.7",
#       "99.2",
#       "99.0",
#       "99.5",
#       "99.4",
#       "99.0",
#       "99.7",
#       "99.9",
#       "99.4",
#       "99.7",
#       "99.4",
#       "99.6",
#       "99.4",
#       "99.6",
#       "99.6",
#       "99.5",
#       "99.0",
#       "96.9",
#       "98.5",
#       "97.1",
#       "97.7",
#       "6.7",
#       "97.0",
#       "97.8",
#       "96.9",
#       "96.5",
#       "98.7",
#       "97.9",
#       "97.0",
#       "97.6",
#       "97.8",
#       "96.6",
#       "95.1",
#       "96.6",
#       "97.6",
#       "95.6",
#       "9.2",
#       "96.0",
#       "97.3",
#       "96.1",
#       "95.6",
#       "97.0",
#       "96.7",
#       "9.1"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "24152624",
#       "24153008",
#       "11772696",
#       "21981808",
#       "26169344",
#       "26591856",
#       "26541904",
#       "26500968",
#       "26331160",
#       "19938408",
#       "19971600",
#       "24570968",
#       "24856656",
#       "24414736",
#       "24910240",
#       "24407016",
#       "24518680",
#       "18982888",
#       "21925688",
#       "21956120",
#       "21948608",
#       "22169232",
#       "22313920",
#       "22081128",
#       "10741288",
#       "20019864",
#       "20242552",
#       "20256456",
#       "20219752",
#       "20270424",
#       "20280376",
#       "4516240",
#       "19201616",
#       "19673808",
#       "19172568",
#       "19193832",
#       "19235400",
#       "19164000",
#       "6197072",
#       "17088408",
#       "18571440",
#       "18685608",
#       "18716888",
#       "18702848",
#       "18625704",
#       "18746448",
#       "13713648",
#       "17944296",
#       "18197480",
#       "18252808",
#       "18303576",
#       "18322080",
#       "18312920",
#       "3820456",
#       "17043920",
#       "17885920",
#       "17922304",
#       "17944752",
#       "17849632",
#       "18006784",
#       "16978312"
#     ],
#     "mean_output_rate": [
#       "15783576",
#       "15599120",
#       "7555424",
#       "12646208",
#       "14962480",
#       "14775800",
#       "14912504",
#       "14918376",
#       "14969864",
#       "11334896",
#       "12401224",
#       "15420512",
#       "15480616",
#       "15489864",
#       "15457776",
#       "15653784",
#       "15258000",
#       "14031048",
#       "16294632",
#       "16449712",
#       "16488768",
#       "16405384",
#       "16334840",
#       "16425432",
#       "8860528",
#       "16887048",
#       "17092720",
#       "17146992",
#       "17137784",
#       "17139664",
#       "17108472",
#       "3859544",
#       "16733224",
#       "17159048",
#       "17171016",
#       "17199840",
#       "17175896",
#       "17204864",
#       "5552704",
#       "15721728",
#       "17118784",
#       "17203584",
#       "17182392",
#       "17182480",
#       "17205304",
#       "17193248",
#       "12907200",
#       "16956968",
#       "17194840",
#       "17215440",
#       "17206648",
#       "17200304",
#       "17207536",
#       "3640080",
#       "16377680",
#       "17185320",
#       "17217424",
#       "17239032",
#       "17238680",
#       "17232992",
#       "16244800"
#     ]
#   },
#   "256": {
#     "cpu": [
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "99.0",
#       "99.2",
#       "98.9",
#       "99.5",
#       "97.9",
#       "98.6",
#       "9.0",
#       "96.1",
#       "98.0",
#       "97.3",
#       "98.0",
#       "98.6",
#       "98.1",
#       "9.2",
#       "93.9",
#       "96.1",
#       "94.3",
#       "93.8",
#       "95.3",
#       "93.8",
#       "94.7",
#       "94.4",
#       "90.7",
#       "94.2",
#       "92.3",
#       "94.1",
#       "95.3",
#       "91.2",
#       "8.7",
#       "92.2",
#       "92.9",
#       "90.7",
#       "91.7",
#       "89.4",
#       "89.5",
#       "8.9",
#       "87.1",
#       "86.6",
#       "88.1",
#       "87.2",
#       "88.6",
#       "87.9",
#       "86.8",
#       "88.4",
#       "85.8",
#       "85.5",
#       "85.8",
#       "85.7",
#       "89.5",
#       "88.8",
#       "6.8"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "47859568",
#       "60261240",
#       "61390912",
#       "61367464",
#       "61728616",
#       "61371488",
#       "61253080",
#       "13375272",
#       "41503232",
#       "42492040",
#       "42504352",
#       "42556416",
#       "42484400",
#       "42482392",
#       "10162544",
#       "36175376",
#       "38162680",
#       "38213576",
#       "38151512",
#       "38218328",
#       "38187952",
#       "20898440",
#       "28827848",
#       "33937024",
#       "34091008",
#       "34105832",
#       "34113712",
#       "34097544",
#       "34108400",
#       "18778440",
#       "30052216",
#       "30786336",
#       "30806176",
#       "30818368",
#       "30803456",
#       "30801832",
#       "7675912",
#       "25708072",
#       "28099824",
#       "28235992",
#       "28238728",
#       "28249576",
#       "28240592",
#       "14769696",
#       "22482640",
#       "24664096",
#       "24809408",
#       "24808696",
#       "24810928",
#       "24826000",
#       "24802712",
#       "16177744",
#       "23168488",
#       "23597160",
#       "23628840",
#       "23628384",
#       "23617208",
#       "23628472",
#       "8856488"
#     ],
#     "mean_output_rate": [
#       "21164928",
#       "26142456",
#       "26317800",
#       "26157496",
#       "26213912",
#       "26396192",
#       "26327280",
#       "5833544",
#       "32622584",
#       "33249240",
#       "33474032",
#       "33277192",
#       "33434000",
#       "33488152",
#       "8002352",
#       "32530352",
#       "34139480",
#       "34290256",
#       "34261088",
#       "34351616",
#       "34186288",
#       "18825560",
#       "28954408",
#       "34291800",
#       "34454336",
#       "34456480",
#       "34467112",
#       "34472016",
#       "34455488",
#       "20641160",
#       "33606552",
#       "34447928",
#       "34466784",
#       "34454008",
#       "34459096",
#       "34458072",
#       "8605528",
#       "31310080",
#       "34269328",
#       "34463936",
#       "34481336",
#       "34479968",
#       "34480880",
#       "19417664",
#       "31272848",
#       "34340920",
#       "34511872",
#       "34520568",
#       "34542552",
#       "34554456",
#       "34539392",
#       "23617632",
#       "33960576",
#       "34666152",
#       "34676712",
#       "34654456",
#       "34642312",
#       "34661736",
#       "13021904"
#     ]
#   },
#   "512": {
#     "cpu": [
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "7.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "9.9",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "6.4",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "9.1",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0",
#       "100.0"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "61163768",
#       "72270824",
#       "72445416",
#       "72334008",
#       "72430696",
#       "72524744",
#       "72113792",
#       "37814000",
#       "63834304",
#       "64681864",
#       "64734704",
#       "64694088",
#       "64748936",
#       "64671768",
#       "16509024",
#       "45362624",
#       "47222040",
#       "47334912",
#       "47358328",
#       "38712896",
#       "38728496",
#       "13670064",
#       "31662712",
#       "33361568",
#       "33466384",
#       "33438928",
#       "33435768",
#       "33468640",
#       "17912064",
#       "25592400",
#       "29955024",
#       "30064792",
#       "30093544",
#       "30108304",
#       "30091584",
#       "30086912",
#       "20598552",
#       "27070752",
#       "27481000",
#       "27515320",
#       "27512040",
#       "27491224",
#       "27507032",
#       "5536832",
#       "25149280",
#       "25755360",
#       "25793120",
#       "25770896",
#       "25767984",
#       "25787616",
#       "6126776",
#       "22529336",
#       "24175952",
#       "23024456",
#       "23039728",
#       "23043784",
#       "23024872"
#     ],
#     "mean_output_rate": [
#       "61057320",
#       "72179080",
#       "72200408",
#       "72218176",
#       "72237792",
#       "72400296",
#       "71959656",
#       "42981824",
#       "74466184",
#       "75824312",
#       "75629640",
#       "75432672",
#       "75591720",
#       "75205696",
#       "19299544",
#       "78932776",
#       "82672944",
#       "82282728",
#       "82796296",
#       "86016552",
#       "85783504",
#       "30559800",
#       "83151344",
#       "88172824",
#       "88187664",
#       "88560176",
#       "88469224",
#       "88341224",
#       "47583568",
#       "75942416",
#       "89206352",
#       "89744736",
#       "89624232",
#       "89757416",
#       "89636736",
#       "89766264",
#       "67314192",
#       "89279648",
#       "90527648",
#       "90913272",
#       "90507464",
#       "90860936",
#       "90560936",
#       "18418480",
#       "89031600",
#       "91386936",
#       "91350176",
#       "91456584",
#       "91291872",
#       "91547016",
#       "21832360",
#       "85887296",
#       "91672904",
#       "92819952",
#       "92182536",
#       "92672528",
#       "92020688"
#     ]
#   },
#   "1024": {
#     "cpu": [
#       "9.1",
#       "72.6",
#       "72.5",
#       "76.0",
#       "75.5",
#       "73.4",
#       "75.7",
#       "70.0",
#       "65.1",
#       "69.7",
#       "69.4",
#       "68.9",
#       "68.9",
#       "65.9",
#       "66.0",
#       "42.5",
#       "66.3",
#       "65.5",
#       "62.6",
#       "62.6",
#       "66.3",
#       "66.2",
#       "9.0",
#       "63.2",
#       "60.9",
#       "60.9",
#       "63.8",
#       "63.9",
#       "63.6",
#       "61.1",
#       "59.1",
#       "59.4",
#       "59.5",
#       "59.3",
#       "62.0",
#       "62.1",
#       "63.6",
#       "60.6",
#       "59.0",
#       "58.7",
#       "62.2",
#       "58.8",
#       "62.4",
#       "62.3",
#       "9.1",
#       "61.3",
#       "58.5",
#       "58.4",
#       "61.3",
#       "61.7",
#       "61.3",
#       "58.4",
#       "57.4",
#       "61.7",
#       "61.8",
#       "60.8",
#       "61.0",
#       "58.1",
#       "58.2",
#       "9.1",
#       "60.8",
#       "60.6",
#       "60.7",
#       "57.9",
#       "61.4",
#       "61.5"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "5077472",
#       "88323832",
#       "97398184",
#       "97667848",
#       "97695904",
#       "97701280",
#       "97714592",
#       "77624320",
#       "52023456",
#       "62654608",
#       "63312792",
#       "63348072",
#       "63332176",
#       "63349824",
#       "63372856",
#       "21016336",
#       "44741928",
#       "46263304",
#       "46335736",
#       "46340456",
#       "46350696",
#       "46346168",
#       "33627960",
#       "28993024",
#       "37699512",
#       "37977824",
#       "38006696",
#       "37953144",
#       "38004136",
#       "37975392",
#       "8141048",
#       "29370000",
#       "29479920",
#       "29482200",
#       "29513792",
#       "29506104",
#       "29476824",
#       "14857880",
#       "26720088",
#       "27087520",
#       "27107016",
#       "27084408",
#       "27108728",
#       "27103856",
#       "7449976",
#       "22995600",
#       "25374584",
#       "25432872",
#       "25468768",
#       "25458032",
#       "25448168",
#       "23541888",
#       "17634288",
#       "23520824",
#       "23904960",
#       "23894280",
#       "23919456",
#       "23913360",
#       "23914688",
#       "3884216",
#       "21466688",
#       "22614920",
#       "22692304",
#       "22671424",
#       "22689544",
#       "22690872"
#     ],
#     "mean_output_rate": [
#       "20340472",
#       "89187560",
#       "97253392",
#       "97588120",
#       "97541304",
#       "97523040",
#       "97529576",
#       "77569848",
#       "77463024",
#       "96287192",
#       "97480704",
#       "97519360",
#       "97511280",
#       "97540320",
#       "97536288",
#       "39370824",
#       "93916800",
#       "97290360",
#       "97537288",
#       "97533520",
#       "97531360",
#       "97514848",
#       "70824656",
#       "73470248",
#       "96767792",
#       "97484168",
#       "97522088",
#       "97512088",
#       "97518400",
#       "97517464",
#       "21624568",
#       "97080464",
#       "97496264",
#       "97510816",
#       "97541296",
#       "97530104",
#       "97517704",
#       "52465928",
#       "96137112",
#       "97452160",
#       "97519616",
#       "97510528",
#       "97521064",
#       "97536552",
#       "26853024",
#       "87999936",
#       "97213824",
#       "97502680",
#       "97540328",
#       "97540512",
#       "97517216",
#       "90329968",
#       "71574832",
#       "95893816",
#       "97481096",
#       "97514776",
#       "97530408",
#       "97517928",
#       "97541776",
#       "15880112",
#       "92266256",
#       "97192952",
#       "97509272",
#       "97540400",
#       "97534456",
#       "97516296"
#     ]
#   },
#   "1280": {
#     "cpu": [
#       "9.7",
#       "58.8",
#       "57.8",
#       "57.7",
#       "54.8",
#       "55.1",
#       "57.6",
#       "9.2",
#       "54.8",
#       "52.1",
#       "52.1",
#       "55.6",
#       "54.8",
#       "54.8",
#       "52.1",
#       "49.9",
#       "53.6",
#       "53.8",
#       "53.3",
#       "55.0",
#       "50.6",
#       "51.4",
#       "9.9",
#       "53.4",
#       "52.4",
#       "52.7",
#       "49.8",
#       "49.7",
#       "52.7",
#       "52.8",
#       "51.2",
#       "52.1",
#       "49.1",
#       "52.6",
#       "52.6",
#       "52.0",
#       "52.8",
#       "48.6",
#       "48.5",
#       "51.3",
#       "51.5",
#       "51.3",
#       "48.4",
#       "48.4",
#       "9.9",
#       "51.6",
#       "51.3",
#       "48.1",
#       "48.4",
#       "51.0",
#       "51.2",
#       "50.9",
#       "50.9",
#       "48.2",
#       "48.0",
#       "51.7",
#       "51.7",
#       "50.7",
#       "51.0",
#       "6.4"
#     ],
#     "ratePercent": [
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "18974696",
#       "60117280",
#       "62796896",
#       "62870104",
#       "62867752",
#       "62905600",
#       "62848504",
#       "62733920",
#       "39891784",
#       "45653624",
#       "45994272",
#       "46015896",
#       "46031840",
#       "46008816",
#       "46025600",
#       "8142424",
#       "36758680",
#       "37705296",
#       "37790776",
#       "37789736",
#       "37784104",
#       "37792512",
#       "20560584",
#       "26708800",
#       "32615104",
#       "32770584",
#       "32808784",
#       "32789480",
#       "32767128",
#       "32806560",
#       "10500240",
#       "27912272",
#       "29043544",
#       "29074088",
#       "29080728",
#       "26930400",
#       "26929232",
#       "15106000",
#       "24611264",
#       "24919624",
#       "24947552",
#       "24939640",
#       "24921648",
#       "24916808",
#       "5941408",
#       "21868744",
#       "23847576",
#       "23926536",
#       "23908552",
#       "23940352",
#       "23920216",
#       "23932880",
#       "16586104",
#       "22430840",
#       "22800880",
#       "22843616",
#       "22828160",
#       "22825104",
#       "22836504",
#       "7499488"
#     ],
#     "mean_output_rate": [
#       "18876496",
#       "92634920",
#       "97365320",
#       "97503408",
#       "97514048",
#       "97523416",
#       "97523368",
#       "97339688",
#       "83380128",
#       "96654784",
#       "97482360",
#       "97521680",
#       "97516968",
#       "97516568",
#       "97535552",
#       "17262144",
#       "94758104",
#       "97343336",
#       "97506512",
#       "97538216",
#       "97539184",
#       "97521792",
#       "53134112",
#       "78900504",
#       "96955640",
#       "97486600",
#       "97520200",
#       "97514488",
#       "97513368",
#       "97541944",
#       "33660848",
#       "93530368",
#       "97388504",
#       "97532056",
#       "97539696",
#       "97539760",
#       "97520128",
#       "58628968",
#       "96298712",
#       "97464744",
#       "97533032",
#       "97514712",
#       "97515944",
#       "97539768",
#       "23248656",
#       "89120400",
#       "97252528",
#       "97499808",
#       "97511384",
#       "97539944",
#       "97524080",
#       "97523296",
#       "70559768",
#       "95826144",
#       "97475760",
#       "97518256",
#       "97521288",
#       "97516576",
#       "97513112",
#       "32074768"
#     ]
#   },
#   "1518": {
#     "cpu": [
#       "52.7",
#       "55.4",
#       "55.5",
#       "55.2",
#       "52.9",
#       "52.6",
#       "56.1",
#       "51.4",
#       "50.5",
#       "51.8",
#       "47.9",
#       "45.3",
#       "45.5",
#       "6.6",
#       "48.0",
#       "47.0",
#       "47.0",
#       "44.2",
#       "44.3",
#       "46.9",
#       "47.2",
#       "30.1",
#       "46.2",
#       "43.4",
#       "43.7",
#       "46.9",
#       "47.3",
#       "46.3",
#       "9.0",
#       "43.1",
#       "43.2",
#       "45.7",
#       "45.8",
#       "45.9",
#       "43.1",
#       "43.1",
#       "41.6",
#       "46.1",
#       "45.6",
#       "45.6",
#       "42.8",
#       "45.5",
#       "45.6",
#       "8.9",
#       "42.6",
#       "42.4",
#       "45.2",
#       "44.9",
#       "45.3",
#       "45.0",
#       "9.1",
#       "42.1",
#       "42.2",
#       "45.5",
#       "45.8",
#       "44.9",
#       "44.9",
#       "42.1"
#     ],
#     "ratePercent": [
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "10",
#       "20",
#       "20",
#       "20",
#       "20",
#       "30",
#       "30",
#       "30",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "40",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "50",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "60",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "70",
#       "80",
#       "80",
#       "90",
#       "90",
#       "90",
#       "90",
#       "90",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100",
#       "100"
#     ],
#     "mean_input_rate": [
#       "91618448",
#       "98014104",
#       "98406112",
#       "98455208",
#       "98452560",
#       "98440344",
#       "98431776",
#       "40685752",
#       "61784296",
#       "62457384",
#       "45865672",
#       "45831648",
#       "45829672",
#       "29816784",
#       "30062552",
#       "37364872",
#       "37520496",
#       "37541184",
#       "37548048",
#       "37537592",
#       "37562216",
#       "9606704",
#       "30843888",
#       "32215808",
#       "32286880",
#       "32271432",
#       "32267560",
#       "32242616",
#       "27458320",
#       "24940888",
#       "28971472",
#       "29258648",
#       "29267640",
#       "29242840",
#       "29269400",
#       "29262088",
#       "5204720",
#       "26140232",
#       "26821824",
#       "26918728",
#       "26903576",
#       "26893160",
#       "26917600",
#       "15141656",
#       "20146512",
#       "24709984",
#       "23657896",
#       "23647264",
#       "23666616",
#       "23650200",
#       "8896776",
#       "20340808",
#       "22327816",
#       "22456288",
#       "22478200",
#       "22477544",
#       "22483744",
#       "22470080"
#     ],
#     "mean_output_rate": [
#       "91944760",
#       "97553664",
#       "97905408",
#       "97950776",
#       "97948776",
#       "97936760",
#       "97927560",
#       "59761656",
#       "96757920",
#       "97874120",
#       "97949384",
#       "97934264",
#       "97927992",
#       "63814760",
#       "77563600",
#       "97299424",
#       "97894048",
#       "97960040",
#       "97927800",
#       "97925328",
#       "97950328",
#       "26933864",
#       "93507936",
#       "97786344",
#       "97940984",
#       "97948160",
#       "97934448",
#       "97928616",
#       "83433424",
#       "83207016",
#       "97027104",
#       "97899080",
#       "97928088",
#       "97927048",
#       "97950912",
#       "97934192",
#       "17449904",
#       "95046880",
#       "97743960",
#       "97939840",
#       "97934096",
#       "97934072",
#       "97934552",
#       "55154224",
#       "79138024",
#       "97345544",
#       "97942096",
#       "97934072",
#       "97928800",
#       "97927496",
#       "36865616",
#       "88513400",
#       "97345864",
#       "97909944",
#       "97926104",
#       "97949792",
#       "97935096",
#       "97934512"
#     ]
#   }
# }
#
# result = dict()
# result["threshold_util"] = dict()
# threshold = "75"
#
# util = utilisation
#
# for key in util:
#   print(util[key])
#   a, b, c, d = util[key]['cpu'], util[key]['ratePercent'], util[key]['mean_input_rate'], util[key]['mean_output_rate']
#   a = [float(i) for i in a]
#   d = [float(i) for i in d]
#   if max(a) >= float(threshold):
#     indices = [index for index, elem in enumerate(a) if elem <= float(threshold) and elem >= 15]
#     print(indices)
#     if len(indices) > 0:
#       ind = d.index(max([d[index] for index in indices]))
#       print(ind)
#       if key not in result["threshold_util"]:
#         result["threshold_util"][key] = dict()
#       result["threshold_util"][key]["cpu"] = a[ind]
#       result["threshold_util"][key]["ratePercent"] = b[ind]
#       result["threshold_util"][key]["mean_input_rate"] = c[ind]
#       result["threshold_util"][key]["mean_output_rate"] = d[ind]
#       result["threshold_util"][key]["max_cpu"] = max(a)
#       result["isSuccess"] = True
#       print(result)
#   else:
#     ind = d.index(max(d))
#     print(ind)
#     if key not in result["threshold_util"]:
#       result["threshold_util"][key] = dict()
#     result["threshold_util"][key]["cpu"] = a[ind]
#     result["threshold_util"][key]["ratePercent"] = b[ind]
#     result["threshold_util"][key]["mean_input_rate"] = c[ind]
#     result["threshold_util"][key]["mean_output_rate"] = d[ind]
#     result["threshold_util"][key]["max_cpu"] = max(a)
#     result["isSuccess"] = True
#     print(result)

# b = ">"
# b = "#"
#
# if ">" or "#" in b:
#   print ("Yes")
# else:
#   print("No")
import json
# from datetime import datetime
# from datetime import timedelta
#
# time1 = datetime.today().replace(microsecond=0).strftime('%Y-%m-%d-%H:%M:%S')
# print (time1)
# time3 = datetime.today().replace(microsecond=0)
# time.sleep(2)
# time2 = datetime.today().replace(microsecond=0)
# time4 = datetime.today().replace(microsecond=0)
# print (time2)
# print (time1)
# duration = time4 - time3
# print (duration.seconds)
#
# duration2=timedelta(seconds=(time2.timestamp()-time1.timestamp()))
# print (time2)
# print (time1)
# print (duration2)
# print (time2.timestamp())
# print (time1.timestamp())
# reportContent = dict()
# reportContent['duration'] = str(timedelta(seconds=68))
#
# reportContent = json.dumps(reportContent)



# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# strResult = pytesseract.image_to_string(r'C:\test_result\Singtel_Inbound_Roaming\Screenshots\takescreen_20210521_135734.png')
# print(strResult)
# strResult = strResult.replace('\n','')
# print(strResult)
# m = re.search(r'.*(Vo.*4GLTE).*', strResult)
# print(m.group(0))
# print(m.group(1))

# from datetime import datetime
# from datetime import timedelta
# time1 = "1623820536500"
# time1 = int(time1)/1000
# #attachTime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time1))
#
# attachTime = datetime.fromtimestamp(time1).strftime('%Y-%m-%d-%H:%M:%S')
# print(attachTime)
# time2 = "1623820701757"
# time2 = int(time2)/1000
# print(time1)
# print(time2)
# print(time2-time1)
# # attachTime2 = datetime.fromtimestamp(time2-time1).strftime('%Y-%m-%d-%H:%M:%S')
# duration = str(timedelta(seconds=(time2-time1))).split('.')[0]
# print(duration)

# from random import random
# val=random()
# print(val)

# time1 = datetime.today().replace(microsecond=0).strftime('%Y-%m-%d-%H:%M:%S')
# print (time1)
# time3 = datetime.today().replace(microsecond=0)
# time.sleep(62)
# time2 = datetime.today().replace(microsecond=0)
# time4 = datetime.today().replace(microsecond=0)
# print (time2)
# print (time1)
# duration = time4 - time3
# print (duration.seconds)
# from datetime import timedelta
# endTime="1626825557685"
# answerTime="1626825538914"
#
# time3 = datetime.today().replace(microsecond=0)
#
# report=dict()
#
# epoch_time = int(time.time())
# print(epoch_time)
#
# time.sleep(2)
#
# epoch_time2 = int(time.time())
# print(epoch_time2)
#
# print(epoch_time2-epoch_time)
#
#
#
# report['voiceCallDuration'] = str(timedelta(seconds=(int(endTime)/1000-int(answerTime)/1000))).split('.')[0]
# report['delay'] = str(timedelta(seconds=(time3.second-int(1626825557685)/1000))).split('.')[0]
#
# print(report)

# import os
# path="C:\\Work\\Projects\\git\\SingTel_IR\\Singtel_Inbound_Roaming\\test_cases\\mms40k.png"
# size=os.path.getsize(path)
# print(size)

# mmsFrom = "61452368691"
# test = "+61452368691"
#
#
# if "+{}".format(mmsFrom) != test and mmsFrom != test:
#   print("error")
# else:
#   print("OK")


suite_result = {
  "suite_task_no": "2021-08-05 1925",
  "test_suite": "InboundRoaming_Test_Suite_IR38",
  "run_count": 1,
  "start_time": "Thu Aug 05 19:26:10 AEST 2021",
  "end_time": "Thu Aug 05 21:10:44 AEST 2021",
  "summary": {
    "total": 11,
    "pass": 9,
    "fail": 2
  },
  "TestCases": {
    "T1": {
      "Completion Result": "Pass",
      "Test Case": "IR38.1 LTE Attach and Detach.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.1%20LTE%20Attach%20and%20Detach.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 19:26:11 AEST 2021",
      "End Time": "Thu Aug 05 19:34:01 AEST 2021",
      "Duration": "469",
      "Total Issues": "86",
      "Report Id": "14059"
    },
    "T2": {
      "Completion Result": "Pass",
      "Test Case": "IR38.2a Internet access of UE(1) across 3G and 4G network (3G to 4G transition).fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.2a%20Internet%20access%20of%20UE(1)%20across%203G%20and%204G%20network%20(3G%20to%204G%20transition).fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 19:34:16 AEST 2021",
      "End Time": "Thu Aug 05 19:43:08 AEST 2021",
      "Duration": "531",
      "Total Issues": "119",
      "Report Id": "14068"
    },
    "T3": {
      "Completion Result": "Pass",
      "Test Case": "IR38.2b Internet access of UE(1) across 3G and 4G network (3G to 4G transition).fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.2b%20Internet%20access%20of%20UE(1)%20across%203G%20and%204G%20network%20(3G%20to%204G%20transition).fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 19:43:23 AEST 2021",
      "End Time": "Thu Aug 05 19:53:30 AEST 2021",
      "Duration": "606",
      "Total Issues": "135",
      "Report Id": "14077"
    },
    "T4": {
      "Completion Result": "Pass",
      "Test Case": "IR38.3a Internet access of UE(1) across 3G and 4G network (4G to 3G transition).fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.3a%20Internet%20access%20of%20UE(1)%20across%203G%20and%204G%20network%20(4G%20to%203G%20transition).fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 19:53:46 AEST 2021",
      "End Time": "Thu Aug 05 20:04:32 AEST 2021",
      "Duration": "646",
      "Total Issues": "129",
      "Report Id": "14086"
    },
    "T6": {
      "Completion Result": "Fail",
      "Test Case": "IR38.4 MMS.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.4%20MMS.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:04:47 AEST 2021",
      "End Time": "Thu Aug 05 20:14:33 AEST 2021",
      "Duration": "585",
      "Total Issues": "103",
      "Report Id": "14095"
    },
    "T7": {
      "Completion Result": "Pass",
      "Test Case": "IR38.5 Combined Attach.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.5%20Combined%20Attach.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:14:49 AEST 2021",
      "End Time": "Thu Aug 05 20:20:27 AEST 2021",
      "Duration": "338",
      "Total Issues": "64",
      "Report Id": "14104"
    },
    "T8": {
      "Completion Result": "Pass",
      "Test Case": "IR38.6 CS Fallback Mobile Originating Voice Call - UE1(a) calls UE2(a).fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.6%20CS%20Fallback%20Mobile%20Originating%20Voice%20Call%20-%20UE1(a)%20calls%20UE2(a).fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:20:42 AEST 2021",
      "End Time": "Thu Aug 05 20:32:37 AEST 2021",
      "Duration": "714",
      "Total Issues": "130",
      "Report Id": "14113"
    },
    "T9": {
      "Completion Result": "Pass",
      "Test Case": "IR38.7 CS Fallback Mobile Terminating Voice Call - UE2(a) calls UE1(a).fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.7%20CS%20Fallback%20Mobile%20Terminating%20Voice%20Call%20-%20UE2(a)%20calls%20UE1(a).fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:32:53 AEST 2021",
      "End Time": "Thu Aug 05 20:44:47 AEST 2021",
      "Duration": "714",
      "Total Issues": "131",
      "Report Id": "14122"
    },
    "T10": {
      "Completion Result": "Pass",
      "Test Case": "IR38.8 SMS over SGs.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.8%20SMS%20over%20SGs.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:45:02 AEST 2021",
      "End Time": "Thu Aug 05 20:55:03 AEST 2021",
      "Duration": "600",
      "Total Issues": "121",
      "Report Id": "14131"
    },
    "T11": {
      "Completion Result": "Abort",
      "Test Case": "IR38.9 LTE Speedtest.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.9%20LTE%20Speedtest.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 20:55:18 AEST 2021",
      "End Time": "Thu Aug 05 21:02:59 AEST 2021",
      "Duration": "460",
      "Total Issues": "68",
      "Report Id": "14140"
    },
    "T12": {
      "Completion Result": "Pass",
      "Test Case": "IR38.10 Data Access from 2G-3G using PGW in HPLMN over Gp-S8 Interface.fftc",
      "Location": "project://Singtel_Inbound_Roaming/test_cases/IR38.10%20Data%20Access%20from%202G-3G%20using%20PGW%20in%20HPLMN%20over%20Gp-S8%20Interface.fftc",
      "Owner": "",
      "Start Time": "Thu Aug 05 21:03:14 AEST 2021",
      "End Time": "Thu Aug 05 21:10:28 AEST 2021",
      "Duration": "434",
      "Total Issues": "85",
      "Report Id": "14149"
    }
  }
}

# suite_result = json.loads(active_suite_str)

# print(suite_result["summary"]["pass"])
# print(suite_result["summary"]["total"])
# print(suite_result["TestCases"])
#
# for testcase in suite_result["TestCases"]:
#   print (testcase)
#
# parentTestCaseName = "IR38.2a Internet access of UE(1) across 3G and 4G network (3G to 4G transition).fftc"
# for key in suite_result["TestCases"]:
#         testcase = suite_result["TestCases"][key]["Test Case"]
#         print(testcase)
#
#         if parentTestCaseName == suite_result["TestCases"][key]["Test Case"]:
#           parentTestCaseStatus = suite_result["TestCases"][key]["Completion Result"]
#           print (parentTestCaseStatus)
#         # print(key)
#         # print(suite_result["TestCases"][key])
from datetime import datetime
# from datetime import timedelta
#
# attachEpochTime = 1633310532.381
# attachCompleteTime = 1633310664
#
# attachDuration = str(timedelta(seconds=(int(attachCompleteTime)-int(attachEpochTime)))).split('.')[0]
# print(attachDuration)
#
#
# temp = int(attachCompleteTime)-int(attachEpochTime)
# print(temp)
#


download = "0.12Mbps"

if Decimal(download.rstrip("Mbps")) > 0:
  print("OK")
else:
  print("Error")

print (download.rstrip("Mbps"))
print (Decimal(download.rstrip("Mbps")))




