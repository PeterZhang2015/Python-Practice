# -*- coding: utf-8 -*-
from googletrans import Translator
socks5 = 'socks5://127.0.0.1'
#translator = Translator(proxies={'http': socks5, 'https': socks5})
#translator = Translator(proxies={'http://wpad.in.telstra.com.au': 'proxy.pac'})
#translator = Translator(proxies={'http://wpad.in.telstra.com.au': 'proxy.pac'})
translator = Translator()
output = translator.translate('Le message a ├⌐t├⌐ envoy├⌐ avec succ├¿s par SMS.')
print(output)


#import urllib2
#import goslate

#proxy_handler = urllib2.ProxyHandler({"http" : "http://wpad.in.telstra.com.au/proxy.pac"})
#proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
  #                                  urllib2.HTTPSHandler(proxy_handler))

#gs_with_proxy = goslate.Goslate(opener=proxy_opener)
#output = gs_with_proxy.translate("hello world", "zh")

#print(output)
