#pi2OBD ~interface between pi2go and the OBD sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R1

import serial
import string
import time

class pi2OBD:

	def __init__(self):
			self.serialIO = serial.Serial('/dev/rfcomm0', 38400, timeout=1)

	def speed(self):
		"""Grabs speed of vehicle"""
		self.serialIO.write("01 0D \r")
		speed_list = self.serialIO.readline().split(' ')
		speed_hex = speed_list[0][4:6]
		print speed_hex
		speed_float = float(int("0x"+speed_hex, 0))
		
		speed_float = speed_float*0.621371	#Comment out if you would rather have Kph
		return speed_float
	
	def rpm(self):
		"""Grabs RPM of Engine"""
		self.serialIO.write("01 0C \r")
		rpm_list = self.serialIO.readline().split(' ')
		rpm_value = []
		rpm_value.append(rpm_list[0][4:6])
		rpm_value.append(rpm_list[0][6:8])
		
		rpm_value[0] = float(int("0x"+rpm_value[0], 0))
		rpm_value[1] = float(int("0x"+rpm_value[1], 0))
		
		#Calulate RPM
		rpm_final = ((rpm_value[0]*256)+rpm_value[1])*.25
		return rpm_final
		
	def OBDread(self):
		finalValues = [0,0] # [speed, rpm] #TODO maybe dictionary
		while(1):
			finalValues[0] = self.speed()
			finalValues[1] = self.rpm()
			return finalValues
		
		
if __name__ == "__main__":
	test = pi2OBD()
	test.OBDread()
	
