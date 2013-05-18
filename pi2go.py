#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V0 R0
import sys
import os

from PyQt4 import *
from main import *

class fotoShoot(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
