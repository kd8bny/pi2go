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

import sys, os, time, pickle #apscheduler.scheduler
import PyQt4
import PyQt4.Qwt5 as Qwt

import config, pi2OBD, pi2log #,sOff
from main import *
import search as searchDialog_ui
import error as errorDialog_ui


class pi2go(QtGui.QMainWindow):

    OBDsignal = QtCore.pyqtSignal([list], name='OBDsignal')
    #careCheck_sched = apscheduler.scheduler.Scheduler()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Qt4      
        #All
        ## Default
        self.default = config.config().loadSave()
        ## Error
        self.ui.careStatus.clicked.connect((lambda : errorDialog().display()))
        self.ui.careStatus.clicked.connect((lambda : careCheck()))
        ## Scheduler
        #self.careCheck_sched.add_cron_job(self.careCheck, day_of_week='0-6') # Will decrease after testing
        #self.careCheck_sched.start() 

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
        self.stopOBD = True #init stopped

        #GPS Tab
        QtCore.QObject.connect(self.ui.GPSbutton, QtCore.SIGNAL("clicked()"), self.GPS)
        self.stopGPS = False

        #Maintenance Tab  
        ## New
        self.ui.caredateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        QtCore.QObject.connect(self.ui.commentcheckBox, QtCore.SIGNAL("toggled(bool)"), (lambda show=True : self.ui.careComments.setHidden(not show)))
        QtCore.QObject.connect(self.ui.logCare, QtCore.SIGNAL("clicked()"), (lambda reset=False : self.logCare(reset)))
        QtCore.QObject.connect(self.ui.resetCare, QtCore.SIGNAL("clicked()"), (lambda reset=True : self.logCare(reset)))
        
        ## Last
        self.logCare_last()
        self.ui.deleteLast.clicked.connect((lambda : pi2log.pi2log().delLast()))
        self.ui.deleteLast.clicked.connect((lambda : self.logCare_last()))
        QtCore.QObject.connect(self.ui.searchLast, QtCore.SIGNAL("clicked()"), (lambda : searchDialog().doSearch(self.ui.careTask.currentText())))
        
        #Settings Tab
        self.settings_load()
        ## OBDII
        self.ui.spinBox_ATSP.valueChanged.connect((lambda : self.settings_OBD('atsp')))

        self.ui.btRadio.clicked.connect((lambda : self.settings_OBD('bt')))
        self.ui.usbRadio.clicked.connect((lambda : self.settings_OBD('usb')))
        self.ui.devRadio.clicked.connect((lambda : self.settings_OBD('dev')))

        self.ui.units_metric_radio.clicked.connect((lambda : self.settings_OBD('metric')))
        self.ui.units_US_radio.clicked.connect((lambda : self.settings_OBD('US'))) 

        QtCore.QObject.connect(self.ui.obdClear, QtCore.SIGNAL("clicked()"), (lambda : pi2OBD.pi2diag().clearCodes())) 

        ## GPS  
        self.ui.GPS_delLog.clicked.connect((lambda : self.settings_GPS('del')))

        ## Maintenance
        self.ui.care_delLog.clicked.connect((lambda : self.settings_care('del')))

        ## Save
        self.ui.saveButton.clicked.connect((lambda : config.config().newSave(self.default)))
        #self.ui.saveButton.clicked.connect((lambda : config.config().loadDefault()))
        #self.ui.saveButton.clicked.connect((lambda : self.settings_load()))

#################################################################################################################
    def ODBII(self):
        """Starts to read the ODB data [speed, rpm, intake, coolant, load, runtime]"""
        self.stopOBD = not self.stopOBD
        OBDvalues = [0,0,0,0,0,0]
        while not self.stopOBD:
            self.ui.obdButton.setText("Stop")
            OBDvalues = pi2OBD.pi2OBD().OBDread(OBDvalues) 
            self.OBDsignal.emit(OBDvalues)
            
        self.ui.obdButton.setText("Start")

        return

    def updateGUI(self, OBDvalues):
        """Update LCD values in QT: receive [speed, rpm, intake, coolant, load]"""
        time_start = time.time()
        time_end = (time_start + self.default['uiRefresh'])
        
        while time_end > time.time():
            PyQt4.QtCore.QCoreApplication.processEvents()

        self.ui.speed_pBar.setValue(OBDvalues[0])
        self.ui.rpm_pBar.setValue(OBDvalues[1])
        self.ui.intake_pBar.setValue(OBDvalues[2])
        self.ui.cool_pBar.setValue(OBDvalues[3])
        self.ui.load_pBar.setValue(OBDvalues[4])

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
        """Calls function read last line -> updates GUI: [date, task, odo, comments]"""
        careValues = pi2log.pi2log().readLast()
        self.ui.date_output.setText(careValues[0])
        self.ui.task_output.setText(careValues[1]) 
        self.ui.odo_output.setText(careValues[2]) 
        self.ui.comment_output.setText(careValues[3])  

        return

    def careCheck(self):    #[WIP]
        """Reads last odo reading and informs user of suggested Maintenance tasks: [date, task, odo, comments]"""
        careValues = pi2log.pi2log().readLast()
        #Still deciding how id like to view care tasks
        if careValues == 'NA':
            self.ui.careStatus.setText("BAD!!!")
            self.careValues.append("No init Value")
            errorDialog.careErrors.append(careValues)

        return

####################################################################################################
    def settings_load(self):
        """Load last saved settings"""
        self.ui.spinBox_ATSP.setValue(self.default['ATSP'])

        if self.default['serialLabel'] == 'bt':
            self.ui.btRadio.setChecked(True)
            try:
                os.system("blueman-manager")
            except:
                print "Please install 'blueman' package"
        elif self.default['serialLabel'] == 'usb':
            self.ui.usbRadio.setChecked(True)
        else:
            self.ui.devRadio.setChecked(True)

        if self.default['units'] == 'metric':
            self.ui.units_metric_radio.setChecked(True)
        else:
            self.ui.units_US_radio.setChecked(True)

        return

    def settings_OBD(self, label):
        """Function of the settings tab"""
        if label == 'bt':
            try:
                self.default['serialLabel'] = label
                self.default['serialDevice'] = config.config().serialDevice[label]
                os.system("blueman-manager")
            except:
                print "Please install 'blueman' package"
        elif label == 'usb':
            self.default['serialLabel'] = label
            self.default['serialDevice'] = config.config().serialDevice[label]
        elif label == 'dev':
            self.default['serialLabel'] = label
            self.default['serialDevice'] = config.config().serialDevice[label]
        elif label == 'metric':
            self.default['units'] = 'metric'
            print 'made it'
        elif label == 'US':
            self.default['units'] = 'US'            
        else: #ATSP signal return int -> else
            self.default['ATSP'] = self.ui.spinBox_ATSP.value()

        return

    def settings_GPS(self, label):
        """Function of the settings tab"""
        print label    
        if label == 'del':
            try:
                os.remove('../logs/GPSLog.txt')
            except:
                print "No file"
        else:
            pass

        return 

    def settings_care(self, label):
        """Function of the settings tab"""       
        if label == 'del':   
            try:
                os.remove("../logs/MaintainanceLog.xls")
            except:
                print "No file"
        else:
            pass

        return

class searchDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = searchDialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
    
    def doSearch(self, task):
        """Search through logs for data"""
        taskList = pi2log.pi2log().search(task)

        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(taskList))
        self.ui.tableWidget.setHorizontalHeaderLabels(QtCore.QString('Date;Task;Odometer;Comments').split(';'))
        
        for taskIndex in range(len(taskList)):
            dataList = taskList[taskIndex]
            for dataIndex in range(len(dataList)):
                self.ui.tableWidget.setItem(taskIndex, dataIndex, QtGui.QTableWidgetItem(dataList[dataIndex]))
        
        return self.exec_()     
        
class errorDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = errorDialog_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.careErrors = []
        #self.ui.clicked.connect

    def display(self):
        """[date, task, odo, comments, error]"""
        print self.careErrors


        return self.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pi2go()
    myapp.show()
    sys.exit(app.exec_())
