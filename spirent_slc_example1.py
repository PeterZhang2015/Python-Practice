from SpirentSLC import SLC
import sys

slc = SLC.init(host='localhost:9005')

project_list = slc.list()
print project_list

#define parameters
project_name = "spirent_slc"
session_name = "Command_Prompt_ffsp"
response_map_name = "slc_windows_ping_ffrm"

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

#Check quick call list for a session.
#quickCallList = project.Command_Prompt_QC_fftc.list()
#print quickCallList

#Check target session profile exist in target iTest project.
if session_name not in project_list:
    print("session profile %s is not in project %s" % (session_name, project))
    sys.exit(0)

#Open target session in target project.
session_string = "session = project.{}.open()" .format(session_name)
exec(session_string)

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
