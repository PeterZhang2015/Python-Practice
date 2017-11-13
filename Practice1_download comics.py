


import requests, os, bs4

#Define Variables.
url = 'http://xkcd.com'              # starting url
dir_name = 'download_comics'  # Define directory to store downloaded file.

#Created directory to store downloaded information.
os.makedirs(dir_name, exist_ok=1)

#Get HTML web code.
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("There is a problem %s" % exc)

#Decode HTML web code with beautiful soup.
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Select special tag in the decoded HTML web code.
tag_filter = '#comic img'
soupElement = soup.select(tag_filter)
if soupElement[0] == "":
    print("There is no selected tag by tag filter %s" % tag_filter)

#Select the special informaion in the decoded tag.
selected_informaion_filter = 'src'      ### Get attribue from selected tags ###
selected_informaion_content = soupElement[0].get(selected_informaion_filter)

#Check the validation for the selected information.
if selected_informaion_content == "":
    print("There is no selected information by selected information filter %s" % selected_informaion_filter)

#Use the decoded information
downloaded_url = url + selected_informaion_content
print("Downloading page %s" % downloaded_url)

res = requests.get(downloaded_url)

try:
    res.raise_for_status()
except Exception as exc:
    print("There is a problem %s when downloading page %s" % exc, downloaded_url)


#Store downloaded file in directory
#Define file name
stored_file_name = os.path.basename(downloaded_url)
stored_file_path = os.path.join(dir_name, stored_file_name)

#Starting to store downloaded information
stored_file = open(stored_file_path, 'wb')
for chuck in res.iter_content(100000):
    stored_file.write(chuck)

### Trying to get linked URL for downloading. ###
#Select the special informaion in the decoded tag.
tag_filter = 'a[rel="prev"]'
soupElement = soup.select(tag_filter)      ###Use attribute as a fiter###
if soupElement[0] == "":
    print("There is no selected tag by tag filter %s" % tag_filter)

#Select the special informaion in the decoded tag.
#The URL that the text links to is determined by the href attribute
selected_informaion_filter = 'href'                ###Get attribute information from selected tags.###
selected_informaion_content = soupElement[0].get(selected_informaion_filter)

#Check the validation for the selected information.
if selected_informaion_content == "":
    print("There is no selected information by selected information filter %s" % selected_informaion_filter)

new_downloaded_url = url + selected_informaion_content

#Get information from new URL.
res = requests.get(new_downloaded_url)

##########################################################################
#Get HTML web code.
#res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("There is a problem %s" % exc)

#Decode HTML web code with beautiful soup.
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Select special tag in the decoded HTML web code.
tag_filter = '#comic img'
soupElement = soup.select(tag_filter)
if soupElement[0] == "":
    print("There is no selected tag by tag filter %s" % tag_filter)

#Select the special informaion in the decoded tag.
selected_informaion_filter = 'src'      ### Get attribue from selected tags ###
selected_informaion_content = soupElement[0].get(selected_informaion_filter)

#Check the validation for the selected information.
if selected_informaion_content == "":
    print("There is no selected information by selected information filter %s" % selected_informaion_filter)

#Use the decoded information
downloaded_url = url + selected_informaion_content
print("Downloading page %s" % downloaded_url)

res = requests.get(downloaded_url)

try:
    res.raise_for_status()
except Exception as exc:
    print("There is a problem %s when downloading page %s" % exc, downloaded_url)


#Store downloaded file in directory
#Define file name
stored_file_name = os.path.basename(downloaded_url)
stored_file_path = os.path.join(dir_name, stored_file_name)

#Starting to store downloaded information
stored_file = open(stored_file_path, 'wb')
for chuck in res.iter_content(100000):
    stored_file.write(chuck)



#End of this file.


