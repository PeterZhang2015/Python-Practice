# -*- coding: utf-8 -*-

from googletrans import Translator
import sys
import json
import codecs

#Get Parameters calling this python script
#text_for_translating = sys.argv[1]
file = open("translating_text.txt", "r")
text_for_translating = file.read()
#text_for_translating = codecs.open('translating_text.txt', encoding="utf8").readlines()
#print ("***********Text for translating*************")
#print(text_for_translating)

translating_to_language = sys.argv[1]
#print ("***********Translating to language*************")
#print(translating_to_language)





#################Main test logical#################################.
def main():
    translator = Translator()


    output = translator.translate(text_for_translating, dest=translating_to_language)

    #print ("***********Translated text*************")
    #print(output.text)
    #print ("***********Text source Language*************")
    #print(output.src)


    # Set return as a Python object (dict):
    returnVal = {
        "translated_text": output.text,
        "translating_source_language": output.src
    }

    # convert into JSON:
    returnVal = json.dumps(returnVal)

    print(returnVal)

#Call main function.
if __name__ == "__main__":
    main()






#from googletrans import Translator
#socks5 = 'socks5://127.0.0.1'
#translator = Translator(proxies={'http': socks5, 'https': socks5})
#translator = Translator(proxies={'http://wpad.in.telstra.com.au': 'proxy.pac'})
#translator = Translator(proxies={'http://wpad.in.telstra.com.au': 'proxy.pac'})
#translator = Translator()
#output = translator.translate('Le message a ├⌐t├⌐ envoy├⌐ avec succ├¿s par SMS.')
#print(output)


#import urllib2
#import goslate

#proxy_handler = urllib2.ProxyHandler({"http" : "http://wpad.in.telstra.com.au/proxy.pac"})
#proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
  #                                  urllib2.HTTPSHandler(proxy_handler))

#gs_with_proxy = goslate.Goslate(opener=proxy_opener)
#output = gs_with_proxy.translate("hello world", "zh")

#print(output)
