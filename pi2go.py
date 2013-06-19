####   #  ####  #####    ####
#   #        #  #       #    #
####   #  ####  #  ###  #    #
#      #  #     #   ##  #    #
#      #  ####  #####    ####
###############################
#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi
#TODO port back to RPi disabled now in order for serial testing

#V1 R2
import sys
import os
from PyQt4 import *
from main import *
import threading
#from sOff import sOff

from guiThreading import *

try:
	import RPi.GPIO as GPIO
except:
	pass


class pi2go(QtGui.QMainWindow):
    
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		#Used by pi2go	
		#self.sOff = sOff()
		
		try:
			#Set Hardware TODO Make class is enough features are introduced
			GPIO.setmode(GPIO.BCM)
			self.F_lights = 17
			self.A_lights = 22
			GPIO.setup(self.F_lights, GPIO.OUT)
			GPIO.setup(self.A_lights, GPIO.OUT)
			GPIO.output(self.F_lights, GPIO.LOW)	; self.F_state = False
			GPIO.output(self.A_lights, GPIO.LOW)	; self.A_state = False
		except:
			pass

		#QT 4
		QtCore.QObject.connect(self.ui.F_lights, QtCore.SIGNAL("clicked()"), self.fogL)	#fog lights
		QtCore.QObject.connect(self.ui.A_lights, QtCore.SIGNAL("clicked()"), self.fancy)	#Accent lights
		QtCore.QObject.connect(self.ui.obdStart, QtCore.SIGNAL("clicked()"), self.obdStart)	#Start OBD
		QtCore.QObject.connect(self.ui.obdKill, QtCore.SIGNAL("clicked()"), self.obdKill)	#Kill OBD
		QtCore.QObject.connect(self.ui.obdClear, QtCore.SIGNAL("clicked()"), self.clearCodes) #clear codes
		self.guiThread = Worker()	#This is a Qthread
		
		#Set logo
		self.scene = QtGui.QGraphicsScene(self)
		self.scene.addPixmap(QtGui.QPixmap('graphics/pi_logo.jpeg'))
		self.ui.graphicsView.setScene(self.scene)
		
	def fogL(self):	
		"""Will turn fog ligths on and off"""
		if(self.F_state is False ):
			GPIO.output(self.F_lights, GPIO.HIGH)
			self.F_state = True
		else:
			GPIO.output(self.F_lights, GPIO.LOW)
			self.F_state = False
		return 

	def fancy(self):
		"""Will turn fog ligths on and off"""
		if(self.A_state is False):
			GPIO.output(self.A_lights, GPIO.HIGH)
			self.A_state = True
		else:
			GPIO.output(self.A_lights, GPIO.LOW)
			self.A_state = False
		return
		
	def obdKill(self):
		#self.obdStart.setEnabled(True)
		self.guiThread.update(True)
		return
	
	def obdStart(self):
		"""Starts to read the ODB sensor"""
		#self.obdStart.setEnabled(False)
		self.guiThread.update(False)
		return
		
	def write_to_UI(self,values):
		"""Updates the UI with new values"""
		# receive [speed, rpm, intake, coolant, load]
		self.ui.lcdNumber_speed.display(values[0])
		self.ui.lcdNumber_rpm.display(values[1])
		self.ui.lcdNumber_inTemp.display(values[2])
		self.ui.lcdNumber_coolTemp.display(values[3])
		self.ui.lcdNumber_load.display(values[4])
		QtGui.QApplication.processEvents() #Writes all pending changes to QT
		return
		
		
	def clearCodes(self):
		"""Clear all trouble codes"""
		self.OBD.clear_codes()
		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
