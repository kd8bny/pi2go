#guiThreading ~Seperate thread to process OBD events
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R0
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pi2OBD import pi2OBD
import time

class Worker(QThread):

	def __init__(self, parent = None):
		QThread.__init__(self, parent)
		self.OBD = pi2OBD()
        
	def update(self,kill):
		"""Updates GUI"""
		self.start()
		while not (kill):	
			obdValue = self.OBD.OBDread()
			self.ui.lcdNumber_speed.display(values[0])
			self.ui.lcdNumber_rpm.display(values[1])
			self.ui.lcdNumber_inTemp.display(values[2])
			self.ui.lcdNumber_coolTemp.display(values[3])
			self.ui.lcdNumber_load.display(values[4])
			time.sleep(5)
		if(kill):
			self.quit()
			
	def __del__(self):
		self.wait()
        
if __name__ == "__main__":
	update()
