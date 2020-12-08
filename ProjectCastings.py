import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QCheckBox, QMessageBox
from ProjectCarts import MyCartsWindows
import sqlite3


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls._name_, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class MyCastWindows(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ProjectCastings.ui', self)
        self.con = sqlite3.connect("projectCastSQ.sqlite")
        self.combo_cast()
        self.btn_open.clicked.connect(self.open_carts)
        self.btn_exit.clicked.connect(self.exit)
        self.btn_del.clicked.connect(self.dellit)


    def combo_cast(self):#выбор всех кастингов
        self.my_castings.clear()
        cur = self.con.cursor()
        result = cur.execute("""SELECT name_casting FROM name_person""").fetchall()#вытаскиваем все названия кастингов
        print(result)
        result = set(result)
        result = list(result)#удаляем повторяющиеся
        print(result)
        res = []
        for i in range(len(result)):
            res.append(result[i][0])
        print(res)
        self.my_castings.addItems(res)#добовляем в combobox список кастингов

    def open_check(self):#проверка наличия кастинга
        reply = QMessageBox.question(self, 'Message',
                                     "У вас нет кастингов", QMessageBox.Retry, QMessageBox.Retry)

    def open_carts(self):#открываем окно карточек участников
        name = self.my_castings.currentText()
        if name == '':
            self.open_check()
            return 0
        self.ex_carts = MyCartsWindows(self.my_castings.currentText())
        self.ex_carts.show()

    def del_check(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Вы точно хотите удалить этот кастинг?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def dellit(self):#удаляем кастинг
        if not self.del_check():
            return None
        cur = self.con.cursor()
        text = self.my_castings.currentText()
        que1 = "DELETE from main_team WHERE name_casting='{}'".format(text)
        cur.execute(que1)#удаляем из main_team
        self.con.commit()
        que2 = "DELETE from name_person WHERE name_casting='{}'".format(text)
        cur.execute(que2)#удаляем из name_person
        self.con.commit()
        self.my_castings.clear()
        cur = self.con.cursor()
        result = cur.execute("""SELECT name_casting FROM name_person""").fetchall()
        print(result)#обновим список наших кастингов
        result = set(result)
        result = list(result)
        print(result)
        res = []
        for i in range(len(result)):
            res.append(result[i][0])
        print(res)
        self.my_castings.addItems(res)

    def exit(self):
        self.close()