import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QCheckBox, QMessageBox
import sqlite3


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls._name_, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class AddWindows(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ProjectAdd.ui', self)
        self.con = sqlite3.connect("projectCastSQ.sqlite")
        self.file_open.clicked.connect(self.open)
        self.make_casting.clicked.connect(self.make)
        self.btn_exit.clicked.connect(self.exit)
        self.btn_instruct.clicked.connect(self.instruct)
        self.add_one.clicked.connect(self.make)

    def open(self):#открыть файл с текстом
        text = ''
        file = self.file_name.text()
        data = open(file, mode="r", encoding='utf8').readlines()
        for i in range(len(data)):
            text += data[i]
        self.casting_text.setText(text)

    def del_check(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Неправильно набран текст", QMessageBox.Retry,
                                     QMessageBox.Retry)

    def make(self):#создать кастинг или добавить человека
        text = self.casting_text.toPlainText()
        if text.count('\n') < 3 or text.count('$') < 2:#проверяем правильность текста
            self.del_check()
            return None
        name_cast = self.nameCast.toPlainText()
        a = []
        allname = text.split('%')#делим на разных людей
        print(allname)
        for i in range(len(allname)):
            d = allname[i].split('$')#делим людей на до соц.сетей/соц.сети/информация
            a.append(d)
        print(a)
        for i in range(len(a)):
            b = a[i][0].split('\n')  # оставляем в "в" все что до соц.сетей
            del a[i][0]
            j = 0
            while b[j] == '':  # убираем лишние переводы строки в начале карточки
                del b[j]
            print(b)
            del b[-1]
            b.extend(a[i])  # добавляем в "в" всю инфу о пользователе
            print(b)
            surname = b[0].split()  # разбираемся с номером,именем,возрастом
            del b[0]
            name = ' '.join(surname[1:3])
            del surname[1:3]
            surname.insert(1, name)
            surname[1] = surname[1][:-1]  # закончили разбираться, сделав из одного элем три нужных
            surname.extend(b)
            b = surname[:]
            if b[4] == 'ОСНОВНОЙ СОСТАВ':
                del b[4]
                cur = self.con.cursor()  # id человека добавляется в другую таблицу БД с основ.состав
                res = cur.execute("""SELECT id FROM name_person""").fetchall()#вытаскиваем последний id
                if res == []:
                    res = 1
                else:
                    res = res[-1]
                    res = res[0]
                    res += 1
                que = "INSERT INTO main_team"
                que += "(id_person, name_casting)"
                que += " VALUES({}, '{}')".format(res, name_cast)
                cur.execute(que)#запрос для заполнения main_team
            a[i] = b  # теперь в a[i] правильный список, подходящий для таблицы БД
            cur = self.con.cursor()
            que = "INSERT INTO name_person"
            que += "(name_casting,name,age,city,networks,info)"
            que += " VALUES('{}','{}',{},'{}','{}','{}')".format(name_cast, b[1], b[2], b[3], b[4], b[5])
            cur.execute(que)#запрос для заполнение name_person
            self.con.commit()
        print(a)

    def instruct(self):
        instruction = QMessageBox.question(self, 'Instruction',
                                     "номер имя фамилия, возраст\n" +
                                     "Город\n" +
                                     "основной состав(не обязательно, можно пропустить)\n" +
                                     "&ссылки&(допустимо много строк; символ '$' обязателен)\n" +
                                     "остальная информация%(ставить символ '%', если не последний человел)",
                                           QMessageBox.Ok, QMessageBox.Ok)

    def exit(self):
        self.close()
