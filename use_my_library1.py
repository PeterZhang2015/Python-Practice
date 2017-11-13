import My_Own_Library, requests

#define python url
url = 'http://xkcd.com'              # starting url

#Use Soup_HTML_URL function
soup = My_Own_Library.Soup_HTML_URL(url)


#Use Get_Selected_Information
tag_filter = '#comic img'
information_filter = 'src'
selected_information_list = My_Own_Library.Get_Selected_Information(soup, tag_filter, information_filter)


#Deal with selected information
# Define directory to store downloaded file.
dir_name = 'download_comics'

#download selected information
for selected_infomation in selected_information_list:
    # Use the decoded information
    downloaded_url = url + selected_infomation
    My_Own_Library.Store_Downloaded_Information(downloaded_url, dir_name)

#Get connected URL
#Use Get_Selected_Information
tag_filter = 'a[rel="prev"]'
information_filter = 'href'

selected_information_list = My_Own_Library.Get_Selected_Information(soup, tag_filter, information_filter)

#download selected information
#There are two "pre" button on webpage.
selected_infomation = selected_information_list[0]
# Use the decoded information
downloaded_url = url + selected_infomation
# Use Soup_HTML_URL function
soup = My_Own_Library.Soup_HTML_URL(downloaded_url)

# Use Get_Selected_Information
tag_filter = "#comic img"
information_filter = "src"
selected_information_list = My_Own_Library.Get_Selected_Information(soup, tag_filter, information_filter)
for selected_infomation in selected_information_list:
    # Use the decoded information
    downloaded_url = url + selected_infomation
    My_Own_Library.Store_Downloaded_Information(downloaded_url, dir_name)



