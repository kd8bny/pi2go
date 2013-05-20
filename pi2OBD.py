#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi
#TODO port back to RPi disabled now in order for serial testing

#V0 R0

from obd import *
from obd.interface import *
from obd.message import *	#revert later

class pi2OBD:
	
	def __init__(self):
		#SetOBD #Find the scan tools attached to the computer and pick one
		self.interfaces = obd.interface.elm.enumerate()
		self.interface = self.interfaces[0]
	
		# Open the connection with the vehicle
		self.interface.open()
		self.interface.set_protocol(None)
		self.interface.connect_to_vehicle()
	
	def OBDread(self):
		#Super basic function....just grabing a singal value for now
		#rpmValue = obd_sensors.rpm(code)e
		# Communicate with the vehicle
		"""request = obd.message.OBDRequest(sid=0x01, pid=0x00)
		responses = interface.send_request(request)""" #TODO working on
		return 000
		
if __name__ == "__main__":
	pass
