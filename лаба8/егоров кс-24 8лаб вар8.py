from PyQt5 import QtWidgets, uic
import sys
import string
from PyQt5.QtWidgets import QTreeWidgetItem
data=[]


app = QtWidgets.QApplication([])
win = uic.loadUi("laba8.ui") # расположение вашего файла .ui


win.show()
def onliliters():
 win.spinBox.setMaximum(25) 
 data.clear() 
 for c in string.ascii_uppercase:
     data.append(c)
 win.spinBox.setValue(0)
 win.label.setText(data[0]) 
onliliters()


def onlididgit(): 
 
 win.spinBox.setMaximum(9) 
 data.clear()
 for c in string.digits: 
     data.append(c)
 win.spinBox.setValue(0)
 win.label.setText(data[0])        

def simbols():
 data.clear() 
 win.spinBox.setMaximum(3)   
 for i in range(38,34,-1):
     data.append(chr(i))
 win.spinBox.setValue(0)

 win.label.setText(data[0])


def cg(i):
 win.label.setText(data[i])



             
def pb():
 win.treeWidget.clear ()
 str1=""
 str2=""
 if (win.checkBox.isChecked() ):
     str1="&"
 if (win.checkBox_2.isChecked() ):
     str2="&"
 k=1
 index=win.spinBox.value()
 char=data[index]
 colum=win.tableWidget.columnCount()
 row =win.tableWidget.rowCount()
 for i in range (colum):
     for j in range (row):
         try:
             text=win.tableWidget.item(j,i).text()
             if (len(text)>0):
                 if(text[0].upper()==char): 
                     parent = QTreeWidgetItem(win.treeWidget)
                     parent.setText(0,str(k))
                     parent.setText(1,str1+text+str2)
                     k+=1
         except AttributeError:
             pass
             
         
 



win.radioButton.toggled.connect(onliliters)
win.radioButton_2.toggled.connect(onlididgit)
win.radioButton_3.toggled.connect(simbols)
win.spinBox.valueChanged.connect(cg)
win.pushButton.clicked.connect(pb)
win.pushButton_2.clicked.connect(lambda: win.tableWidget.insertColumn(win.tableWidget.columnCount()) )
win.pushButton_3.clicked.connect(lambda: win.tableWidget.insertRow(win.tableWidget.rowCount()) )
win.pushButton_4.clicked.connect(lambda: win.tableWidget.removeColumn(win.tableWidget.columnCount()-1) )
win.pushButton_5.clicked.connect(lambda: win.tableWidget.removeRow(win.tableWidget.rowCount()-1) )
sys.exit(app.exec())