#pi2GPS ~interface between pi2go and the GPS sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V0a R0a

import serial, string, time

class pi2GPS:

	def __init__(self):
		try:
			#TODO GPS serial port
			#self.GPS = serial.Serial('/dev/rfcomm0', 38400, timeout=1)
		except:
			print "GPS Serial Issue"
		
	def readGPS(self):
	#this fxn creates a txt file and saves only GPGGA sentences
	while 1:
		line = ser.readline()
		line_str = str(line)
		if(line_str[4] == 'G'): # $GPGGA
			if(len(line_str) > 50): 
				# open txt file and log data
				f = open('nmea.txt', 'a')
				try:
					f.write('{0:}'.format(line_str))
				finally:
					f.close()
			else:
				stream_serial()

	def logGPS(self):
		pass

		
	def main(self):
		readGPS()
		
		
		
if __name__ == "__main__":
	test = pi2GPS()
	test.main()