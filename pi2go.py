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

#V1 R5

import sys, os, threading, PyQt4
import PyQt4.Qwt5 as Qwt
import pi2OBD #,sOff
from main import *

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
			print 'Heads up: No GPIO Connection'


		#QT 4
		#Welcome tab
		self.scene = QtGui.QGraphicsScene(self)
		self.scene.addPixmap(QtGui.QPixmap('graphics/pi_logo.jpeg'))
		self.ui.welcome.setScene(self.scene)

		self.ui.AnalogClock.setCurrentTime()
		#Car Tab
		QtCore.QObject.connect(self.ui.F_lights, QtCore.SIGNAL("clicked()"), self.fogL)	#fog lights
		QtCore.QObject.connect(self.ui.A_lights, QtCore.SIGNAL("clicked()"), self.fancy)	#Accent lights
		#OBD Tab
		QtCore.QObject.connect(self.ui.obdButton, QtCore.SIGNAL("clicked()"), self.ODBII)	#Start/kill OBD
		self.stopOBD = False
		#GPS tab
		QtCore.QObject.connect(self.ui.logGPS, QtCore.SIGNAL("clicked()"), self.logGPS)
		QtCore.QObject.connect(self.ui.GPSbutton, QtCore.SIGNAL("clicked()"), self.GPS)
		self.stopGPS = False
		#Settings tab
		QtCore.QObject.connect(self.ui.pushButton_bt, QtCore.SIGNAL("clicked()"), self.blueman)	#Start Blueman
		QtCore.QObject.connect(self.ui.obdClear, QtCore.SIGNAL("clicked()"), self.clearCodes) #clear codes
		QtCore.QObject.connect(self.ui.spinBox_ATSP, QtCore.SIGNAL("valueChanged(int)"), self.settings)	#ATSP Value
		

#################################################################################################################		
		
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

#################################################################################################################	
	def ODBII(self):
		"""Starts to read the ODB data"""
		if not self.stopOBD:
			self.ui.obdButton.setText("Stop")
			pi2OBD.pi2OBD().main(False)
			while not self.stopOBD:
				obdTemp = open('obdTemp.txt', 'r')
				values = obdTemp.readline().split(',')	#TODO When readline is null Still need to know line numbers
				# receive [speed, rpm, intake, coolant, load]
				self.ui.lcdNumber_speed.display(values[0])
				self.ui.lcdNumber_rpm.display(values[1])
				self.ui.lcdNumber_inTemp.display(values[2])
				self.ui.lcdNumber_coolTemp.display(values[3])
				self.ui.lcdNumber_load.display(values[4])
		else:
			self.ui.obdButton.setText("Start")
			pi2OBD.pi2OBD().main(True)	
		'''#Start thread
		qtgui.QApplication.processEvents() #Writes all pending changes to QT
		self.wait(1)
		updateThread = threading.Thread(target = self.updateThread)
		updateThread.start()'''
		self.stopOBD = not self.stopOBD #toggle value
		return
		
	def clearCodes(self):
		"""Clear all trouble codes"""
		self.OBD.clear_codes()

####################################################################################################
	def GPS(self):
		if not self.GPS:
			self.ui.GPSbutton.setText("Stop")			
		else:
			self.ui.GPSbutton.setText("Start")
		self.stopGPS = not self.stopGPS #toggle value

	def logGPS(self):
		pass
####################################################################################################

	def settings(self):
		"""Function of the settings tab"""
		self.ATSP = self.ui.spinBox_ATSP.value()
		
	def blueman(self):
		"""Starts blueman-manager"""
		try:
			os.system("blueman-manager")
		except:
			print "Please install 'blueman' package"		


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
