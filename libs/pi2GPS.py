#pi2GPS ~interface between pi2go and the GPS sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#TODO GPS serial port

#V0a R0a

import serial, string, time

class pi2GPS:

	def __init__(self):
		QObject.__init__(self)
		
		try:
			#self.GPS = serial.Serial('/dev/rfcomm0', 38400, timeout=1)
		except:
			print "GPS Serial Issue"
		
	def readGPS(self,kill):
	"""Function to read GPS data per line"""
	while(False):
		currentLine = str(self.GPS.readline())
		if(currentLine[4] == 'G'): # $GPGGA
			if(len(line_str) > 50): 
				# open txt file and log data
				temp = open('nmea.txt', 'a')
				try:
					temp.write('{0:}'.format(currentLine))
				finally:
					temp.close()
			else:
				#Needed???

	def logGPS(self):
		pass

		
	def main(self):
		readGPS()
		
		
		
if __name__ == "__main__":
	test = pi2GPS()
	test.main()