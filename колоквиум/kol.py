from PyQt5 import  QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox, QTreeWidgetItem
import sys
import os
import kol_gui
class mainwindow(QtWidgets.QMainWindow,kol_gui.Ui_MainWindow):
 def __init__(self, parent = None):
     super().__init__(parent)
     self.setupUi(self)
     self.A=[]
     self.B=[]
     self.C=[]
     self.inp="Input.txt"
     self.pushButton_2.clicked.connect( self.vsodmas)

    
 def fread(self): 
     self.A.clear()
     if (os.path.exists(self.inp)):
         with open(self.inp, 'r') as f:
             for line in f:
                  self.A.append(line.replace('\n',"").split(";"))
     for i in range(len(self.A)):
         for j in range(len(self.A[i])):
             self.A[i][j]=int (self.A[i][j])
     
     for i in range(len(self.A)):
         for j in range(len(self.A[i])):
             self.B.append(self.A[i][j])
     
     if (self.radioButton.isChecked()):
         self.B=sorted(self.B,reverse=True)
 
     if (self.radioButton_2.isChecked()):
         self.B=sorted(self.B)
     for i in range(len(self.A)):
         for j in range(len(self.A[i])):
             index=len(self.A[i])*i+j
             self.A[i][j]=self.B[index]
 
 
 
 
 def write(self,a,str1 ):
     if str1=="B":
         self.comboBox.addItem
         with open('Data.txt','a') as f:
             f.write(str1+"\n")
             for i in range( len(a)):
                 self.comboBox.addItem(str(a[i]))
                 f.write ( '{:< 24}'.format((a[i])))
                 if (i<len(a)-1):
                     f.write(",")
                 else:f.write("\n")
     if str1=="A":
         with open('Data.txt','a') as f:
             f.write ( str1+"\n")
             str1=""
             for i in range( len(a)):
                 for j in range( len(a[i])):
                     str1=str1+'{:< 24}'.format((a[i][j]))
                     f.write ( '{:< 24}'.format((a[i][j])))

                     if (j<(len(a[i])-1)):
                         f.write(",")
                         str1=str1+','
                     else:
                         f.write("\n")
                         str1=str1+"\n"
         self.textEdit_3.setText(str1)
     if str1=="C":
         with open('Data.txt','a') as f:
             f.write ( str1+"\n")
             str1=""
             for i in range( len(a)):
                 for j in range(len(a[i])):
                     str1=str1+'{:< 24}'.format(a[i][j])
                     f.write ( '{:< 24}'.format(a[i][j]))
                     if (j<(len(a[i])-1)):
                         f.write(",")
                         str1=str1+','
                     else:
                         f.write("\n")
                         str1=str1+"\n"
         self.textEdit_2.setText(str1)
                 

             



             

        
 def vsodmas(self):
     self.A.clear()
     self.B.clear()
     self.C.clear()
     self.comboBox.clear()
     self.textEdit_3.clear()
     self.textEdit_2.clear()
     self.fread()

     try :
      row =int (self.lineEdit.text())
      colum= int (self.lineEdit_2.text())
     except :
         return
     for i in range(row):
         self.C.append([])
         for j in range(colum):
             index=colum*i+j
             if(index<=(len(self.B)-1)):
                 self.C[i].append(self.B[index])
             else:
                 self.C[i].append(0)
     self. write(self.B,"B")
     self. write(self.A,"A")
     self. write(self.C,"C")

    


app = QtWidgets.QApplication(sys.argv)
window = mainwindow()
window.show()
app.exec_()



     
    