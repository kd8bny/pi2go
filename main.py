# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Jun  4 13:04:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(564, 376)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 551, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.welcomeTab = QtGui.QWidget()
        self.welcomeTab.setObjectName(_fromUtf8("welcomeTab"))
        self.graphicsView = QtGui.QGraphicsView(self.welcomeTab)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 261, 251))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.welcomeTab)
        self.label.setGeometry(QtCore.QRect(440, 260, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.welcomeTab, _fromUtf8(""))
        self.obdTab = QtGui.QWidget()
        self.obdTab.setObjectName(_fromUtf8("obdTab"))
        self.widget = QtGui.QWidget(self.obdTab)
        self.widget.setGeometry(QtCore.QRect(170, 40, 178, 174))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdNumber_speed = QtGui.QLCDNumber(self.widget)
        self.lcdNumber_speed.setObjectName(_fromUtf8("lcdNumber_speed"))
        self.gridLayout.addWidget(self.lcdNumber_speed, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.lcdNumber_rpm = QtGui.QLCDNumber(self.widget)
        self.lcdNumber_rpm.setObjectName(_fromUtf8("lcdNumber_rpm"))
        self.gridLayout.addWidget(self.lcdNumber_rpm, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
        self.lcdNumber_inTemp = QtGui.QLCDNumber(self.widget)
        self.lcdNumber_inTemp.setObjectName(_fromUtf8("lcdNumber_inTemp"))
        self.gridLayout.addWidget(self.lcdNumber_inTemp, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 2)
        self.lcdNumber_coolTemp = QtGui.QLCDNumber(self.widget)
        self.lcdNumber_coolTemp.setObjectName(_fromUtf8("lcdNumber_coolTemp"))
        self.gridLayout.addWidget(self.lcdNumber_coolTemp, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 2)
        self.lcdNumber_load = QtGui.QLCDNumber(self.widget)
        self.lcdNumber_load.setObjectName(_fromUtf8("lcdNumber_load"))
        self.gridLayout.addWidget(self.lcdNumber_load, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 2)
        self.obdStart = QtGui.QPushButton(self.widget)
        self.obdStart.setObjectName(_fromUtf8("obdStart"))
        self.gridLayout.addWidget(self.obdStart, 5, 0, 1, 2)
        self.obdKill = QtGui.QPushButton(self.widget)
        self.obdKill.setObjectName(_fromUtf8("obdKill"))
        self.gridLayout.addWidget(self.obdKill, 5, 2, 1, 1)
        self.tabWidget.addTab(self.obdTab, _fromUtf8(""))
        self.carTab = QtGui.QWidget()
        self.carTab.setObjectName(_fromUtf8("carTab"))
        self.F_lights = QtGui.QToolButton(self.carTab)
        self.F_lights.setGeometry(QtCore.QRect(10, 30, 111, 71))
        self.F_lights.setObjectName(_fromUtf8("F_lights"))
        self.A_lights = QtGui.QToolButton(self.carTab)
        self.A_lights.setGeometry(QtCore.QRect(10, 110, 111, 71))
        self.A_lights.setObjectName(_fromUtf8("A_lights"))
        self.tabWidget.addTab(self.carTab, _fromUtf8(""))
        self.settingTab = QtGui.QWidget()
        self.settingTab.setObjectName(_fromUtf8("settingTab"))
        self.obdClear = QtGui.QPushButton(self.settingTab)
        self.obdClear.setGeometry(QtCore.QRect(40, 40, 131, 27))
        self.obdClear.setObjectName(_fromUtf8("obdClear"))
        self.tabWidget.addTab(self.settingTab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "pi2go V1 R2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), _translate("MainWindow", "Welcome", None))
        self.label_3.setText(_translate("MainWindow", "Mph", None))
        self.label_2.setText(_translate("MainWindow", "RPM", None))
        self.label_4.setText(_translate("MainWindow", "deg (Intake)", None))
        self.label_5.setText(_translate("MainWindow", "deg (Coolant)", None))
        self.label_6.setText(_translate("MainWindow", "Load", None))
        self.obdStart.setText(_translate("MainWindow", "Start", None))
        self.obdKill.setText(_translate("MainWindow", "Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.obdTab), _translate("MainWindow", "OBDII", None))
        self.F_lights.setText(_translate("MainWindow", "Fog Lights", None))
        self.A_lights.setText(_translate("MainWindow", "Accent Lights", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.carTab), _translate("MainWindow", "Car", None))
        self.obdClear.setText(_translate("MainWindow", "Clear Error Codes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

