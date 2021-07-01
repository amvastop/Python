import os
import sys
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

xarr=[]
yarr=[]
garr=[]





def readrez(str1):
 ind= int(str1[1:-4])-1
 with open(str1,'r') as f:
 
 
    for line in f : 
        str1 = list (line[:-1].split(',') )
        garr.append(str1)
 
 
 mem=0
 with open('Calc.ini', 'r+') as f:
     for i in range(ind):
         str1=f.readline()
         mem=int(str1[:-1])+mem+ len(str1)
         f.seek(mem)
     f.readline()   
     yarr.extend(f.readline()[:-1].split(','))
     xarr.extend(f.readline()[:-1].split(','))

 


def readdat(str1):
 with open(str1,'r') as f:
  
    str1  =f.readline()
    str1  =f.readline()
    yarr=list(str1[4:-2].split(',')) 
    
    for line in f : 
        str1 = list (line[:-1].split(',') )
        xarr.append(str1.pop(0))
        garr.append(str1)
 
 
 






def readlog():
 if (not os.path.exists("myProgram.log")):
     QMessageBox.critical(win,'crit',"Program.log file is not created",QMessageBox.Ok )
     sys.exit()
 with open("myProgram.log",'r') as f:
    str1= f.read()
 
 str1= list(str1.split("\n"))
 
 for s in str1:
     if(s.find(".dat") >0 ):
         win.listWidget.addItem(s)
         win.listWidget.addItem(s.replace("dat","rez"))


def clik(): 
 try:
     str1= win.listWidget.currentItem().text()
 except AttributeError:
     QMessageBox.warning(win,'war',"the file list is empty",QMessageBox.Ok )
     return
 if (not os.path.exists(str1)):
     QMessageBox.warning(win,'war',"file does not exist",QMessageBox.Ok )
     return 
 if(str1.find("rez")>0):
     readrez(str1)
 else:
     readdat(str1)


if __name__ == "__main__":

 app = QtWidgets.QApplication([])
 win = uic.loadUi("laba5_3.ui") # расположение вашего файла .ui

 win.show()

 readlog()
 win.pushButton.clicked.connect(clik)
 sys.exit(app.exec())
