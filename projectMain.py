import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QCheckBox, QMessageBox
from projectAdd import AddWindows
from ProjectCastings import MyCastWindows


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls._name_, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('projectMain.ui', self)
        self.btn_add.clicked.connect(self.add)
        self.btn_castings.clicked.connect(self.my_castings)

    def add(self):#открываем окно добавления кастинга
        self.ex_add = AddWindows()
        self.ex_add.show()

    def my_castings(self):#открываем окно кастингов
        self.ex_castings = MyCastWindows()
        self.ex_castings.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())