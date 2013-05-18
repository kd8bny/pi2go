# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat May 18 00:08:01 2013
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 541, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.welcomeTab = QtGui.QWidget()
        self.welcomeTab.setObjectName(_fromUtf8("welcomeTab"))
        self.graphicsView = QtGui.QGraphicsView(self.welcomeTab)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.welcomeTab)
        self.label.setGeometry(QtCore.QRect(440, 260, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.welcomeTab, _fromUtf8(""))
        self.musicTab = QtGui.QWidget()
        self.musicTab.setObjectName(_fromUtf8("musicTab"))
        self.tabWidget.addTab(self.musicTab, _fromUtf8(""))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "pi2go V1 R0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.welcomeTab), _translate("MainWindow", "Welcome", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musicTab), _translate("MainWindow", "Music", None))
        self.F_lights.setText(_translate("MainWindow", "Fog Lights", None))
        self.A_lights.setText(_translate("MainWindow", "Accent Lights", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.carTab), _translate("MainWindow", "Car", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

