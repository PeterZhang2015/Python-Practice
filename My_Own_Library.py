import requests, os, bs4

#Use to soup the html code from a URL.
def Soup_HTML_URL(url):

    #Get HTML code from requests by the input url.
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print("There is a problem %s" % exc)


    soup = bs4.BeautifulSoup(res.text, "html.parser")

    return soup

#Use to get selected information on decoded HTML.
def Get_Selected_Information(soup, tag_filter, information_filter):

    soup_element_list = soup.select(tag_filter)

    selected_information_list = []

    for soup_element in soup_element_list:
        selected_information = soup_element.get(information_filter)
        selected_information_list = selected_information_list + [selected_information]

    return selected_information_list

#Store downloaded information
def Store_Downloaded_Information(downloaded_url, dir_name):

    #Get HTML code from requests by the input url.
    res = requests.get(downloaded_url)
    try:
        res.raise_for_status()
        print("Downloading page %s" % downloaded_url)
    except Exception as exc:
        print("There is a problem %s" % exc)

    #Create downloaded dir if it is doesn't exist.
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Set stored filed name and related path.
    stored_file_name = os.path.basename(downloaded_url)
    stored_file_with_path = os.path.join(dir_name, stored_file_name)

    # Starting to store downloaded information
    stored_file = open(stored_file_with_path, 'wb')
    for chuck in res.iter_content(100000):
        stored_file.write(chuck)



