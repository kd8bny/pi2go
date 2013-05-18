#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V0 R0
import sys
import os

from PyQt4 import *
#TODO whe GUI is in place ~from main import *
class fotoShoot(): #TODO GUI ~QtGui.QMainWindow
	def__init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.mainDir = 0
        self.pause = self.ui.spinBox.value()
