#pi2OBD ~interface between pi2go and the OBD sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V2 R0a

import serial, string, time, threading
from PyQt4.QtCore import *
from main import *

class pi2OBD(QObject):
	global serialDevice

	def __init__(self):
		QObject.__init__(self)

		try:
			self.serialIO = serial.Serial(serialDevice, 38400, timeout=1)
		except:
			print "Serial Issue"

		#Datafile setup
		self.obdTemp = open('obdTemp.txt', 'w')

		#Thread Info
		self.signal = SIGNAL("signal")
		self.toKill = False
		self.isFirst = True
		
	def speed(self):
		"""Grabs speed of vehicle"""
		self.serialIO.write("01 0D \r")
		speed_list = self.serialIO.readline().split(' ')
		speed_hex = speed_list[0][4:6]
		try:
			speed_float = float(int("0x"+speed_hex, 0))
		except:
			return 0
		
		speed_float = speed_float*0.621371	#Comment out if you would rather have Kph
		return speed_float
	
	def rpm(self):
		"""Grabs RPM of Engine"""
		self.serialIO.write("01 0C \r")
		rpm_list = self.serialIO.readline().split(' ')
		rpm_value = []
		rpm_value.append(rpm_list[0][4:6])
		rpm_value.append(rpm_list[0][6:8])
		try:
			rpm_value[0] = float(int("0x"+rpm_value[0], 0))
			rpm_value[1] = float(int("0x"+rpm_value[1], 0))
		except:
			return 0
			
		#Calulate RPM
		rpm_final = ((rpm_value[0]*256)+rpm_value[1])*.25
		return rpm_final
		
	def intake_temp(self):
		"""Grabs Intake Air temp (Temp outside)"""
		self.serialIO.write("01 0F \r")
		temp_list = self.serialIO.readline().split(' ')
		temp_hex = temp_list[0][4:6]
		try:
			temp_float = float(int("0x"+temp_hex, 0))
		except:
			return 0
			
		temp_final = temp_float-40	
		temp_final = temp_final*(9/5)+32	#Comment out if you would rather have deg C 
		return temp_final
		
	def coolant_temp(self):
		"""Grabs Intake Air temp (Temp outside)"""
		self.serialIO.write("01 05 \r")
		temp_list = self.serialIO.readline().split(' ')
		temp_hex = temp_list[0][4:6]
		try:
			temp_float = float(int("0x"+temp_hex, 0))
		except:
			return 0
			
		temp_final = temp_float-40
		temp_final = temp_final*(9/5)+32	#Comment out if you would rather have deg C
		return temp_final
		
	def load(self):
		"""Grabs Total Engine Load"""
		self.serialIO.write("01 04 \r")
		load_list = self.serialIO.readline().split(' ')
		load_hex = load_list[0][4:6]
		try:
			load_float = float(int("0x"+load_hex, 0))
		except:
			return 0
			
		load_final = (load_float*100)/255
		return load_final
		
	def run_time(self):	#TODO
		"""Will grab amount of time engine has been running"""
		self.serialIO.write("01 7F \r")
		temp_list = self.serialIO.readline().split(' ')
		pass
		
	def OBDread(self):
		"""Function to read and write data"""
		try:
			self.obdTemp.write(str(self.speed())+',')
			self.obdTemp.write(str(self.rpm())+',')
			self.obdTemp.write(str(self.intake_temp())+',')
			self.obdTemp.write(str(self.coolant_temp())+',')
			self.obdTemp.write(str(self.load())+','+'\n')
		finally:
			self.obdTemp.close()
		return 
		
	def clear_codes(self):	#TODO Will add to own class when working with codes
		"""Clear all trouble codes"""
		self.serialIO.write("04")

	def setup(self):
		"""Set up OBD Comm"""
		self.serialIO.write("ATZ \r")
		time.sleep(2)
		self.serialIO.write("ATSP %d \r" %pi2go.ATSP)
		time.sleep(.5)
		self.serialIO.readline().split(' ')
		self.serialIO.write("01 00 \r")
		time.sleep(.5)
		return

	def main(self,kill):
		"""Formats OBDII data"""

		if self.isFirst:
			obdValue = self.setup()
			self.isFirst = False
			self.updateThread()

		#Start thread
		obdThread = threading.Thread(target = self.main)
		obdThread.start()

		while not (kill):
			if(self.obdTemp.tell() > 2000):	#100 lines of data @20char
				self.obdTemp.seek(0)
			else:
				self.wait(1)
		self.updateThread.quit()
		self.quit()
		
if __name__ == "__main__":
	test = pi2OBD()
	test.main(False)
	