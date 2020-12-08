# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectCastings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(795, 448)
        self.my_castings = QtWidgets.QComboBox(form)
        self.my_castings.setGeometry(QtCore.QRect(260, 20, 261, 61))
        self.my_castings.setIconSize(QtCore.QSize(16, 16))
        self.my_castings.setObjectName("my_castings")
        self.btn_open = QtWidgets.QPushButton(form)
        self.btn_open.setGeometry(QtCore.QRect(590, 360, 181, 71))
        self.btn_open.setObjectName("btn_open")
        self.btn_exit = QtWidgets.QPushButton(form)
        self.btn_exit.setGeometry(QtCore.QRect(20, 310, 141, 61))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_del = QtWidgets.QPushButton(form)
        self.btn_del.setGeometry(QtCore.QRect(610, 30, 171, 41))
        self.btn_del.setObjectName("btn_del")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "MyCasting"))
        self.btn_open.setText(_translate("form", "Открыть"))
        self.btn_exit.setText(_translate("form", "Назад"))
        self.btn_del.setText(_translate("form", "Удалить"))
