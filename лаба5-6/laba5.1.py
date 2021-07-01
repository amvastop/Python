from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
app = QtWidgets.QApplication([])
win = uic.loadUi("laba5_1.ui") # расположение вашего файла .ui
win.show()



def clik():
   try:
    strArr= int(win.lineEdit.text())
   except ValueError:
      msbox("Value Error")
   except OverflowError:
      msbox("Over flow Error")

def msbox(str1):
 ret = QMessageBox.question(win,'qusetion',str1+ "\n Repeat Entry or Stop?",QMessageBox.Retry|QMessageBox.Cancel,QMessageBox.Cancel)
 if ret == QMessageBox.Retry:
    win.show()
    win.accepted.connect(clik)

win.accepted.connect(clik)
sys.exit(app.exec())