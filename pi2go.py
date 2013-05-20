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

#V1 R0
import sys
import os

from PyQt4 import *
from main import *
from pi2OBD import *
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
		
		#Set Hardware TODO Make class is enough features are introduced
		"""GPIO.setup(self.F_lights, GPIO.OUT)
		GPIO.setup(self.A_lights, GPIO.OUT)
		GPIO.output(self.F_lights, GPIO.LOW)
		GPIO.output(self.A_lights, GPIO.LOW)"""
		
	def fogL(self):	#Will turn fog ligths on and off
		"""if(self.F_lights==GPIO.LOW):
			GPIO.output(self.F_lights, GPIO.HIGH)
		else:
			GPIO.output(self.F_lights, GPIO.LOW)"""
		pass
	def fancy(self):	#Will turn fog ligths on and off
		"""if(self.A_lights==GPIO.LOW):
			GPIO.output(self.A_lights, GPIO.HIGH)
		else:
			GPIO.output(self.A_lights, GPIO.LOW)"""
		pass
	
	def obdStart(self):
		self.OBD = pi2OBD()
		self.OBDValue = self.OBD.OBDread()
		print "made it here"
		self.ui.lcdNumber.display(self.OBDValue)
		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
