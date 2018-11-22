from SpirentSLC import SLC
import sys
import json

slc = SLC.init(host='localhost:9005')

project_list = slc.list()
print project_list

#define parameters
project_name = "spirent_slc"
session_name = "Command_Prompt_ffsp"
quick_calls_name = "Command_Prompt_QC_fftc"
response_map_name = "slc_windows_ping_ffrm"
quick_call_name1 = "Get_Date_Time"
quick_call_name2 = "Get_List_Largest"

#Check target iTest project exist.
if project_name not in project_list:
    print("project %s is not in project list %s" % (project_name, project_list))
    sys.exit(0)

#Open project
project = slc.open(project_name)
print project

#Check project list
project_list = project.list(parameter_file=True, response_map=True)
print project_list


#Check target session profile exist in target iTest project.
if session_name not in project_list:
    print("session profile %s is not in project %s" % (session_name, project))
    sys.exit(0)

#Open target session in target project.
session_string = "session = project.{}.open()" .format(session_name)
exec(session_string)


#Check quick call list for a session.
quickCallList_string = "quickCallList = project.{}.list()" .format(quick_calls_name)
exec(quickCallList_string)
print quickCallList

#Check quick call exist.
if quick_call_name1 not in quickCallList:
    print("quick call %s is not in project %s" % (quick_call_name1, project))
    sys.exit(0)

quickCall_string1 = "current_date_time = project.{}.{}()" .format(session_name, quick_call_name1)
exec(quickCall_string1)
#current_date_time = project.Command_Prompt_ffsp.Get_Date_Time()
print current_date_time

#Check quick call exist.
if quick_call_name2 not in quickCallList:
    print("quick call %s is not in project %s" % (quick_call_name1, project))
    sys.exit(0)

#set input parameters for quick call 2.
inputList = [5,2,7,22,1,8,3,2,4,6,7]
inputList = " ".join(map(str, inputList))

quickCall_string2 = "result = project.{}.{}(List_In=\"{}\")" .format(session_name, quick_call_name2, inputList)
print(quickCall_string2)
exec(quickCall_string2)
#current_date_time = project.Command_Prompt_ffsp.Get_Date_Time()
print(result)

#Format the return value to json format.
result = str(result)
result = json.loads(result)
print(result)

largest_value = result["largest_value"]
type = result["type"]
print(largest_value)
print(type)

#Check target response map exist in target iTest project.
if response_map_name not in project_list:
    print("response map %s is not in project %s" % (response_map_name, project))
    sys.exit(0)

#Use target response map for the command in target session.
response_map_string = "response_map = session.command('ping localhost', response_map=project.{})" .format(response_map_name)
exec(response_map_string)

print response_map.queries()

print response_map.prompt()

print response_map.packets_sent()
print response_map.packets_received()
print response_map.packets_lost()
print response_map.packets_lost_percentage()

print response_map.minimum_latency()
print response_map.maximum_latency()
print response_map.average_latency()

#response_map.close()
session.close()
#project.close()
slc.close()
