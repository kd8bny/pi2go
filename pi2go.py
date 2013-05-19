#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi
#TODO port back to RPi disabled now in order for serial testing

#V1 R0
import sys
import os

from PyQt4 import *
from main import *
from obd import *
import obd.message.request
#import RPi.GPIO as GPIO

class pi2go(QtGui.QMainWindow):

	F_lights = 17
	A_Lights = 22 
    
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		#Set buttons
		QtCore.QObject.connect(self.ui.F_lights, QtCore.SIGNAL("clicked()"), self.fogL)	#fog lights
		QtCore.QObject.connect(self.ui.A_lights, QtCore.SIGNAL("clicked()"), self.fancy)	#Accent lights
		QtCore.QObject.connect(self.ui.obdStart, QtCore.SIGNAL("clicked()"), self.obdStart)	#Start OBD
		
		#Set logo
		self.scene = QtGui.QGraphicsScene(self)
		self.scene.addPixmap(QtGui.QPixmap('graphics/pi_logo.jpeg'))
		self.ui.graphicsView.setScene(self.scene)
		
		#SetOBD #Find the scan tools attached to the computer and pick one
		self.interfaces = obd.interface.enumerate()
		self.interface = self.interfaces[0]
		# Open the connection with the vehicle
		interface.open()
		interface.set_protocol(None)
		interface.connect_to_vehicle()
		
		#Set Hardware TODO Make class is enough features are introduced
		#GPIO.setup(self.F_lights, GPIO.OUT)
		#GPIO.setup(self.A_lights, GPIO.OUT)
		#GPIO.output(self.F_lights, False)
		#GPIO.output(self.A_lights, False)
		
	def fogL(self):	#Will turn fog ligths on and off
		#if(self.F_lights==False):
		#	GPIO.output(self.F_lights, True)
		#else:
		#	GPIO.output(self.F_lights, False)
		pass
	def fancy(self):	#Will turn fog ligths on and off
		"""if(self.A_lights==False):
			GPIO.output(self.A_lights, True)
		else:
			GPIO.output(self.A_lights, False)"""
		pass
	
	def obdStart(self):
		#Super basic function....just grabing a singal value for now
		#rpmValue = obd_sensors.rpm(code)e
		self.ui.lcdNumber.display(000)
		# Communicate with the vehicle
		request = obd.message.OBDRequest(sid=0x01, pid=0x00)
		responses = interface.send_request(request)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
