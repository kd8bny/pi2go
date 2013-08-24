#guiThreading ~Seperate thread to process OBD events
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Prupose is to have a DIY in car computer using RPi

#V1 R2
import PyQt4.QtCore as qtcore
import PyQt4.QtGui as qtgui
from pi2OBD import pi2OBD

class Worker(qtcore.QThread):

	def __init__(self, parent = None):
		qtcore.QThread.__init__(self, parent)
		self.signal = qtcore.SIGNAL("signal")
		
		self.OBD = pi2OBD()
		self.toKill = False
		self.isFirst = True	
		         
	def update(self,kill):
		"""Updates GUI"""
		self.toKill = kill
		self.start()

		if self.isFirst:
			obdValue = self.OBD.setup()

		while not (self.toKill):
			self.isFirst = False
			obdValue = self.OBD.OBDread()
			self.emit(qtcore.SIGNAL('obdValue[int,int,int,int,int]'), obdValue)
			qtgui.QApplication.processEvents() #Writes all pending changes to QT
			self.wait(1)
		self.quit()
			
	def kill(self,kill):
		self.toKill = kill
		return self.toKill
			
			
	def __del__(self):
		self.wait()
        
if __name__ == "__main__":
	update()
