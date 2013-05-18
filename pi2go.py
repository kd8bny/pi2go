#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R0
import sys
import os

from PyQt4 import *
from main import *
import RPi.GPIO as GPIO

class pi2go(QtGui.QMainWindow):

	F_lights = 17
	A_Lights = 22 
    
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		#Set buttons
		QtCore.QObject.connect(self.ui.F_lights, QtCore.SIGNAL("clicked()"), self.fogL)	#browse button
		QtCore.QObject.connect(self.ui.A_lights, QtCore.SIGNAL("clicked()"), self.fancy)	#browse button
		
		#Set logo
		self.scene = QtGui.QGraphicsScene(self)
		self.scene.addPixmap(QtGui.QPixmap('graphics/pi_logo.jpeg'))
		self.ui.graphicsView.setScene(self.scene)
		
		#Set Hardware TODO Make class is enough features are introduced
		GPIO.setup(self.F_lights, GPIO.OUT)
		GPIO.setup(self.A_lights, GPIO.OUT)
		GPIO.output(self.F_lights, False)
		GPIO.output(self.A_lights, False)
		
	def fogL(self):	#Will turn fog ligths on and off
			if(self.F_lights==False):
				GPIO.output(self.F_lights, True)
			else:
				GPIO.output(self.F_lights, False)
		
	def fancy(self):	#Will turn fog ligths on and off
		if(self.A_lights==False):
				GPIO.output(self.A_lights, True)
			else:
				GPIO.output(self.A_lights, False)		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
