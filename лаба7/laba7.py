import sys
import os
import shutil
from PyQt5 import  QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox, QTreeWidgetItem
import laba7_2
import laba7_1
from PyQt5.QtGui import QPixmap
import pickle
import _pickle


class secwindow(QtWidgets.QMainWindow,laba7_2.Ui_Form):
 
 def __init__(self,sf,i):
     super().__init__( )
     self.setupUi(self)
     self.mwself=sf
     self.ind=i
     self.scene = QGraphicsScene()
     self.graphicsView.setScene(self.scene)
     self.path=["",""]
     self.boll=[False,False,False,False,False,True]
     if((len(self.mwself.data)-1)>=self.ind):
         self.showitem()
     for i in range(1950,2051):
         self.comboBox.addItem(str(i))
         
     self.lineEdit.textChanged.connect(lambda: self.chekd(0))
     self.lineEdit_2.textChanged.connect(lambda: self.chekd(1))
     self.lineEdit_3.textChanged.connect(lambda: self.chekd(2))
     self.lineEdit_4.textChanged.connect(lambda: self.chekd(3))
     self.lineEdit_5.textChanged.connect(lambda: self.chekd(4))
     self.comboBox.editTextChanged.connect(lambda: self.chekd(5))
     self.pushButton_2.clicked.connect(lambda : self.close())
     self.pushButton_3.clicked.connect(self.cleartable)
     self.pushButton.clicked.connect(self.appl)
     self.pushButton_4.clicked.connect(self.imdw)     

 def showitem(self):
         self.lineEdit.setText(self.mwself.data[self.ind][0])
         self.lineEdit_2.setText(self.mwself.data[self.ind][1])
         self.lineEdit_3.setText(self.mwself.data[self.ind][2])
         self.lineEdit_4.setText(self.mwself.data[self.ind][3])
         self.lineEdit_5.setText(self.mwself.data[self.ind][4])
         self.comboBox.setEditText(self.mwself.data[self.ind][5])
         
         self.path[1]=self.mwself.data[self.ind][6]
         if len(self.path[1])>0 :
             self.showimage(1)
         self.pushButton.setEnabled(True)
         self.boll=[True,True,True,True,True,True]

 def cleartable(self):
     self.lineEdit.clear()
     self.lineEdit_2.clear()
     self.lineEdit_3.clear()
     self.lineEdit_4.clear()
     self.lineEdit_5.clear()
     self.comboBox.clearEditText ()
     if (self.graphicsView.scene().isActive()):
         self.graphicsView.scene().clear()
     if (os.path.exists(self.path[1])):
         os.remove(self.path[1]) 
     self.path[1]="" 
     self.path[0]=""
     self.pushButton.setEnabled(False)

 def showimage(self,ind):
     width= self.graphicsView.width()
     height= self.graphicsView.height()
     if(os.path.exists(self.path[ind])):
         self.scene.addPixmap(QPixmap(self.path[ind]).scaled(width,height))

 def imdw(self):
     fname= QFileDialog.getOpenFileName(self, 'Open file', 
   'c:\\',"Image files (*.jpg *.png)")
     if (len(fname[0])!=0):
         if(os.path.exists(self.path[1])):
             os.remove(self.path[1]) 
         self.path[0] =fname[0]
         ind=self.path[0].rfind("/")
         self.path[1] ="src"+self.path[0][ind:]
         self.showimage(0)
         


         
         
 def chekd(self,ind):
     self.pushButton.setEnabled(False)
     sw={
     0 : not self.lineEdit.text().isdigit(),
     1 : not self.lineEdit_2.text().isdigit(),
     2 : not self.lineEdit_3.text().isdigit(),
     3 : self.lineEdit_4.text().isdigit(),
     4 : self.lineEdit_5.text().isdigit(),
     5 : self.comboBox.currentText().isdigit(),
     }
     j=0
     self.boll[ind]=sw.get(ind)
     for i in range(6):
         if(self.boll[i]):
             j+=1
     if (j== 6):
         self.pushButton.setEnabled(True)
      
 def appl(self):
     if((len(self.mwself.data)-1)<self.ind):
         self.mwself.data.append([])
         self.mwself.data[self.ind].append(self.lineEdit.text())
         self.mwself.data[self.ind].append(self.lineEdit_2.text())
         self.mwself.data[self.ind].append(self.lineEdit_3.text())
         self.mwself.data[self.ind].append(self.lineEdit_4.text())
         self.mwself.data[self.ind].append(self.lineEdit_5.text())
         self.mwself.data[self.ind].append(self.comboBox.currentText())
         if (os.path.exists(self.path[0])):
             shutil.copy(self.path[0],"src")
         else:
             self.path[1]=""
         self.mwself.data[self.ind].append(self.path[1])
         self.mwself.add(self.ind)
     else:
         self.mwself.data[self.ind][0]=(self.lineEdit.text())
         self.mwself.data[self.ind][1]=(self.lineEdit_2.text())
         self.mwself.data[self.ind][2]=(self.lineEdit_3.text())
         self.mwself.data[self.ind][3]=(self.lineEdit_4.text())
         self.mwself.data[self.ind][4]=(self.lineEdit_5.text())
         self.mwself.data[self.ind][5]=(self.comboBox.currentText())
         if (os.path.exists(self.path[0])):
             shutil.copy(self.path[0],"src")
         else:
             self.path[1]=""
         self.mwself.data[self.ind][6]=(self.path[1])
         mainwindow.changeitem(self.mwself,self.ind)

     self.close()
 


class mainwindow(QtWidgets.QMainWindow,laba7_1.Ui_Form):
 
 
 def __init__(self, parent = None):
     super().__init__(parent)
     self.setupUi(self)
     
     if not os.path.exists("src"):
         os.mkdir("src")
     self.data=[]
     self.twoWindow = None
     self.ffail= False
     self.dwfname=["",""]
     self.scene = QGraphicsScene()
     self.graphicsView.setScene(self.scene)
     self.pushButton_3.clicked.connect(self.addelment)
     self.pushButton_4.clicked.connect(self.removeitem)
     self.pushButton_2.clicked.connect(self.save)
     self.pushButton_5.clicked.connect(self.clearform)
     self.pushButton.clicked.connect(self.dwon)
     self.treeWidget.itemClicked.connect(self.showimg)
     self.treeWidget.itemDoubleClicked.connect(self.chang)
 
 def clearform(self):
     self.treeWidget.clear()
     for i in range(len(self.data)):
         if (os.path.exists(self.data[i][6]) and not self.ffail ):
             os.remove(self.data[i][6])
     self.data.clear()

     

     if (self.graphicsView.scene().isActive()):
         self.graphicsView.scene().clear()
   

 def addelment(self,str1):
     i=len(self.data)
     self.twoWindow = secwindow(self,i)
     self.twoWindow.show()
 def add(self,i):
     parent = QTreeWidgetItem(self.treeWidget)
     
     parent.setText(0,str(i+1))
     for j in range(1,7): 
         parent.setText(j,self.data[i][j-1])


 def dwon(self):
     self.dwfname= QFileDialog.getOpenFileName(self, 'Open file', 
   'c:\\',"Image files ( *.dat)") 

     if (len(self.dwfname[0])>0):
         try:
             with open(self.dwfname[0], 'rb') as f:
                 self.clearform()
                 self.data = pickle.load(f)
                 self.ffail=True
                   
                 for i in range(len(self.data)):
                     self.add(i)
         except _pickle.UnpicklingError:
             QMessageBox.critical(self,"erro","фаил невозможно загрузить",QMessageBox.Ok)
                 
                 
 def save(self):
     if (len(self.data)>0 and not self.ffail ):
         fname= QFileDialog.getSaveFileName(self, 'Save file', 'c:\\',"Data files (*.dat )")
         if (len(fname[0])>0 ):
             with open(fname[0], 'wb') as f:
                 pickle.dump(self.data, f)
             self.clearform()

     if (self.ffail and len(self.data)==0 and os.path.exists(self.dwfname[0])):
         os.remove(self.dwfname[0])
         self.ffail=False
     if(self.ffail and os.path.exists(self.dwfname[0])):
         with open(self.dwfname[0], 'wb') as f:
             pickle.dump(self.data, f)
         self.clearform()
         self.ffail=False
         
    
            
     

 def showimg(self,item):
     if (self.graphicsView.scene().isActive()):
         self.graphicsView.scene().clear()
     ind=self.treeWidget.indexFromItem(item).row()
     if (os.path.exists(self.data[ind][6])):
         width= self.graphicsView.width()
         height= self.graphicsView.height()
         
         self.scene.addPixmap(QPixmap(self.data[ind][6]).scaled(width-3,height-3))
         


 def chang(self,item):
     ind=self.treeWidget.indexFromItem(item).row()
     self.twoWindow = secwindow(self,ind)
     self.twoWindow.show()

 def changeitem(self,ind):
     self.treeWidget.takeTopLevelItem(ind)
     parent = QTreeWidgetItem()
     parent.setText(0,str(ind+1))
     for j in range(1,7): 
         parent.setText(j,self.data[ind][j-1])
     self.treeWidget.insertTopLevelItem(ind,parent)   
     
 def removeitem(self):
     item=self.treeWidget.currentItem()
     ind=self.treeWidget.indexFromItem(item).row()
     if(ind>=0):
         self.data.pop(ind)
         self.treeWidget.takeTopLevelItem(ind)


app = QtWidgets.QApplication(sys.argv)
window = mainwindow()
window.show()
app.exec_()
