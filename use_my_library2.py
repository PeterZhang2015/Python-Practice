import My_Own_Library, requests

#define python url
base_url = 'http://xkcd.com'              # starting url, which is the end page of one of the commics on target web page.

python_url = base_url

downloaded_dir = "downloaded_comics/downloaded_comic1"

while not python_url.endswith("#"):     # Need to locate the characteristic of the last downloaded page(No "pre" page).

    #Decode URL with beautiful soup.
    soup = My_Own_Library.Soup_HTML_URL(python_url)

    #Locate the downloaded URL of the content by inspecting the element by development tool of web browser.
    tag_filter = "#comic img"   #tag filter by tag and parent tag.
    information_filter = "src"   #Attribute of selected tag, which is the locating URL.

    #Get the selected information
    selected_information = My_Own_Library.Get_Selected_Information(soup, tag_filter, information_filter)

    if selected_information == []:  #Judge gotten resources before using it, empty list.
        print("There is no commic to be downloaded on URL %s" % python_url)
        break

    downloaded_url = python_url + selected_information[0] #selected URL is not exactly the downloaded url, needs pre dealing.

    #Download current content.
    My_Own_Library.Store_Downloaded_Information(downloaded_url, downloaded_dir)

    #Get the next URL that needs to be downloaded.
    #Locate the downloaded URL of the content by inspecting the element by development tool of web browser.
    tag_filter = "a[rel='prev']"   #tag filter by tag and parent tag.
    information_filter = "href"   #Attribute of selected tag, which is the locating URL.

    #Get the selected information
    selected_information = My_Own_Library.Get_Selected_Information(soup, tag_filter, information_filter)

    if selected_information == []:  #Judge gotten resources before using it, empty list.
        print("There is no pre page to be downloaded on URL %s" % python_url)
        break

    # Update new python URL.
    python_url = base_url + selected_information[0] #selected URL is not exactly the downloaded url, needs pre dealing.
