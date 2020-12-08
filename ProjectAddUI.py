# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 448)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_name = QtWidgets.QLineEdit(Form)
        self.file_name.setGeometry(QtCore.QRect(60, 20, 111, 31))
        self.file_name.setObjectName("file_name")
        self.file_open = QtWidgets.QPushButton(Form)
        self.file_open.setGeometry(QtCore.QRect(60, 70, 111, 71))
        self.file_open.setObjectName("file_open")
        self.make_casting = QtWidgets.QPushButton(Form)
        self.make_casting.setGeometry(QtCore.QRect(60, 160, 111, 71))
        self.make_casting.setObjectName("make_casting")
        self.casting_text = QtWidgets.QTextEdit(Form)
        self.casting_text.setGeometry(QtCore.QRect(220, 10, 391, 411))
        self.casting_text.setObjectName("casting_text")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(690, 370, 81, 51))
        self.btn_exit.setObjectName("btn_exit")
        self.nameCast = QtWidgets.QTextEdit(Form)
        self.nameCast.setGeometry(QtCore.QRect(640, 50, 121, 41))
        self.nameCast.setObjectName("nameCast")
        self.name_c = QtWidgets.QLabel(Form)
        self.name_c.setGeometry(QtCore.QRect(630, 20, 151, 21))
        self.name_c.setObjectName("name_c")
        self.btn_instruct = QtWidgets.QPushButton(Form)
        self.btn_instruct.setGeometry(QtCore.QRect(60, 360, 111, 51))
        self.btn_instruct.setObjectName("btn_instruct")
        self.add_one = QtWidgets.QPushButton(Form)
        self.add_one.setGeometry(QtCore.QRect(60, 250, 111, 51))
        self.add_one.setObjectName("add_one")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AddCasting"))
        self.file_open.setText(_translate("Form", "Открыть файл"))
        self.make_casting.setText(_translate("Form", "Создать кастинг"))
        self.btn_exit.setText(_translate("Form", "Назад"))
        self.name_c.setText(_translate("Form", "Введите название кастинга"))
        self.btn_instruct.setText(_translate("Form", "Справка"))
        self.add_one.setText(_translate("Form", "Добавить человека"))
