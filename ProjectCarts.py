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


class MyCartsWindows(QWidget):
    def __init__(self, name_cast):
        super().__init__()
        uic.loadUi('ProjectCarts.ui', self)
        self.name_cast = name_cast
        self.con = sqlite3.connect("projectCastSQ.sqlite")
        self.btn_choise.clicked.connect(self.choise)
        self.main_p.clicked.connect(self.main_person)
        self.all_p.clicked.connect(self.all_person)
        self.btn_save.clicked.connect(self.save)
        self.btn_exit.clicked.connect(self.exit)
        self.btn_del.clicked.connect(self.dellit)
        self.btn_to_main.clicked.connect(self.add_to_main)
        self.check_team = ''

    def all_person(self): #выбор всех людей из кастинга
        self.check_team = 'all'
        print(self.name_cast)
        self.combo_person.clear()
        cur = self.con.cursor()
        result = cur.execute("""SELECT name FROM name_person WHERE name_casting='{}'""".format
                             (self.name_cast)).fetchall()#выбор всех людей из кастинга
        print(result)
        res = []
        for i in range(len(result)):
            res.append(result[i][0])
        print(res) #добавление имен в массив
        self.combo_person.addItems(res)#добавление имен в combobox

    def main_person(self):# выбор основного состава
        self.check_team = 'main'
        self.combo_person.clear()
        cur = self.con.cursor()
        result = cur.execute("""SELECT name FROM name_person WHERE id IN(
                                SELECT id_person FROM main_team WHERE name_casting='{}')""".format(
                                self.name_cast)).fetchall()# выбор основного состава
        print(result)
        res = []
        for i in range(len(result)):
            res.append(result[i][0])
        print(res)#добавление основного состава в массив
        self.combo_person.addItems(res)#добавление основного состава в combobox

    def choise(self):#открыть информацию о человеке
        cur = self.con.cursor()
        name = self.combo_person.currentText()
        result= cur.execute("SELECT * FROM name_person WHERE name='{}'".format(name)).fetchall()#вытаскиваем информацию
        res = [[]]
        for i in range(len(result[0])):
            if i != 1:
                res[0].append(result[0][i])
        self.num_text.setText(str(res[0][0]))
        self.name_text.setText(res[0][1])
        self.age_text.setText(str(res[0][2]))
        self.city_text.setText(res[0][3])
        self.network_text.setText(res[0][4])
        self.info_text.setText(res[0][5])
        #вставили все в текстовые поля

    def save(self):#сохранить изменения
        ind_num = self.num_text.toPlainText()#вытаскиваем из полей инфорацию
        ind_name = self.name_text.toPlainText()
        ind_age = int(self.age_text.toPlainText())
        ind_city = self.city_text.toPlainText()
        ind_network = self.network_text.toPlainText()
        ind_info = self.info_text.toPlainText()
        res = []
        res.append(ind_num)
        res.append(ind_name)
        res.append(ind_age)
        res.append(ind_city)
        res.append(ind_network)
        res.append(ind_info)
        print(res)
        cur = self.con.cursor()
        que = "UPDATE name_person SET"#составляем запрос
        que += "(name,age,city,networks,info)"
        que += "=('{}',{},'{}','{}','{}')".format(res[1], res[2], res[3], res[4], res[5])
        que += "WHERE id={}".format(str(int(res[0])))
        print(que)
        cur.execute(que)
        self.con.commit()#выполняем запрос
        self.all_person()

    def del_check(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Вы точно хотите удалить этого человека?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def dellit(self):#удаление человека
        if not self.del_check():
            return None
        cur = self.con.cursor()
        name = self.combo_person.currentText()
        que1 = "DELETE from main_team WHERE id_person = (SELECT id FROM name_person WHERE name='{}' ".format(name)
        que1 += "AND name_casting='{}')".format(self.name_cast)#напишем запрос чтобы удалить из main_team
        cur.execute(que1)
        self.con.commit()
        que2 = "DELETE from name_person WHERE name='{}' AND name_casting='{}'".format(name, self.name_cast)
        cur.execute(que2)#напишем запрос чтобы удалить из name_person
        self.con.commit()
        if self.check_team == 'main':
            self.main_person()
        elif self.check_team == 'all':
            self.all_person()

    def add_main_check(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Этот человек уже в основном составе", QMessageBox.Retry, QMessageBox.Retry)

    def add_to_main(self):#добавить человека в основной состав
        name = self.combo_person.currentText()
        cur = self.con.cursor()
        if cur.execute("""SELECT id_person FROM main_team WHERE id_person IN(
                                SELECT id FROM name_person WHERE name='{}' AND name_casting='{}')""".format(
                                name, self.name_cast)).fetchall():# проверяется, есть ли человек в основе
            self.add_main_check()
            return 0
        res = cur.execute("""SELECT id FROM name_person WHERE name='{}' AND name_casting='{}'""".format(
            name, self.name_cast)).fetchall()  # вытаскиваем id человека
        res = res[0][0]
        que = "INSERT INTO main_team"
        que += "(id_person, name_casting)"
        que += " VALUES({}, '{}')".format(res, self.name_cast)# добавляем его в main_team
        print(que)
        cur.execute(que)  # запрос для заполнения main_team

    def exit(self):#закрытие
        self.close()