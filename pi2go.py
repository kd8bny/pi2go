####   #  ####  #####    ####
#   #        #  #       #    #
####   #  ####  #  ###  #    #
#      #  #     #   ##  #    #
#      #  ####  #####    ####
###############################
#In car use of the raspberry pi
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a DIY in car computer using RPi
#TODO port back to RPi disabled now in order for serial testing

#V1 R5

import sys, os, threading, PyQt4, time
import PyQt4.Qwt5 as Qwt
import pi2OBD, config #,sOff
from main import *

try:
    import RPi.GPIO as GPIO
except:
    print "Developmental Use Only"
    pass


class pi2go(QtGui.QMainWindow):

    OBDsignal = QtCore.pyqtSignal([list], name='OBDsignal')

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        try:
            #Set Hardware TODO Make class is enough features are introduced
            GPIO.setmode(GPIO.BCM)
            self.F_lights = 17
            self.A_lights = 22
            GPIO.setup(self.F_lights, GPIO.OUT)
            GPIO.setup(self.A_lights, GPIO.OUT)
            GPIO.output(self.F_lights, GPIO.LOW)    ; self.F_state = False
            GPIO.output(self.A_lights, GPIO.LOW)    ; self.A_state = False
        except:
            print 'Heads up: No GPIO Connection'


        #Qt4
        #Welcome Tab
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.addPixmap(QtGui.QPixmap('graphics/pi_logo.jpeg'))
        self.ui.welcome.setScene(self.scene)

        self.piClocktimer = QtCore.QTimer()
        QtCore.QObject.connect(self.piClocktimer, QtCore.SIGNAL("timeout()"), self.ui.AnalogClock, QtCore.SLOT("setCurrentTime()"))
        self.piClocktimer.start(1000)

        #Car Tab
        QtCore.QObject.connect(self.ui.F_lights, QtCore.SIGNAL("clicked()"), self.fogL) #fog lights
        QtCore.QObject.connect(self.ui.A_lights, QtCore.SIGNAL("clicked()"), self.fancy)    #Accent lights
        
        #OBDII Tab
        self.OBDsignal.connect(self.updateGUI)
        QtCore.QObject.connect(self.ui.obdButton, QtCore.SIGNAL("clicked()"), self.ODBII)   #Start/kill OBD
        QtCore.QObject.connect(self.ui.obdClear, QtCore.SIGNAL("clicked()"), self.clearCodes) #clear codes
        self.stopOBD = True #init stopped

        #GPS Tab
        QtCore.QObject.connect(self.ui.logGPS, QtCore.SIGNAL("clicked()"), self.logGPS)
        QtCore.QObject.connect(self.ui.GPSbutton, QtCore.SIGNAL("clicked()"), self.GPS)
        self.stopGPS = False

        #Maintenance Tab
        QtCore.QObject.connect(self.ui.logCare, QtCore.SIGNAL("clicked()"), (lambda reset=False : self.logCare(reset))) #Pass reset field
        QtCore.QObject.connect(self.ui.resetCare, QtCore.SIGNAL("clicked()"), (lambda reset=True : self.logCare(reset)))
        
        #Settings Tab
        QtCore.QObject.connect(self.ui.pushButton_bt, QtCore.SIGNAL("clicked()"), self.blueman) #Start Blueman
        QtCore.QObject.connect(self.ui.spinBox_ATSP, QtCore.SIGNAL("valueChanged(int)"), self.settings) #ATSP Value
        
        if self.ui.btRadio.isChecked():
            config.serialDevice = 'rfcomm0'
        if self.ui.usbRadio.isChecked():
            config.serialDevice = '/dev/ttyUSB0'
        else:
            config.serialDevice = '/dev/pts/5'
            
        

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
        self.stopOBD = not self.stopOBD
        OBDvalues = [0, 0, 0, 0, 0]
        while not self.stopOBD:
            self.ui.obdButton.setText("Stop")
            OBDvalues = pi2OBD.pi2OBD().OBDread() 
            self.OBDsignal.emit(OBDvalues)
            PyQt4.QtCore.QCoreApplication.processEvents()
            
        self.ui.obdButton.setText("Start")
        self.OBDsignal.emit(OBDvalues)

        return

    def updateGUI(self):
        """Update LCD values in QT: receive [speed, rpm, intake, coolant, load]"""
        self.ui.lcdNumber_speed.display(OBDvalues[0])
        self.ui.lcdNumber_rpm.display(OBDvalues[1])
        self.ui.lcdNumber_inTemp.display(OBDvalues[2])
        self.ui.lcdNumber_coolTemp.display(OBDvalues[3])
        self.ui.lcdNumber_load.display(OBDvalues[4])
        time.sleep(config.refresh)

        return

    def clearCodes(self):
        """Clear all trouble codes"""
        pi2OBD.pi2OBD.clear_codes()

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

    def logCare(self, reset):
        """Log Maintenance values into spreadsheet: [date, task, odo, comments]"""
        logValues = []
        if reset:
            self.ui.careOdo.clear()

        else:
            tempQDate = self.ui.caredateEdit.date()
            tempPyDate = str(tempQDate.toPyDate())
            tempTask = str(self.ui.careTask.currentText())
            tempOdo = str(self.ui.careOdo.text())
            tempComment = str(self.ui.careComments.toPlainText())

            logValues.insert(0, tempPyDate)
            logValues.insert(1, tempTask)
            logValues.insert(2, tempOdo)
            logValues.insert(3, tempComment)             

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
