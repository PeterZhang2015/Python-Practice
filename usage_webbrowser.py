import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')


try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

#download_file = open('RomeoAndJuliet.txt', 'wb')

#for chunk in res.iter_content(100000):#
#    download_file.write(chunk)

#download_file.close()

#print(res.text[:2000])

print(res.headers)


#print('There was a problem: %s' % (exc))

