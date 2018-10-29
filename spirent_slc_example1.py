from SpirentSLC import SLC
slc = SLC.init(host='localhost:9005')

project_list = slc.list()
print project_list

#define parameters
project_name = "spirent_slc"
#session_name = "selenium_ffsp"
response_name = "slc_windows_ping_ffrm"

#Open project
project = slc.open(project_name)
print project

#Check project list
project_list = project.list(parameter_file=True, response_map=True)
print project_list

#Check quick call list for a session.
#quickCallList = project.Command_Prompt_QC_fftc.list()
#print quickCallList


#Open target session in target project.
session = project.Command_Prompt_ffsp.open()
print session

#Use target response map for the command in target session.
response_map = session.command('ping localhost', response_map=project.slc_windows_ping_ffrm)
print response_map.queries()

print response_map.prompt()

print response_map.Packets_Sent()
print response_map.Packets_Received()
print response_map.Packets_Lost()
print response_map.Packets_Lost_Percentage()

print response_map.Minimum_Latency()
print response_map.Maximum_Latency()
print response_map.Average_Latency()

#response_map.close()
session.close()
#project.close()
slc.close()
