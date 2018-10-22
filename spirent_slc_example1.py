from SpirentSLC import SLC
slc = SLC.init(host='localhost:9005')

project_list = slc.list()
print project_list

#define parameters
project_name = "language_tanslation"
session_name = "Command_Prompt"
response_name = "get_python_language_code"

#Open project
project = slc.open(project_name)
print project

project_list = project.list(parameter_file=True, response_map=True)
print project_list

session = project.Command_Prompt_ffsp.open()
print session


#response_map = session.command('ls', response_map=project.response_map_ls_ffrm)
response_map = session.command('ls')
print response_map

#response_map.close()
session.close()
#project.close()

