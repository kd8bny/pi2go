# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'libs/main.ui'
#
# Created: Sat Jun 21 17:49:26 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

#Edited By: #Daryl W. Bennett --kd8bny@gmail.com 
#QWT5 support added using makeQWT V1 R1 

from PyQt4 import QtCore, QtGui
from PyQt4.Qwt5 import * 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(656, 524)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(638, 478))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.welcomeTab = QtGui.QWidget()
        self.welcomeTab.setObjectName(_fromUtf8("welcomeTab"))
        self.welcome = QtGui.QGraphicsView(self.welcomeTab)
        self.welcome.setGeometry(QtCore.QRect(30, 40, 261, 251))
        self.welcome.setFrameShape(QtGui.QFrame.WinPanel)
        self.welcome.setFrameShadow(QtGui.QFrame.Sunken)
        self.welcome.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.welcome.setOptimizationFlags(QtGui.QGraphicsView.DontAdjustForAntialiasing)
        self.welcome.setObjectName(_fromUtf8("welcome"))
        self.label = QtGui.QLabel(self.welcomeTab)
        self.label.setGeometry(QtCore.QRect(410, 280, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.AnalogClock = QwtAnalogClock(self.welcomeTab)
        self.AnalogClock.setGeometry(QtCore.QRect(350, 50, 206, 206))
        self.AnalogClock.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.AnalogClock.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.AnalogClock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnalogClock.setLineWidth(4)
        self.AnalogClock.setFrameShadow(QwtDial.Plain)
        self.AnalogClock.setMode(QwtDial.RotateNeedle)
        self.AnalogClock.setObjectName(_fromUtf8("AnalogClock"))
        self.tabWidget.addTab(self.welcomeTab, _fromUtf8(""))
        self.obdTab = QtGui.QWidget()
        self.obdTab.setObjectName(_fromUtf8("obdTab"))
        self.layoutWidget = QtGui.QWidget(self.obdTab)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 13, 181, 201))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdNumber_speed = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber_speed.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_speed.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_speed.setObjectName(_fromUtf8("lcdNumber_speed"))
        self.gridLayout.addWidget(self.lcdNumber_speed, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.lcdNumber_rpm = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber_rpm.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_rpm.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_rpm.setObjectName(_fromUtf8("lcdNumber_rpm"))
        self.gridLayout.addWidget(self.lcdNumber_rpm, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
        self.lcdNumber_inTemp = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber_inTemp.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_inTemp.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_inTemp.setObjectName(_fromUtf8("lcdNumber_inTemp"))
        self.gridLayout.addWidget(self.lcdNumber_inTemp, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 2)
        self.lcdNumber_coolTemp = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber_coolTemp.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_coolTemp.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_coolTemp.setObjectName(_fromUtf8("lcdNumber_coolTemp"))
        self.gridLayout.addWidget(self.lcdNumber_coolTemp, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 2)
        self.lcdNumber_load = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber_load.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_load.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_load.setObjectName(_fromUtf8("lcdNumber_load"))
        self.gridLayout.addWidget(self.lcdNumber_load, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 2)
        self.obdButton = QtGui.QPushButton(self.layoutWidget)
        self.obdButton.setCheckable(False)
        self.obdButton.setAutoRepeat(False)
        self.obdButton.setAutoDefault(False)
        self.obdButton.setDefault(False)
        self.obdButton.setFlat(False)
        self.obdButton.setObjectName(_fromUtf8("obdButton"))
        self.gridLayout.addWidget(self.obdButton, 5, 0, 1, 3)
        self.OBDplot = QwtPlot(self.obdTab)
        self.OBDplot.setGeometry(QtCore.QRect(210, 30, 400, 200))
        self.OBDplot.setObjectName(_fromUtf8("OBDplot"))
        self.tabWidget.addTab(self.obdTab, _fromUtf8(""))
        self.GPStab = QtGui.QWidget()
        self.GPStab.setObjectName(_fromUtf8("GPStab"))
        self.label_12 = QtGui.QLabel(self.GPStab)
        self.label_12.setGeometry(QtCore.QRect(340, 70, 66, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.GPStab)
        self.label_13.setGeometry(QtCore.QRect(340, 100, 71, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.GPSbutton = QtGui.QPushButton(self.GPStab)
        self.GPSbutton.setGeometry(QtCore.QRect(330, 280, 98, 27))
        self.GPSbutton.setObjectName(_fromUtf8("GPSbutton"))
        self.Compass = QwtCompass(self.GPStab)
        self.Compass.setGeometry(QtCore.QRect(30, 80, 200, 200))
        self.Compass.setLineWidth(4)
        self.Compass.setObjectName(_fromUtf8("Compass"))
        self.toolButton = QtGui.QToolButton(self.GPStab)
        self.toolButton.setGeometry(QtCore.QRect(320, 370, 101, 21))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.tabWidget.addTab(self.GPStab, _fromUtf8(""))
        self.caretab = QtGui.QWidget()
        self.caretab.setObjectName(_fromUtf8("caretab"))
        self.layoutWidget1 = QtGui.QWidget(self.caretab)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 631, 431))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.addnew_groupBox = QtGui.QGroupBox(self.layoutWidget1)
        self.addnew_groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addnew_groupBox.sizePolicy().hasHeightForWidth())
        self.addnew_groupBox.setSizePolicy(sizePolicy)
        self.addnew_groupBox.setAutoFillBackground(False)
        self.addnew_groupBox.setObjectName(_fromUtf8("addnew_groupBox"))
        self.commentcheckBox = QtGui.QCheckBox(self.addnew_groupBox)
        self.commentcheckBox.setGeometry(QtCore.QRect(17, 123, 140, 21))
        self.commentcheckBox.setChecked(True)
        self.commentcheckBox.setObjectName(_fromUtf8("commentcheckBox"))
        self.careComments = QtGui.QPlainTextEdit(self.addnew_groupBox)
        self.careComments.setEnabled(True)
        self.careComments.setGeometry(QtCore.QRect(17, 150, 251, 131))
        self.careComments.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.careComments.setAcceptDrops(False)
        self.careComments.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.careComments.setTabChangesFocus(True)
        self.careComments.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.careComments.setObjectName(_fromUtf8("careComments"))
        self.layoutWidget2 = QtGui.QWidget(self.addnew_groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 320, 191, 31))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.logCare = QtGui.QPushButton(self.layoutWidget2)
        self.logCare.setObjectName(_fromUtf8("logCare"))
        self.horizontalLayout_2.addWidget(self.logCare)
        self.resetCare = QtGui.QPushButton(self.layoutWidget2)
        self.resetCare.setObjectName(_fromUtf8("resetCare"))
        self.horizontalLayout_2.addWidget(self.resetCare)
        self.layoutWidget3 = QtGui.QWidget(self.addnew_groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 205, 92))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.caredateEdit = QtGui.QDateEdit(self.layoutWidget3)
        self.caredateEdit.setWrapping(False)
        self.caredateEdit.setMinimumDate(QtCore.QDate(2014, 1, 1))
        self.caredateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.caredateEdit.setCalendarPopup(True)
        self.caredateEdit.setObjectName(_fromUtf8("caredateEdit"))
        self.gridLayout_2.addWidget(self.caredateEdit, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.careTask = QtGui.QComboBox(self.layoutWidget3)
        self.careTask.setObjectName(_fromUtf8("careTask"))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.careTask.setItemText(7, _fromUtf8(""))
        self.careTask.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.careTask, 1, 0, 1, 1)
        self.careOdo = QtGui.QLineEdit(self.layoutWidget3)
        self.careOdo.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.careOdo.setText(_fromUtf8(""))
        self.careOdo.setMaxLength(8)
        self.careOdo.setObjectName(_fromUtf8("careOdo"))
        self.gridLayout_2.addWidget(self.careOdo, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.addnew_groupBox)
        self.line_2 = QtGui.QFrame(self.layoutWidget1)
        self.line_2.setWindowModality(QtCore.Qt.NonModal)
        self.line_2.setFrameShadow(QtGui.QFrame.Raised)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_5.addWidget(self.line_2)
        self.last_groupBox = QtGui.QGroupBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_groupBox.sizePolicy().hasHeightForWidth())
        self.last_groupBox.setSizePolicy(sizePolicy)
        self.last_groupBox.setAutoFillBackground(False)
        self.last_groupBox.setObjectName(_fromUtf8("last_groupBox"))
        self.layoutWidget4 = QtGui.QWidget(self.last_groupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 30, 271, 241))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_18 = QtGui.QLabel(self.layoutWidget4)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)
        self.date_output = QtGui.QLineEdit(self.layoutWidget4)
        self.date_output.setReadOnly(True)
        self.date_output.setObjectName(_fromUtf8("date_output"))
        self.gridLayout_3.addWidget(self.date_output, 0, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget4)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.task_output = QtGui.QLineEdit(self.layoutWidget4)
        self.task_output.setReadOnly(True)
        self.task_output.setObjectName(_fromUtf8("task_output"))
        self.gridLayout_3.addWidget(self.task_output, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        self.odo_output = QtGui.QLineEdit(self.layoutWidget4)
        self.odo_output.setReadOnly(True)
        self.odo_output.setObjectName(_fromUtf8("odo_output"))
        self.gridLayout_3.addWidget(self.odo_output, 2, 2, 1, 1)
        self.comment_output = QtGui.QTextEdit(self.layoutWidget4)
        self.comment_output.setObjectName(_fromUtf8("comment_output"))
        self.gridLayout_3.addWidget(self.comment_output, 3, 2, 1, 1)
        self.line = QtGui.QFrame(self.last_groupBox)
        self.line.setGeometry(QtCore.QRect(-17, 0, 20, 431))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.careTask_Search = QtGui.QComboBox(self.last_groupBox)
        self.careTask_Search.setGeometry(QtCore.QRect(70, 390, 129, 26))
        self.careTask_Search.setObjectName(_fromUtf8("careTask_Search"))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.careTask_Search.setItemText(7, _fromUtf8(""))
        self.careTask_Search.addItem(_fromUtf8(""))
        self.deleteLast = QtGui.QPushButton(self.last_groupBox)
        self.deleteLast.setGeometry(QtCore.QRect(190, 280, 85, 27))
        self.deleteLast.setObjectName(_fromUtf8("deleteLast"))
        self.searchLast = QtGui.QPushButton(self.last_groupBox)
        self.searchLast.setGeometry(QtCore.QRect(210, 390, 85, 27))
        self.searchLast.setObjectName(_fromUtf8("searchLast"))
        self.horizontalLayout_5.addWidget(self.last_groupBox)
        self.tabWidget.addTab(self.caretab, _fromUtf8(""))
        self.settingTab = QtGui.QWidget()
        self.settingTab.setObjectName(_fromUtf8("settingTab"))
        self.settingToolBox = QtGui.QToolBox(self.settingTab)
        self.settingToolBox.setGeometry(QtCore.QRect(10, 10, 271, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingToolBox.sizePolicy().hasHeightForWidth())
        self.settingToolBox.setSizePolicy(sizePolicy)
        self.settingToolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.settingToolBox.setObjectName(_fromUtf8("settingToolBox"))
        self.OBDpage = QtGui.QWidget()
        self.OBDpage.setGeometry(QtCore.QRect(0, 0, 269, 299))
        self.OBDpage.setObjectName(_fromUtf8("OBDpage"))
        self.layoutWidget5 = QtGui.QWidget(self.OBDpage)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 0, 139, 28))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.spinBox_ATSP = QtGui.QSpinBox(self.layoutWidget5)
        self.spinBox_ATSP.setToolTip(_fromUtf8(""))
        self.spinBox_ATSP.setWrapping(True)
        self.spinBox_ATSP.setReadOnly(False)
        self.spinBox_ATSP.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_ATSP.setMinimum(1)
        self.spinBox_ATSP.setMaximum(5)
        self.spinBox_ATSP.setProperty("value", 1)
        self.spinBox_ATSP.setObjectName(_fromUtf8("spinBox_ATSP"))
        self.horizontalLayout_3.addWidget(self.spinBox_ATSP)
        self.layoutWidget6 = QtGui.QWidget(self.OBDpage)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 60, 175, 23))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.usbRadio = QtGui.QRadioButton(self.layoutWidget6)
        self.usbRadio.setObjectName(_fromUtf8("usbRadio"))
        self.horizontalLayout.addWidget(self.usbRadio)
        self.btRadio = QtGui.QRadioButton(self.layoutWidget6)
        self.btRadio.setChecked(False)
        self.btRadio.setObjectName(_fromUtf8("btRadio"))
        self.horizontalLayout.addWidget(self.btRadio)
        self.devRadio = QtGui.QRadioButton(self.layoutWidget6)
        self.devRadio.setEnabled(True)
        self.devRadio.setChecked(True)
        self.devRadio.setObjectName(_fromUtf8("devRadio"))
        self.horizontalLayout.addWidget(self.devRadio)
        self.label_11 = QtGui.QLabel(self.OBDpage)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 63, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_14 = QtGui.QLabel(self.OBDpage)
        self.label_14.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.layoutWidget7 = QtGui.QWidget(self.OBDpage)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 120, 129, 23))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.units_metric_radio = QtGui.QRadioButton(self.layoutWidget7)
        self.units_metric_radio.setObjectName(_fromUtf8("units_metric_radio"))
        self.horizontalLayout_4.addWidget(self.units_metric_radio)
        self.units_US_radio = QtGui.QRadioButton(self.layoutWidget7)
        self.units_US_radio.setChecked(True)
        self.units_US_radio.setObjectName(_fromUtf8("units_US_radio"))
        self.horizontalLayout_4.addWidget(self.units_US_radio)
        self.obdClear = QtGui.QPushButton(self.OBDpage)
        self.obdClear.setGeometry(QtCore.QRect(10, 160, 131, 27))
        self.obdClear.setObjectName(_fromUtf8("obdClear"))
        self.settingToolBox.addItem(self.OBDpage, _fromUtf8(""))
        self.GPSpage = QtGui.QWidget()
        self.GPSpage.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.GPSpage.setObjectName(_fromUtf8("GPSpage"))
        self.GPS_delLog = QtGui.QPushButton(self.GPSpage)
        self.GPS_delLog.setGeometry(QtCore.QRect(10, 10, 93, 27))
        self.GPS_delLog.setObjectName(_fromUtf8("GPS_delLog"))
        self.settingToolBox.addItem(self.GPSpage, _fromUtf8(""))
        self.carePage = QtGui.QWidget()
        self.carePage.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.carePage.setObjectName(_fromUtf8("carePage"))
        self.care_delLog = QtGui.QPushButton(self.carePage)
        self.care_delLog.setGeometry(QtCore.QRect(10, 10, 93, 27))
        self.care_delLog.setObjectName(_fromUtf8("care_delLog"))
        self.settingToolBox.addItem(self.carePage, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.saveButton = QtGui.QPushButton(self.page_3)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(50, 240, 93, 27))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.settingToolBox.addItem(self.page_3, _fromUtf8(""))
        self.layoutWidget8 = QtGui.QWidget(self.settingTab)
        self.layoutWidget8.setGeometry(QtCore.QRect(310, 20, 282, 141))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_19 = QtGui.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setWordWrap(False)
        self.label_19.setOpenExternalLinks(False)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setScaledContents(False)
        self.label_20.setWordWrap(True)
        self.label_20.setOpenExternalLinks(False)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setScaledContents(False)
        self.label_21.setWordWrap(True)
        self.label_21.setOpenExternalLinks(False)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.layoutWidget8)
        self.label_22.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_22.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout.addWidget(self.label_22)
        self.tabWidget.addTab(self.settingTab, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 4)
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_4.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_4.addWidget(self.label_24, 1, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_4.addWidget(self.label_25, 1, 2, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(20, 20))
        self.graphicsView.setMaximumSize(QtCore.QSize(20, 20))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_7.addWidget(self.graphicsView)
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.status.setTextFormat(QtCore.Qt.AutoText)
        self.status.setObjectName(_fromUtf8("status"))
        self.horizontalLayout_7.addWidget(self.status)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.settingToolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pi2go V1 R4", None))
        self.label.setText(_translate("MainWindow", "pi2go V1 R4A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), _translate("MainWindow", "Welcome", None))
        self.label_3.setText(_translate("MainWindow", "Mph", None))
        self.label_2.setText(_translate("MainWindow", "RPM", None))
        self.label_4.setText(_translate("MainWindow", "deg (Intake)", None))
        self.label_5.setText(_translate("MainWindow", "deg (Coolant)", None))
        self.label_6.setText(_translate("MainWindow", "Load", None))
        self.obdButton.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.obdTab), _translate("MainWindow", "OBDII", None))
        self.label_12.setText(_translate("MainWindow", "Latitude", None))
        self.label_13.setText(_translate("MainWindow", "Longitude", None))
        self.GPSbutton.setText(_translate("MainWindow", "Start", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GPStab), _translate("MainWindow", "GPS", None))
        self.addnew_groupBox.setTitle(_translate("MainWindow", "Add New", None))
        self.commentcheckBox.setText(_translate("MainWindow", "Other Comments", None))
        self.logCare.setText(_translate("MainWindow", "Log It!", None))
        self.resetCare.setText(_translate("MainWindow", "Reset Fields", None))
        self.label_8.setText(_translate("MainWindow", "Date", None))
        self.careTask.setItemText(0, _translate("MainWindow", "Air Filter", None))
        self.careTask.setItemText(1, _translate("MainWindow", "Brakes", None))
        self.careTask.setItemText(2, _translate("MainWindow", "Fuel Filter", None))
        self.careTask.setItemText(3, _translate("MainWindow", "New Tires", None))
        self.careTask.setItemText(4, _translate("MainWindow", "Oil Change", None))
        self.careTask.setItemText(5, _translate("MainWindow", "Tire Rotation", None))
        self.careTask.setItemText(6, _translate("MainWindow", "Plugs and Wires", None))
        self.careTask.setItemText(8, _translate("MainWindow", "Miscellaneous", None))
        self.label_10.setText(_translate("MainWindow", "Odometer", None))
        self.label_9.setText(_translate("MainWindow", "Task", None))
        self.last_groupBox.setTitle(_translate("MainWindow", "Last Entry", None))
        self.label_18.setText(_translate("MainWindow", "Comments", None))
        self.label_16.setText(_translate("MainWindow", "Task", None))
        self.label_15.setText(_translate("MainWindow", "Date", None))
        self.label_17.setText(_translate("MainWindow", "Odometer", None))
        self.careTask_Search.setItemText(0, _translate("MainWindow", "Air Filter", None))
        self.careTask_Search.setItemText(1, _translate("MainWindow", "Brakes", None))
        self.careTask_Search.setItemText(2, _translate("MainWindow", "Fuel Filter", None))
        self.careTask_Search.setItemText(3, _translate("MainWindow", "New Tires", None))
        self.careTask_Search.setItemText(4, _translate("MainWindow", "Oil Change", None))
        self.careTask_Search.setItemText(5, _translate("MainWindow", "Tire Rotation", None))
        self.careTask_Search.setItemText(6, _translate("MainWindow", "Plugs and Wires", None))
        self.careTask_Search.setItemText(8, _translate("MainWindow", "Miscellaneous", None))
        self.deleteLast.setText(_translate("MainWindow", "Delete", None))
        self.searchLast.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.caretab), _translate("MainWindow", "Maintenance", None))
        self.label_7.setText(_translate("MainWindow", "ATSP Mode", None))
        self.usbRadio.setText(_translate("MainWindow", "USB", None))
        self.btRadio.setText(_translate("MainWindow", "BT", None))
        self.devRadio.setText(_translate("MainWindow", "Dev", None))
        self.label_11.setText(_translate("MainWindow", "Units", None))
        self.label_14.setText(_translate("MainWindow", "Connection Type", None))
        self.units_metric_radio.setText(_translate("MainWindow", "Metric", None))
        self.units_US_radio.setText(_translate("MainWindow", "US", None))
        self.obdClear.setText(_translate("MainWindow", "Clear Error Codes", None))
        self.settingToolBox.setItemText(self.settingToolBox.indexOf(self.OBDpage), _translate("MainWindow", "OBDII", None))
        self.GPS_delLog.setText(_translate("MainWindow", "Delete Log", None))
        self.settingToolBox.setItemText(self.settingToolBox.indexOf(self.GPSpage), _translate("MainWindow", "GPS", None))
        self.care_delLog.setText(_translate("MainWindow", "Delete Log", None))
        self.settingToolBox.setItemText(self.settingToolBox.indexOf(self.carePage), _translate("MainWindow", "Maintenance", None))
        self.saveButton.setText(_translate("MainWindow", "save", None))
        self.settingToolBox.setItemText(self.settingToolBox.indexOf(self.page_3), _translate("MainWindow", "Save Changes", None))
        self.label_19.setText(_translate("MainWindow", "pi2go", None))
        self.label_20.setText(_translate("MainWindow", "Daryl Bennett", None))
        self.label_21.setText(_translate("MainWindow", "kd8bny@gmail.com", None))
        self.label_22.setText(_translate("MainWindow", "http://www.kd8bny.blogpot.com", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings", None))
        self.label_23.setText(_translate("MainWindow", "Direction", None))
        self.label_24.setText(_translate("MainWindow", "Lat", None))
        self.label_25.setText(_translate("MainWindow", "Long", None))
        self.status.setText(_translate("MainWindow", "Good", None))

#Removedrt QwtPlot

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

