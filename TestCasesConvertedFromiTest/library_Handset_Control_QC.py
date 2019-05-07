"""
Headline: Quickcall library handset ADB control
Description:
	Quickcall library for handset ADB control.
"""

from iTestCommon import *

class library_Handset_Control_QC(object):

    def main(self):
        """
        Headline: The entry point to the test case
        """
        session = iTestCommon()._getSession()
        response = eval('session.main()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Activate_BAIC(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Activate_BAIC(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Activate_BAOC(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Activate_BAOC(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Activate_BAIC_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Activate_BAIC_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Activate_BAOC_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Activate_BAOC_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Activate_CFU_S7(self, Handset_Id, Forwarded_Number=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Forwarded_Number is not None:
            nonMandatoryArgs.append('Forwarded_Number=\'' + Forwarded_Number + '\'')
        response = eval('session.Activate_CFU_S7(Handset_Id=\'' + Handset_Id + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Check_Current_Setting(self, Handset_Id=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.APN_Check_Current_Setting(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Config_Exists(self, Handset_Id, Apn_In):
        session = iTestCommon()._getSession()
        response = eval('session.APN_Config_Exists(Handset_Id=\'' + Handset_Id + '\', Apn_In=\'' + Apn_In + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Add_toberemoved(self, Handset_Id=None, Apn_Auth_Type=None, New_Apn=None, New_Name=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Apn_Auth_Type is not None:
            nonMandatoryArgs.append('Apn_Auth_Type=\'' + Apn_Auth_Type + '\'')
        if New_Apn is not None:
            nonMandatoryArgs.append('New_Apn=\'' + New_Apn + '\'')
        if New_Name is not None:
            nonMandatoryArgs.append('New_Name=\'' + New_Name + '\'')
        response = eval('session.APN_Add_toberemoved(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Add_S7(self, Handset_Id, New_Apn, New_Name, New_APN_Type, New_UserName=None, New_Password=None, New_MMSC=None, New_MMS_Proxy=None, New_MMS_Port=None, APN_Protocol=None, APN_Roaming_Protocol=None, Sim_Slot=None, Auth_Type='-1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if New_UserName is not None:
            nonMandatoryArgs.append('New_UserName=\'' + New_UserName + '\'')
        if New_Password is not None:
            nonMandatoryArgs.append('New_Password=\'' + New_Password + '\'')
        if New_MMSC is not None:
            nonMandatoryArgs.append('New_MMSC=\'' + New_MMSC + '\'')
        if New_MMS_Proxy is not None:
            nonMandatoryArgs.append('New_MMS_Proxy=\'' + New_MMS_Proxy + '\'')
        if New_MMS_Port is not None:
            nonMandatoryArgs.append('New_MMS_Port=\'' + New_MMS_Port + '\'')
        if APN_Protocol is not None:
            nonMandatoryArgs.append('APN_Protocol=\'' + APN_Protocol + '\'')
        if APN_Roaming_Protocol is not None:
            nonMandatoryArgs.append('APN_Roaming_Protocol=\'' + APN_Roaming_Protocol + '\'')
        if Sim_Slot is not None:
            nonMandatoryArgs.append('Sim_Slot=\'' + Sim_Slot + '\'')
        response = eval('session.APN_Add_S7(Handset_Id=\'' + Handset_Id + '\', New_Apn=\'' + New_Apn + '\', New_Name=\'' + New_Name + '\', New_APN_Type=\'' + New_APN_Type + '\', Auth_Type=\'' + Auth_Type + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting_Deprecated(self, Handset_Id, Apn, Protocol, Reboot_flag='0'):
        session = iTestCommon()._getSession()
        response = eval('session.APN_Change_Protocol_Setting_Deprecated(Handset_Id=\'' + Handset_Id + '\', Reboot_flag=\'' + Reboot_flag + '\', Apn=\'' + Apn + '\', Protocol=\'' + Protocol + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting(self, Handset_Id, Apn, Protocol, Reboot_flag='0'):
        session = iTestCommon()._getSession()
        response = eval('session.APN_Change_Protocol_Setting(Handset_Id=\'' + Handset_Id + '\', Reboot_flag=\'' + Reboot_flag + '\', Apn=\'' + Apn + '\', Protocol=\'' + Protocol + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting_byId(self, Handset_Id, apnId, Protocol, testServer=None, Reboot_flag='0'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.APN_Change_Protocol_Setting_byId(Handset_Id=\'' + Handset_Id + '\', Reboot_flag=\'' + Reboot_flag + '\', apnId=\'' + apnId + '\', Protocol=\'' + Protocol + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting_Deprecated(self, Handset_Id, Apn):
        session = iTestCommon()._getSession()
        response = eval('session.APN_Get_Protocol_Setting_Deprecated(Handset_Id=\'' + Handset_Id + '\', Apn=\'' + Apn + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting(self, Handset_Id, Apn):
        session = iTestCommon()._getSession()
        response = eval('session.APN_Get_Protocol_Setting(Handset_Id=\'' + Handset_Id + '\', Apn=\'' + Apn + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting_byId(self, Handset_Id, apnId, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.APN_Get_Protocol_Setting_byId(Handset_Id=\'' + Handset_Id + '\', apnId=\'' + apnId + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Get_Attribute(self, Apn_Id, Apn_Attribute, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.APN_Get_Attribute(Apn_Id=\'' + Apn_Id + '\', Apn_Attribute=\'' + Apn_Attribute + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Update_Attribute(self, Apn_Id, Apn_Attribute, Attribute_Value, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.APN_Update_Attribute(Apn_Id=\'' + Apn_Id + '\', Apn_Attribute=\'' + Apn_Attribute + '\', Attribute_Value=\'' + Attribute_Value + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Add_IPv6(self, Handset_Id=None, New_Apn=None, New_Name=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if New_Apn is not None:
            nonMandatoryArgs.append('New_Apn=\'' + New_Apn + '\'')
        if New_Name is not None:
            nonMandatoryArgs.append('New_Name=\'' + New_Name + '\'')
        response = eval('session.APN_Add_IPv6(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Switch(self, Handset_Id=None, Apn_Id=None, Reboot_Flag='0'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Apn_Id is not None:
            nonMandatoryArgs.append('Apn_Id=\'' + Apn_Id + '\'')
        response = eval('session.APN_Switch(Reboot_Flag=\'' + Reboot_Flag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Delete(self, Handset_Id=None, Apn_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Apn_Id is not None:
            nonMandatoryArgs.append('Apn_Id=\'' + Apn_Id + '\'')
        response = eval('session.APN_Delete(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def APN_Get_Max(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.APN_Get_Max(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Answer_CS_Call(self, Handset_Id=None, testServer=None, unlock_flag='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Answer_CS_Call(unlock_flag=\'' + unlock_flag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Answer_CS_Call_Alt(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Answer_CS_Call_Alt(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attach_User(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Attach_User(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attach_User_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Attach_User_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attach_User_Noreboot(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Attach_User_Noreboot(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attach_User_Noreboot_S7_toberemoved(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Attach_User_Noreboot_S7_toberemoved(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def UnAttach_User_Noreboot_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.UnAttach_User_Noreboot_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def ReAttach_User_Noreboot_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.ReAttach_User_Noreboot_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_LTE(self, Atten_Level=None, Command=None, Directory='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Atten_Level is not None:
            nonMandatoryArgs.append('Atten_Level=\'' + Atten_Level + '\'')
        if Command is not None:
            nonMandatoryArgs.append('Command=\'' + Command + '\'')
        response = eval('session.Attenuation_LTE(Directory=\'' + Directory + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel(self, Channel_Number, Atten_Level, Command=None, Directory='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Command is not None:
            nonMandatoryArgs.append('Command=\'' + Command + '\'')
        response = eval('session.Attenuation_Channel(Channel_Number=\'' + Channel_Number + '\', Atten_Level=\'' + Atten_Level + '\', Directory=\'' + Directory + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel_ShowStatus(self, File=None):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        response = eval('session.Attenuation_Channel_ShowStatus(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Initialize_All_Channels(self, Atten_Level='0'):
        session = iTestCommon()._getSession()
        response = eval('session.Attenuation_Initialize_All_Channels(Atten_Level=\'' + Atten_Level + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Lanes_Connectivity(self, ComName=None, Directory='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if ComName is not None:
            nonMandatoryArgs.append('ComName=\'' + ComName + '\'')
        response = eval('session.Attenuation_Lanes_Connectivity(Directory=\'' + Directory + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_SetBlockLevel(self, File=None, Atten_Val=None, Block_No='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if Atten_Val is not None:
            nonMandatoryArgs.append('Atten_Val=\'' + Atten_Val + '\'')
        response = eval('session.Attenuation_SetBlockLevel(Block_No=\'' + Block_No + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_SetAllBlockLevel(self, File=None, Atten_Val=None):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if Atten_Val is not None:
            nonMandatoryArgs.append('Atten_Val=\'' + Atten_Val + '\'')
        response = eval('session.Attenuation_SetAllBlockLevel(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_GetBlockLevel(self, File=None, testServer=None, Block_No='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Attenuation_GetBlockLevel(Block_No=\'' + Block_No + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_FadeBlockLevel(self, File=None, Start_Atten_Val=None, End_Atten_Val=None, Int_Time=None, Block_No='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if Start_Atten_Val is not None:
            nonMandatoryArgs.append('Start_Atten_Val=\'' + Start_Atten_Val + '\'')
        if End_Atten_Val is not None:
            nonMandatoryArgs.append('End_Atten_Val=\'' + End_Atten_Val + '\'')
        if Int_Time is not None:
            nonMandatoryArgs.append('Int_Time=\'' + Int_Time + '\'')
        response = eval('session.Attenuation_FadeBlockLevel(Block_No=\'' + Block_No + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Handover(self, File=None, vBlock_No=None, wBlock_No=None, Start_Atten_Val=None, End_Atten_Val=None, Int_Time=None):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if vBlock_No is not None:
            nonMandatoryArgs.append('vBlock_No=\'' + vBlock_No + '\'')
        if wBlock_No is not None:
            nonMandatoryArgs.append('wBlock_No=\'' + wBlock_No + '\'')
        if Start_Atten_Val is not None:
            nonMandatoryArgs.append('Start_Atten_Val=\'' + Start_Atten_Val + '\'')
        if End_Atten_Val is not None:
            nonMandatoryArgs.append('End_Atten_Val=\'' + End_Atten_Val + '\'')
        if Int_Time is not None:
            nonMandatoryArgs.append('Int_Time=\'' + Int_Time + '\'')
        response = eval('session.Attenuation_Handover(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Browser_Close(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Browser_Close(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Browse_Internet(self, Handset_Id, Url='http://www.spirent.com', Use_Chrome='0'):
        session = iTestCommon()._getSession()
        response = eval('session.Browse_Internet(Handset_Id=\'' + Handset_Id + '\', Url=\'' + Url + '\', Use_Chrome=\'' + Use_Chrome + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_IMEI_by_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_IMEI_by_Id(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_BAIC(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Check_BAIC(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_BAIC_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Check_BAIC_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type_OLD(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = eval('session.Change_Handset_Network_Type_OLD(Handset_Id=\'' + Handset_Id + '\', New_Network_Type=\'' + New_Network_Type + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type_Android5(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = eval('session.Change_Handset_Network_Type_Android5(Handset_Id=\'' + Handset_Id + '\', New_Network_Type=\'' + New_Network_Type + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = eval('session.Change_Handset_Network_Type(Handset_Id=\'' + Handset_Id + '\', New_Network_Type=\'' + New_Network_Type + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Handset_Userplane_Ip(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Check_Handset_Userplane_Ip(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Handset_Network_Type(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Check_Handset_Network_Type(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Handset_Screen_Lock(self, Handset_Id, Return_State_As_Boolean='0'):
        session = iTestCommon()._getSession()
        response = eval('session.Check_Handset_Screen_Lock(Handset_Id=\'' + Handset_Id + '\', Return_State_As_Boolean=\'' + Return_State_As_Boolean + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_In_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_In_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Network_Connectivity(self, ip):
        session = iTestCommon()._getSession()
        response = eval('session.Check_Network_Connectivity(ip=\'' + ip + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_CS_Call_Status(self, Handset_Id, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_CS_Call_Status(Handset_Id=\'' + Handset_Id + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_CS_Call_Status_to_be_removed(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_CS_Call_Status_to_be_removed(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_CS_Calling_Number_Display(self, Handset_Id, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_CS_Calling_Number_Display(Handset_Id=\'' + Handset_Id + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_MMS_Max_Id(self, Handset_Id, M_Type):
        session = iTestCommon()._getSession()
        response = eval('session.Check_MMS_Max_Id(Handset_Id=\'' + Handset_Id + '\', M_Type=\'' + M_Type + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_MMS_Max_Id_New(self, Handset_Id, Type, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_MMS_Max_Id_New(Handset_Id=\'' + Handset_Id + '\', Type=\'' + Type + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Out_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_Out_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_SMS_Max_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_SMS_Max_Id(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_SMS_Max_Id_New(self, Handset_Id, Type, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_SMS_Max_Id_New(Handset_Id=\'' + Handset_Id + '\', Type=\'' + Type + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Body_Deprecated(self, Handset_Id=None, Received_MMS_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Received_MMS_Id is not None:
            nonMandatoryArgs.append('Received_MMS_Id=\'' + Received_MMS_Id + '\'')
        response = eval('session.Check_Receive_MMS_Body_Deprecated(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Body(self, Handset_Id=None, Received_MMS_Id=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Received_MMS_Id is not None:
            nonMandatoryArgs.append('Received_MMS_Id=\'' + Received_MMS_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_Receive_MMS_Body(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Subject_Deprecated(self, Handset_Id=None, Received_MMS_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Received_MMS_Id is not None:
            nonMandatoryArgs.append('Received_MMS_Id=\'' + Received_MMS_Id + '\'')
        response = eval('session.Check_Receive_MMS_Subject_Deprecated(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Subject(self, Handset_Id, Received_MMS_Id, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_Receive_MMS_Subject(Handset_Id=\'' + Handset_Id + '\', Received_MMS_Id=\'' + Received_MMS_Id + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS(self, Handset_Id=None, SMS_Max_Id=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if SMS_Max_Id is not None:
            nonMandatoryArgs.append('SMS_Max_Id=\'' + SMS_Max_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_Receive_SMS(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS_Body_original(self, Handset_Id=None, SMS_Max_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if SMS_Max_Id is not None:
            nonMandatoryArgs.append('SMS_Max_Id=\'' + SMS_Max_Id + '\'')
        response = eval('session.Check_Receive_SMS_Body_original(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS_Body(self, Handset_Id=None, SMS_Max_Id=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if SMS_Max_Id is not None:
            nonMandatoryArgs.append('SMS_Max_Id=\'' + SMS_Max_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Check_Receive_SMS_Body(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Sent_SMS_Body(self, Handset_Id, SMS_Max_Id, B_Number, Select_Items):
        session = iTestCommon()._getSession()
        response = eval('session.Check_Sent_SMS_Body(Handset_Id=\'' + Handset_Id + '\', SMS_Max_Id=\'' + SMS_Max_Id + '\', B_Number=\'' + B_Number + '\', Select_Items=\'' + Select_Items + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Check_Sent_SMS(self, Handset_Id, SMS_Max_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Check_Sent_SMS(Handset_Id=\'' + Handset_Id + '\', SMS_Max_Id=\'' + SMS_Max_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Clean_Handset_Cache(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Clean_Handset_Cache(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Clear_Handset_XML_Files(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Clear_Handset_XML_Files(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Clean_Handset_SMS_Database(self):
        session = iTestCommon()._getSession()
        response = eval('session.Clean_Handset_SMS_Database()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Close_Netcat_Session(self):
        session = iTestCommon()._getSession()
        response = eval('session.Close_Netcat_Session()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def De_Activate_BAIC(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.De_Activate_BAIC(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def De_Activate_BAOC(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.De_Activate_BAOC(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def De_Activate_BAIC_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.De_Activate_BAIC_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def De_Activate_BAOC_S7(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.De_Activate_BAOC_S7(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def De_Activate_CFU_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.De_Activate_CFU_S7(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Decode_HTTP_Pcap_By_Keyword(self, Pcap_Path, Pcap_Name, Host=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Host is not None:
            nonMandatoryArgs.append('Host=\'' + Host + '\'')
        response = eval('session.Decode_HTTP_Pcap_By_Keyword(Pcap_Path=\'' + Pcap_Path + '\', Pcap_Name=\'' + Pcap_Name + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Decode_HTTP_Pcap_Redirect(self, Pcap_Path, Pcap_Name, Host=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Host is not None:
            nonMandatoryArgs.append('Host=\'' + Host + '\'')
        response = eval('session.Decode_HTTP_Pcap_Redirect(Pcap_Path=\'' + Pcap_Path + '\', Pcap_Name=\'' + Pcap_Name + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Delete_Handset_XML(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Delete_Handset_XML(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Delete_SMS(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Delete_SMS(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Detach_User(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Detach_User(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def End_CS_Call(self, Handset_Id=None, testServer=None, unlock_flag='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.End_CS_Call(unlock_flag=\'' + unlock_flag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def File_Download(self, User, Pwd, Handset_Id, Server_Address='10.32.51.15', Local_Folder='/sdcard/Download', DL_Filename=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if DL_Filename is not None:
            nonMandatoryArgs.append('DL_Filename=\'' + DL_Filename + '\'')
        response = eval('session.File_Download(Server_Address=\'' + Server_Address + '\', User=\'' + User + '\', Pwd=\'' + Pwd + '\', Handset_Id=\'' + Handset_Id + '\', Local_Folder=\'' + Local_Folder + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def FTP_Download(self, Handset_Id, Server_Ip, User, Password, File_Get, File_Size=None, testServer=None, Remote_Folder='/export/home/support/iTest/DL/', Timeout='1800'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File_Size is not None:
            nonMandatoryArgs.append('File_Size=\'' + File_Size + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.FTP_Download(Handset_Id=\'' + Handset_Id + '\', Remote_Folder=\'' + Remote_Folder + '\', Server_Ip=\'' + Server_Ip + '\', User=\'' + User + '\', Password=\'' + Password + '\', File_Get=\'' + File_Get + '\', Timeout=\'' + Timeout + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def FTP_Download_OLD(self, Handset_Id=None, Server_Ip=None, User=None, Password=None, File_Name=None, File_Size=None, Timeout='1800'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Server_Ip is not None:
            nonMandatoryArgs.append('Server_Ip=\'' + Server_Ip + '\'')
        if User is not None:
            nonMandatoryArgs.append('User=\'' + User + '\'')
        if Password is not None:
            nonMandatoryArgs.append('Password=\'' + Password + '\'')
        if File_Name is not None:
            nonMandatoryArgs.append('File_Name=\'' + File_Name + '\'')
        if File_Size is not None:
            nonMandatoryArgs.append('File_Size=\'' + File_Size + '\'')
        response = eval('session.FTP_Download_OLD(Timeout=\'' + Timeout + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def FTP_Upload_OLD(self, Handset_Id, Server_Ip=None, User=None, Password=None, File_Name=None, File_Size=None, Timeout='1800'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Server_Ip is not None:
            nonMandatoryArgs.append('Server_Ip=\'' + Server_Ip + '\'')
        if User is not None:
            nonMandatoryArgs.append('User=\'' + User + '\'')
        if Password is not None:
            nonMandatoryArgs.append('Password=\'' + Password + '\'')
        if File_Name is not None:
            nonMandatoryArgs.append('File_Name=\'' + File_Name + '\'')
        if File_Size is not None:
            nonMandatoryArgs.append('File_Size=\'' + File_Size + '\'')
        response = eval('session.FTP_Upload_OLD(Handset_Id=\'' + Handset_Id + '\', Timeout=\'' + Timeout + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def FTP_Upload(self, Handset_Id, File_Put, testServer=None, Server_Ip=None, User=None, Password=None, File_Size=None, Remote_Folder='/export/home/support/iTest/UL/', Timeout='1800'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        if Server_Ip is not None:
            nonMandatoryArgs.append('Server_Ip=\'' + Server_Ip + '\'')
        if User is not None:
            nonMandatoryArgs.append('User=\'' + User + '\'')
        if Password is not None:
            nonMandatoryArgs.append('Password=\'' + Password + '\'')
        if File_Size is not None:
            nonMandatoryArgs.append('File_Size=\'' + File_Size + '\'')
        response = eval('session.FTP_Upload(Handset_Id=\'' + Handset_Id + '\', Remote_Folder=\'' + Remote_Folder + '\', File_Put=\'' + File_Put + '\', Timeout=\'' + Timeout + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Interrogate_Supplementary_Service(self, UE_ID, Service_User_Number, Interrogate_Number, Service_Name):
        session = iTestCommon()._getSession()
        response = eval('session.Interrogate_Supplementary_Service(UE_ID=\'' + UE_ID + '\', Service_User_Number=\'' + Service_User_Number + '\', Interrogate_Number=\'' + Interrogate_Number + '\', Service_Name=\'' + Service_Name + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Adb_Handler_For_Handset(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Get_Adb_Handler_For_Handset(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_APN_List(self):
        session = iTestCommon()._getSession()
        response = eval('session.Get_APN_List()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_APN_Id(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Get_APN_Id(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_CurrentAPN_Id(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Get_CurrentAPN_Id(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_APN_UserName(self, Handset_Id, APN):
        session = iTestCommon()._getSession()
        response = eval('session.Get_APN_UserName(Handset_Id=\'' + Handset_Id + '\', APN=\'' + APN + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_4G_3G_Id(self, id_List):
        session = iTestCommon()._getSession()
        response = eval('session.Get_4G_3G_Id(id_List=\'' + id_List + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Device_Index(self):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Device_Index()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Date_From_Handset(self, Handset_Id, testServer=None, nodeFormat='0'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Get_Date_From_Handset(Handset_Id=\'' + Handset_Id + '\', nodeFormat=\'' + nodeFormat + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Element_From_List(self, list_input=None, i=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if list_input is not None:
            nonMandatoryArgs.append('list_input=\'' + list_input + '\'')
        if i is not None:
            nonMandatoryArgs.append('i=\'' + i + '\'')
        response = eval('session.Get_Element_From_List(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Handset_Software_Version(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Handset_Software_Version(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Imsi_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Imsi_From_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_IMEI_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_IMEI_From_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_First_8_Digit_of__IMEI_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_First_8_Digit_of__IMEI_From_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Mobile_Number_by_Imsi(self, Imsi):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Mobile_Number_by_Imsi(Imsi=\'' + Imsi + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_MMS_Time(self, Handset_Id, MMS_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_MMS_Time(Handset_Id=\'' + Handset_Id + '\', MMS_Id=\'' + MMS_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_MMS_Time_New(self):
        session = iTestCommon()._getSession()
        response = eval('session.Get_MMS_Time_New()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Ping_RTT(self, testServer=None, ip=None, Handset_Id=None, send_count=None, packet_size=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        if ip is not None:
            nonMandatoryArgs.append('ip=\'' + ip + '\'')
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if send_count is not None:
            nonMandatoryArgs.append('send_count=\'' + send_count + '\'')
        if packet_size is not None:
            nonMandatoryArgs.append('packet_size=\'' + packet_size + '\'')
        response = eval('session.Get_Ping_RTT(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Session_IP(self, Handset_Id, Protocol='ipv4'):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Session_IP(Handset_Id=\'' + Handset_Id + '\', Protocol=\'' + Protocol + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_SMS_Database_Info(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_SMS_Database_Info(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_MMS_Database_Info(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_MMS_Database_Info(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Screen_Resolution(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Screen_Resolution(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_DL_Traffic(self):
        session = iTestCommon()._getSession()
        response = eval('session.Generate_DL_Traffic()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_iPerf_Traffic(self, Ip, Format, Interval, BW, Time, Server_Port, Protocol, Ret_Data=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Ret_Data is not None:
            nonMandatoryArgs.append('Ret_Data=\'' + Ret_Data + '\'')
        response = eval('session.Generate_iPerf_Traffic(Ip=\'' + Ip + '\', Format=\'' + Format + '\', Interval=\'' + Interval + '\', BW=\'' + BW + '\', Time=\'' + Time + '\', Server_Port=\'' + Server_Port + '\', Protocol=\'' + Protocol + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_Ping_Traffic(self, Handset_Id=None, ip=None, send_count=None, packet_size=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if ip is not None:
            nonMandatoryArgs.append('ip=\'' + ip + '\'')
        if send_count is not None:
            nonMandatoryArgs.append('send_count=\'' + send_count + '\'')
        if packet_size is not None:
            nonMandatoryArgs.append('packet_size=\'' + packet_size + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Generate_Ping_Traffic(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_Ping_From_Server(self, Dest_Ip=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Dest_Ip is not None:
            nonMandatoryArgs.append('Dest_Ip=\'' + Dest_Ip + '\'')
        response = eval('session.Generate_Ping_From_Server(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_Ping_From_Ftp_Server_To_IP(self, Dest_Ip, Packets_Num, Packets_Size):
        session = iTestCommon()._getSession()
        response = eval('session.Generate_Ping_From_Ftp_Server_To_IP(Dest_Ip=\'' + Dest_Ip + '\', Packets_Num=\'' + Packets_Num + '\', Packets_Size=\'' + Packets_Size + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Generate_User_Plane_Traffic(self, ip_iperf_server, Handset_Id=None, test_time=None, test_interval=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if test_time is not None:
            nonMandatoryArgs.append('test_time=\'' + test_time + '\'')
        if test_interval is not None:
            nonMandatoryArgs.append('test_interval=\'' + test_interval + '\'')
        response = eval('session.Generate_User_Plane_Traffic(ip_iperf_server=\'' + ip_iperf_server + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Get_Total_SMS_MMS(self, Handset_Id, Message_Type):
        session = iTestCommon()._getSession()
        response = eval('session.Get_Total_SMS_MMS(Handset_Id=\'' + Handset_Id + '\', Message_Type=\'' + Message_Type + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Handset_Signal_Strength(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Handset_Signal_Strength(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Handover_From_4G_To_3G(self, Handset_Id, testServer=None, att_start_level='10', incrBy='1'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Handover_From_4G_To_3G(Handset_Id=\'' + Handset_Id + '\', att_start_level=\'' + att_start_level + '\', incrBy=\'' + incrBy + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Handover_From_3G_To_4G(self, Handset_Id, testServer=None, att_start_level='20', decrBy='-1'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Handover_From_3G_To_4G(Handset_Id=\'' + Handset_Id + '\', att_start_level=\'' + att_start_level + '\', decrBy=\'' + decrBy + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Handover_From_4G_To_4G(self, Handset_Id, Source_4G_Channel_Id, Destination_4G_Channel_Id, testServer=None):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Handover_From_4G_To_4G(Handset_Id=\'' + Handset_Id + '\', Source_4G_Channel_Id=\'' + Source_4G_Channel_Id + '\', Destination_4G_Channel_Id=\'' + Destination_4G_Channel_Id + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Http_Get_Wget_Or_Curl(self, Handset_Id=None, Url=None, Output_File='output.html'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Url is not None:
            nonMandatoryArgs.append('Url=\'' + Url + '\'')
        response = eval('session.Http_Get_Wget_Or_Curl(Output_File=\'' + Output_File + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Intialize_Handset_ADB(self):
        session = iTestCommon()._getSession()
        response = eval('session.Intialize_Handset_ADB()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Locate_G_NetTrack_Log(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Locate_G_NetTrack_Log(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Lock_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Lock_Handset(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Network_Traffic_Statistics(self):
        session = iTestCommon()._getSession()
        response = eval('session.Network_Traffic_Statistics()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Output_G_NetTrack_Log(self, Handset_Id=None, Log_Folder_Name=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Log_Folder_Name is not None:
            nonMandatoryArgs.append('Log_Folder_Name=\'' + Log_Folder_Name + '\'')
        response = eval('session.Output_G_NetTrack_Log(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Power_Off_Handset(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Power_Off_Handset(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Place_CS_Call(self, Handset_Id, Phone_Number, testServer=None, unlock_flag='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Place_CS_Call(Handset_Id=\'' + Handset_Id + '\', Phone_Number=\'' + Phone_Number + '\', unlock_flag=\'' + unlock_flag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Place_Emergency_Call(self, Handset_Id=None, Phone_Number=None, testServer=None, endCallFlag='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Phone_Number is not None:
            nonMandatoryArgs.append('Phone_Number=\'' + Phone_Number + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Place_Emergency_Call(endCallFlag=\'' + endCallFlag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Query_AIRPLANE_Mode(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Query_AIRPLANE_Mode(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Restart_Adb_Server(self):
        session = iTestCommon()._getSession()
        response = eval('session.Restart_Adb_Server()')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Restart_Handset(self, Handset_Id=None, Wait_handset_reboot='0'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Restart_Handset(Wait_handset_reboot=\'' + Wait_handset_reboot + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Screen_Capture(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Screen_Capture(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Send_SMS(self, Handset_Id, Phone_Number, Sms_Body, Sms_Subject, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Send_SMS(Handset_Id=\'' + Handset_Id + '\', Phone_Number=\'' + Phone_Number + '\', Sms_Body=\'' + Sms_Body + '\', Sms_Subject=\'' + Sms_Subject + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Send_MMS(self, Handset_Id=None, testServer=None, Phone_Number=None, Mms_Body=None, Mms_Subject=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        if Phone_Number is not None:
            nonMandatoryArgs.append('Phone_Number=\'' + Phone_Number + '\'')
        if Mms_Body is not None:
            nonMandatoryArgs.append('Mms_Body=\'' + Mms_Body + '\'')
        if Mms_Subject is not None:
            nonMandatoryArgs.append('Mms_Subject=\'' + Mms_Subject + '\'')
        response = eval('session.Send_MMS(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Set_Network_Mode(self, Handset_Id=None, Network_Mode=None, testServer=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Network_Mode is not None:
            nonMandatoryArgs.append('Network_Mode=\'' + Network_Mode + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Set_Network_Mode(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Set_Network_Mode_Through_GUI(self, Handset_Id=None, Network_Mode=None, testServer=None, turnOffFlag='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Network_Mode is not None:
            nonMandatoryArgs.append('Network_Mode=\'' + Network_Mode + '\'')
        if testServer is not None:
            nonMandatoryArgs.append('testServer=\'' + testServer + '\'')
        response = eval('session.Set_Network_Mode_Through_GUI(turnOffFlag=\'' + turnOffFlag + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def SSH_To_Server(self, CustNet_Server, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.SSH_To_Server(CustNet_Server=\'' + CustNet_Server + '\', Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def S7_SSH_To_Server(self, Server_Id, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.S7_SSH_To_Server(Server_Id=\'' + Server_Id + '\', Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def S7_Generate_iPerf_Traffic(self, Handset_Id, Ip, Format, Interval, BW, Time, Server_Port, Protocol, Ret_Data=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Ret_Data is not None:
            nonMandatoryArgs.append('Ret_Data=\'' + Ret_Data + '\'')
        response = eval('session.S7_Generate_iPerf_Traffic(Handset_Id=\'' + Handset_Id + '\', Ip=\'' + Ip + '\', Format=\'' + Format + '\', Interval=\'' + Interval + '\', BW=\'' + BW + '\', Time=\'' + Time + '\', Server_Port=\'' + Server_Port + '\', Protocol=\'' + Protocol + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def S7_Start_iPerf_Server(self, Handset_Id, Port, Interval, Format, W_Size=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if W_Size is not None:
            nonMandatoryArgs.append('W_Size=\'' + W_Size + '\'')
        response = eval('session.S7_Start_iPerf_Server(Handset_Id=\'' + Handset_Id + '\', Port=\'' + Port + '\', Interval=\'' + Interval + '\', Format=\'' + Format + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Start_Android_Application(self, Handset_Id=None, Activity_Name=None, Application_Name=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Activity_Name is not None:
            nonMandatoryArgs.append('Activity_Name=\'' + Activity_Name + '\'')
        if Application_Name is not None:
            nonMandatoryArgs.append('Application_Name=\'' + Application_Name + '\'')
        response = eval('session.Start_Android_Application(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Start_Application(self, Handset_Id=None, App_Path='com.metricowireless.datumandroid/com.metricowireless.datumandroid.datumui.DatumAndroidFragmentActivity  '):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Start_Application(App_Path=\'' + App_Path + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Start_Netcat_Session(self, Nc_Port, Nc_Host):
        session = iTestCommon()._getSession()
        response = eval('session.Start_Netcat_Session(Nc_Port=\'' + Nc_Port + '\', Nc_Host=\'' + Nc_Host + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Start_iPerf_Server(self, Port, Interval, Format, W_Size=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if W_Size is not None:
            nonMandatoryArgs.append('W_Size=\'' + W_Size + '\'')
        response = eval('session.Start_iPerf_Server(Port=\'' + Port + '\', Interval=\'' + Interval + '\', Format=\'' + Format + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Stop_Android_Application(self, Handset_Id=None, Application_Name=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Application_Name is not None:
            nonMandatoryArgs.append('Application_Name=\'' + Application_Name + '\'')
        response = eval('session.Stop_Android_Application(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_On_Mobile_Data(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_On_Mobile_Data(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_off_Mobile_Data(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_off_Mobile_Data(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_AIRPLANE_Mode_S4(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_AIRPLANE_Mode_S4(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_On_AIRPLANE_Mode_toremove(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_On_AIRPLANE_Mode_toremove(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_On_AIRPLANE_Mode(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_On_AIRPLANE_Mode(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_Off_AIRPLANE_Mode(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_Off_AIRPLANE_Mode(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Switch_Off_AIRPLANE_Mode_toremove(self, Handset_Id=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Switch_Off_AIRPLANE_Mode_toremove(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Tcp_Dump_old(self, Handset_Id=None, Time=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Time is not None:
            nonMandatoryArgs.append('Time=\'' + Time + '\'')
        response = eval('session.Tcp_Dump_old(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Tcp_Dump_HTTP(self, Handset_Id=None, Time=None, Url=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Time is not None:
            nonMandatoryArgs.append('Time=\'' + Time + '\'')
        if Url is not None:
            nonMandatoryArgs.append('Url=\'' + Url + '\'')
        response = eval('session.Tcp_Dump_HTTP(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Tcp_Dump(self, Handset_Id=None, Packets_Number=None, Name_Index=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        if Packets_Number is not None:
            nonMandatoryArgs.append('Packets_Number=\'' + Packets_Number + '\'')
        if Name_Index is not None:
            nonMandatoryArgs.append('Name_Index=\'' + Name_Index + '\'')
        response = eval('session.Tcp_Dump(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Ui_Check_If_Screen_Element_Is_Present(self, Element_Xpath=None, Handset_Id=None, Refresh_Screen_XML='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Element_Xpath is not None:
            nonMandatoryArgs.append('Element_Xpath=\'' + Element_Xpath + '\'')
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Ui_Check_If_Screen_Element_Is_Present(Refresh_Screen_XML=\'' + Refresh_Screen_XML + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Ui_Get_Element_Tap_Coordinates(self, Input_XML=None, Element_Xpath=None):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Input_XML is not None:
            nonMandatoryArgs.append('Input_XML=\'' + Input_XML + '\'')
        if Element_Xpath is not None:
            nonMandatoryArgs.append('Element_Xpath=\'' + Element_Xpath + '\'')
        response = eval('session.Ui_Get_Element_Tap_Coordinates(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Ui_Get_Screen_Layout(self, Handset_Id=None, Refresh_Screen_XML='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Ui_Get_Screen_Layout(Refresh_Screen_XML=\'' + Refresh_Screen_XML + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Ui_Tap_On_Screen_Element_By_Xpath(self, Element_Xpath=None, Handset_Id=None, Refresh_Screen_XML='1', Duration='50', Bypass_MTP_Prompt='1'):
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if Element_Xpath is not None:
            nonMandatoryArgs.append('Element_Xpath=\'' + Element_Xpath + '\'')
        if Handset_Id is not None:
            nonMandatoryArgs.append('Handset_Id=\'' + Handset_Id + '\'')
        response = eval('session.Ui_Tap_On_Screen_Element_By_Xpath(Refresh_Screen_XML=\'' + Refresh_Screen_XML + '\', Duration=\'' + Duration + '\', Bypass_MTP_Prompt=\'' + Bypass_MTP_Prompt + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Unlock_Handset(self, Handset_Id, timeOut='600000'):
        session = iTestCommon()._getSession()
        response = eval('session.Unlock_Handset(Handset_Id=\'' + Handset_Id + '\', timeOut=\'' + timeOut + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_Simple(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Unlock_Handset_Simple(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Unlock_Handset_S7(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_Non_Reboot(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = eval('session.Unlock_Handset_Non_Reboot(Handset_Id=\'' + Handset_Id + '\')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel_Connectivity(self, ComName=None, Directory='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if ComName is not None:
            nonMandatoryArgs.append('ComName=\'' + ComName + '\'')
        response = eval('session.Attenuation_Channel_Connectivity(Directory=\'' + Directory + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_SetChannel_Atten(self, File=None, Atten_Val=None, Block_No='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        if Atten_Val is not None:
            nonMandatoryArgs.append('Atten_Val=\'' + Atten_Val + '\'')
        response = eval('session.Attenuation_SetChannel_Atten(Block_No=\'' + Block_No + '\',' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

    def Attenuation_ShowStatus(self, File=None):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        nonMandatoryArgs = []
        if File is not None:
            nonMandatoryArgs.append('File=\'' + File + '\'')
        response = eval('session.Attenuation_ShowStatus(' + ', '.join(nonMandatoryArgs) + ')')
        iTestCommon()._writeLog(response.steps_report())
        return iTestCommon()._formResponse(response)

