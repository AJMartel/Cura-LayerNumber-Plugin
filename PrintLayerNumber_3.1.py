# This PostProcessing Plugin script is released 
# under the terms of the AGPLv3 or higher

from ..Script import Script
#from UM.Logger import Logger
# from cura.Settings.ExtruderManager import ExtruderManager

class PrintLayerNumber(Script):
	def __init__(self):
		super().__init__()

	def getSettingDataString(self):
		return """{
			"name":"PrintLayerNumber",
			"key": "PrintLayerNumber",
			"metadata": {},
			"version": 2,
			"settings": {}
		}"""

	def execute(self, data: list):
		count = len(data) - 3
		for i in range(count):
			if i > 1:
				data[i] = ("M117 Layer %d/%d\n" % (i - 1, count)) + data[i];

		return data
