# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(310, 50, 171, 111))
        self.btn_add.setCheckable(False)
        self.btn_add.setAutoRepeatInterval(100)
        self.btn_add.setObjectName("btn_add")
        self.btn_castings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_castings.setGeometry(QtCore.QRect(310, 220, 171, 111))
        self.btn_castings.setObjectName("btn_castings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "Добавить кастинг"))
        self.btn_castings.setText(_translate("MainWindow", "Мои кастинги"))
