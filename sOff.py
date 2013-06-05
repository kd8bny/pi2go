#sOff ~Safely shutsdown RPi when car shutdown
###################################################
#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R0
import os
import threading
import RPi.GPIO as GPIO
class sOff:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.smartOff = 23
 		GPIO.setup(self.smartOff, GPIO.IN)
 		
 		#Create Thread
 		self.sOff_thread = Thread(target=self.turnOff()) #TODO try: exception: 
		self.sOff_event = Event()
		self.sOff_thread.start()

		
	def shutdown(self):	#TODO kill thread
		"""Shutdown RPi safely"""
		os.system( "shutdown now -h -k" )
		
	
	def getState(self, sOff_state = True):
		"""Grabs the key_on state"""
		while(sOff_state):
			if(GPIO.input(self.smartOff) is False):
				for aThread in threading.enumerate():	#All alive threads
					self.sOff_event.set()
				self.shutdown()
			else:
				self.sOff_thread.wait(120)
		
if __name__ == "__main__":
	getState()
