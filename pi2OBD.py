#pi2OBD ~interface between pi2go and the OBD sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R0

import sys
from optparse import OptionParser

import obd
from obd.message import OBDRequest
from obd.util import untested
import obd.util

class pi2OBD:
	
	def __init__(self):
		#SetOBD #Find the scan tools attached to the computer and pick one
		"""self.interfaces = obd.interface.elm.enumerate()
		self.interface = self.interfaces[0]
	
		# Open the connection with the vehicle
		self.interface.open()
		self.interface.set_protocol(None)
		self.interface.connect_to_vehicle()"""
		pass
		
	def OBDinter(self):
		#Will grab all possible ports
		pass
	
	def OBDread(self):
		#Super basic function....just grabing a singal value for now
		#rpmValue = obd_sensors.rpm(code)e
		# Communicate with the vehicle
		"""request = obd.message.OBDRequest(sid=0x01, pid=0x00)
		responses = interface.send_request(request)""" #TODO working on
		return 123 #test rpm value
		
if __name__ == "__main__":
	pass
