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

import sys, os, time, numpy
import PyQt4
import PyQt4.Qwt5 as Qwt
from PyQt4.Qwt5.anynumpy import *

import config, pi2OBD, pi2log #,sOff
from main import *

try:
    import RPi.GPIO as GPIO
except:
    "Missing RPi.GPIO"
    pass


class pi2go(QtGui.QMainWindow):

    OBDsignal = QtCore.pyqtSignal([list], name='OBDsignal')

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Qt4
        #Welcome Tab
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.addPixmap(QtGui.QPixmap('../graphics/pi_logo.jpeg'))
        self.ui.welcome.setScene(self.scene)

        self.piClocktimer = QtCore.QTimer()
        QtCore.QObject.connect(self.piClocktimer, QtCore.SIGNAL("timeout()"), self.ui.AnalogClock, QtCore.SLOT("setCurrentTime()"))
        self.piClocktimer.start(1000)
        
        #OBDII Tab
        self.OBDsignal.connect(self.updateGUI)
        QtCore.QObject.connect(self.ui.obdButton, QtCore.SIGNAL("clicked()"), self.ODBII)
        QtCore.QObject.connect(self.ui.obdClear, QtCore.SIGNAL("clicked()"), (lambda : pi2OBD.pi2OBD().clearCodes()))
        self.stopOBD = True #init stopped

        #GPS Tab
        QtCore.QObject.connect(self.ui.GPSbutton, QtCore.SIGNAL("clicked()"), self.GPS)
        self.stopGPS = False

        #Maintenance Tab
        #New
        self.ui.caredateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        QtCore.QObject.connect(self.ui.commentcheckBox, QtCore.SIGNAL("toggled(bool)"), (lambda show=True : self.ui.careComments.setHidden(not show)))
        QtCore.QObject.connect(self.ui.logCare, QtCore.SIGNAL("clicked()"), (lambda reset=False : self.logCare(reset)))
        QtCore.QObject.connect(self.ui.resetCare, QtCore.SIGNAL("clicked()"), (lambda reset=True : self.logCare(reset)))
        #Last
        self.logCare_last()
        QtCore.QObject.connect(self.ui.deleteLast, QtCore.SIGNAL("clicked()"), (lambda : pi2log.pi2log().delLast()))
        
        #Settings Tab
        ## OBDII
        QtCore.QObject.connect(self.ui.spinBox_ATSP, QtCore.SIGNAL("valueChanged(int)"), (lambda label='atsp' : self.settings(label)))

        QtCore.QObject.connect(self.ui.btRadio, QtCore.SIGNAL("clicked()"), (lambda label='bt' : self.settings(label)))
        QtCore.QObject.connect(self.ui.usbRadio, QtCore.SIGNAL("clicked()"), (lambda label='usb' : self.settings(label)))
        QtCore.QObject.connect(self.ui.devRadio, QtCore.SIGNAL("clicked()"), (lambda label='dev' : self.settings(label)))

        QtCore.QObject.connect(self.ui.units_metric_radio, QtCore.SIGNAL("clicked()"), (lambda label='metric' : self.settings(label)))
        QtCore.QObject.connect(self.ui.units_US_radio, QtCore.SIGNAL("clicked()"), (lambda label='US' : self.settings(label)))    
        
        #self.plot()    

#################################################################################################################
    def ODBII(self):
        """Starts to read the ODB data"""
        self.stopOBD = not self.stopOBD
        while not self.stopOBD:
            self.ui.obdButton.setText("Stop")
            OBDvalues = pi2OBD.pi2OBD().OBDread() 
            self.OBDsignal.emit(OBDvalues)
            PyQt4.QtCore.QCoreApplication.processEvents() #self.update() self.ui
            
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

    def plot(self):
         # Initialize data
        x = arange(0.0, 100.1, 0.5)
        y = arange(0.0, 100.1, 0.5)
        z = arange(50, 0.0, 0.5)

        curveR = Qwt.QwtPlotCurve("Data Moving Right")
        curveR.attach(self.ui.OBDplot)
        curveL = Qwt.QwtPlotCurve("Data Moving Left")
        curveL.attach(self.ui.OBDplot)


        curveL.setSymbol(Qwt.QwtSymbol(Qwt.QwtSymbol.Ellipse,
                                        QtGui.QBrush(),
                                        QtGui.QPen(PyQt4.QtGui.QColor('yellow')),
                                        QtCore.QSize(7, 7)))

        curveR.setPen(QtGui.QPen(PyQt4.QtGui.QColor('red')))
        curveL.setPen(QtGui.QPen(PyQt4.QtGui.QColor('blue')))

        mY = Qwt.QwtPlotMarker()
        mY.setLabelAlignment(PyQt4.QtCore.Qt.AlignRight | PyQt4.QtCore.Qt.AlignTop)
        mY.setLineStyle(Qwt.QwtPlotMarker.HLine)
        mY.setYValue(0.0)
        mY.attach(self.ui.OBDplot)

        self.ui.OBDplot.setAxisTitle(Qwt.QwtPlot.xBottom, "Time (seconds)")
        self.ui.OBDplot.setAxisTitle(Qwt.QwtPlot.yLeft, "Values")


        curveR.setData(x, y)
        curveL.setData(x, z)

        self.ui.OBDplot.replot()

        return

####################################################################################################
    def GPS(self):
        if not self.GPS:
            self.ui.GPSbutton.setText("Stop")           
        else:
            self.ui.GPSbutton.setText("Start")
        self.stopGPS = not self.stopGPS

        return

####################################################################################################
    def logCare(self, reset):
        """Log Maintenance values into spreadsheet: [date, task, odo, comments]"""
        logValues = []
        if reset:
            self.ui.careOdo.clear()
            self.ui.careComments.clear()

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
            pi2log.pi2log().addData(logValues) 
            self.logCare_last()

        return

    def logCare_last(self):
        """Calls function read last line -> updates GUI"""
        careValues = pi2log.pi2log().readLast()
        self.ui.date_output.setText(careValues[0])
        self.ui.task_output.setText(careValues[1]) 
        self.ui.odo_output.setText(careValues[2]) 
        self.ui.comment_output.setText(careValues[3])  

        return

####################################################################################################
    def settings(self, label):
        """Function of the settings tab"""       
        if label == 'bt':
            try:
                config.serialDevice = 'rfcomm0'
                os.system("blueman-manager")
            except:
                print "Please install 'blueman' package"
        elif label == 'usb':
            config.serialDevice = '/dev/ttyUSB0'
        elif label == 'dev':
            config.serialDevice = '/dev/pts/5'
        elif label == 'metric':
            config.units = 'metric'
        elif label == 'us':
            config.units = 'US'            
        else: #ATSP signal return int -> else
            config.ATSP = self.ui.spinBox_ATSP.value()

        return    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
