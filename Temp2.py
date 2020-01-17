import json

#response = {"isSuccess":"true","startTime":"1570149500023","description":"Current Network Type is 4G\/3G\/2G (auto connect)","networkMode":"4G\/3G\/2G (auto connect)","screenshotURL":"\/sdcard\/MAndroid2\/Output\/Screenshot\/takescreen_20191004_103820.png"};

f=open("json_data2.txt", "r");
if f.mode == 'r':
    contents = f.read();
    print contents;

    response = contents;

    data = json.loads(response);
    description = data["description"];
    screenshotURL = data["screenshotURL"];


    print "description: {}".format(description)

    print "screenshotURL: {}".format(screenshotURL)









