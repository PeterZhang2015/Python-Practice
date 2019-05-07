from SpirentSLC import SLC
from SpirentSLC.Execution import *
from robot.api import logger

import re
import io
import logging
import collections
from time import sleep, time
from datetime import datetime
from robot.api import logger

global session
global sessionMap
global sessionIndex
global index
global log_level

class iTestCommon(object):

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	global log_level
	log_level = 'INFO'

	def connectItest(self, host='localhost:9005'):
		self.slc = SLC.init(host)

	def openProject(self, project='my_project'):
		self.project = self.slc.open(project)

	def startSession(self, name, alias=None, parameter=None):
		global session
		if (parameter is None):
			open_command = "self.project." + name + ".open()"
		else:
			open_command = "self.project." + name + ".open(parameter_file='" + parameter + "')"
		if (alias is None):
			alias = name
		try:
			session = eval(open_command)
			self.sessionIndex[self.index] = alias
			self.sessionMap[alias] = session
			self.session = session
			self.index += 1
		except Exception:
			raise Exception('Can not open session, perform: ' + open_command + ' error')

	def switchSession(self, index_or_alias):
		global session
		global index
		if self._representsInt(index_or_alias):
			i = int(index_or_alias)
			if (i <= 0 or i >= self.index):
				raise Exception('Invalid index: ' + str(index_or_alias))
			index_or_alias = self.sessionIndex[i]
		try:
			session = self.sessionMap[index_or_alias]
			self.session = session
		except Exception:
			raise Exception('Invalid alias: ' + str(index_or_alias))

	def closeSession(self, index_or_alias=None):
		global session
		if index_or_alias != None:
			self.switchSession(index_or_alias)
		session.close()

	def closeAllSessions(self):
		global sessionMap
		global sessionIndex
		global index
		for key, ss in self.sessionMap.items():
			ss.close()
		self.sessionMap = {}
		self.sessionIndex = {}
		self.index = 1
	
	def _writeLog(self, steps):
		global log_level
		if log_level == 'INFO' or log_level == 'DEBUG':
			logger.write(steps, level=log_level, html=False)

	def _formResponse(self, response):
		if response.json != None:
			return response.json
		else:
			responseDictionary = {'text' : response.text.strip()}
			responseQueryList = eval(response.queries())
			for key in responseQueryList:
				try:
					responseDictionary[re.sub('[()]','',key)] = eval('response.' + key)
				except Exception:
					logger.debug('Can not get query ' + key)
			return responseDictionary

	def __init__(self):
		self._description = 'common library'
		self.sessionMap = {}
		self.sessionIndex = {}
		self.index = 1
		
	def _getSession(self):
		global session
		return session

	def _representsInt(self, s):
		try: 
			int(s)
			return True
		except ValueError:
			return False
