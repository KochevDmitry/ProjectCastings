# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectCarts.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 448)
        self.main_p = QtWidgets.QPushButton(Form)
        self.main_p.setGeometry(QtCore.QRect(20, 10, 131, 51))
        self.main_p.setObjectName("main_p")
        self.combo_person = QtWidgets.QComboBox(Form)
        self.combo_person.setGeometry(QtCore.QRect(590, 20, 191, 51))
        self.combo_person.setObjectName("combo_person")
        self.all_p = QtWidgets.QPushButton(Form)
        self.all_p.setGeometry(QtCore.QRect(20, 70, 131, 51))
        self.all_p.setObjectName("all_p")
        self.info_text = QtWidgets.QTextEdit(Form)
        self.info_text.setGeometry(QtCore.QRect(210, 210, 331, 221))
        self.info_text.setObjectName("info_text")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(20, 370, 141, 51))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_choise = QtWidgets.QPushButton(Form)
        self.btn_choise.setGeometry(QtCore.QRect(620, 80, 131, 61))
        self.btn_choise.setObjectName("btn_choise")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(600, 240, 171, 71))
        self.btn_save.setObjectName("btn_save")
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setGeometry(QtCore.QRect(620, 150, 131, 51))
        self.btn_del.setObjectName("btn_del")
        self.num_text = QtWidgets.QTextEdit(Form)
        self.num_text.setGeometry(QtCore.QRect(210, 20, 111, 31))
        self.num_text.setObjectName("num_text")
        self.name_text = QtWidgets.QTextEdit(Form)
        self.name_text.setGeometry(QtCore.QRect(210, 80, 141, 31))
        self.name_text.setObjectName("name_text")
        self.city_text = QtWidgets.QTextEdit(Form)
        self.city_text.setGeometry(QtCore.QRect(210, 140, 101, 41))
        self.city_text.setObjectName("city_text")
        self.network_text = QtWidgets.QTextEdit(Form)
        self.network_text.setGeometry(QtCore.QRect(330, 140, 211, 41))
        self.network_text.setObjectName("network_text")
        self.label_num = QtWidgets.QLabel(Form)
        self.label_num.setGeometry(QtCore.QRect(210, 0, 47, 13))
        self.label_num.setObjectName("label_num")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(210, 60, 47, 13))
        self.label_name.setObjectName("label_name")
        self.label_city = QtWidgets.QLabel(Form)
        self.label_city.setGeometry(QtCore.QRect(210, 120, 47, 13))
        self.label_city.setObjectName("label_city")
        self.label_network = QtWidgets.QLabel(Form)
        self.label_network.setGeometry(QtCore.QRect(340, 120, 101, 16))
        self.label_network.setObjectName("label_network")
        self.label_info = QtWidgets.QLabel(Form)
        self.label_info.setGeometry(QtCore.QRect(210, 190, 131, 16))
        self.label_info.setObjectName("label_info")
        self.age_text = QtWidgets.QTextEdit(Form)
        self.age_text.setGeometry(QtCore.QRect(380, 80, 51, 31))
        self.age_text.setObjectName("age_text")
        self.label_age = QtWidgets.QLabel(Form)
        self.label_age.setGeometry(QtCore.QRect(380, 60, 47, 13))
        self.label_age.setObjectName("label_age")
        self.btn_to_main = QtWidgets.QPushButton(Form)
        self.btn_to_main.setGeometry(QtCore.QRect(600, 330, 171, 71))
        self.btn_to_main.setObjectName("btn_to_main")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MyCarts"))
        self.main_p.setText(_translate("Form", "Основной состав"))
        self.all_p.setText(_translate("Form", "Общий состав"))
        self.btn_exit.setText(_translate("Form", "Назад"))
        self.btn_choise.setText(_translate("Form", "Выбрать"))
        self.btn_save.setText(_translate("Form", "Сохранить"))
        self.btn_del.setText(_translate("Form", "Удалить"))
        self.label_num.setText(_translate("Form", "Номер"))
        self.label_name.setText(_translate("Form", "Имя"))
        self.label_city.setText(_translate("Form", "Город"))
        self.label_network.setText(_translate("Form", "Социальные сети"))
        self.label_info.setText(_translate("Form", "Остальная информмация"))
        self.label_age.setText(_translate("Form", "Возраст"))
        self.btn_to_main.setText(_translate("Form", "Добавить в основной состав"))
