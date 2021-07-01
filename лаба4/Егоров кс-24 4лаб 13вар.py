from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("laba4.ui") # расположение вашего файла .ui
win.show()

http="http://maydome.com" 
variant="_v13."
def worcstr(str1):
 if str1.find('\\') >=0:
   str1=str1.replace('\\','/')
   str1=http+str1[str1.index("/"):]
 s2= list(str1.split("/"))
 s2=s2[len(s2)-1].replace('.',variant)
 if str1.count("/" )>=4 :
   str1=str1[:str1.rfind("/")]
   str1=str1[:str1.rfind("/")+1]
 else:
    str1=str1[:str1.rfind("/")+1]
 str1=str1+s2
 return str1

def click():
  strArr= win.textEdit.toPlainText()
  strArr = list(strArr.split("\n"))
  for i in range(len(strArr)):
   strArr[i]=worcstr(strArr[i])
  strArr='\n'.join(strArr)
  win.textEdit_2.setText(strArr)
win.pushButton.clicked.connect(click )


sys.exit(app.exec())
