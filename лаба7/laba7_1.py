# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laba7_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(827, 472)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 791, 231))
        self.treeWidget.setColumnCount(7)
        self.treeWidget.setObjectName("treeWidget")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(280, 280, 131, 151))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 270, 81, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 270, 241, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridlayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(91, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridlayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(95, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridlayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(95, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridlayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridlayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.layoutWidget.raise_()
        self.treeWidget.raise_()
        self.graphicsView.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "№"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Журнал"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Статья"))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Авторы"))
        self.treeWidget.headerItem().setText(4, _translate("Form", "год"))
        self.treeWidget.headerItem().setText(5, _translate("Form", "Номер"))
        self.treeWidget.headerItem().setText(6, _translate("Form", "Страница"))
        self.pushButton_5.setText(_translate("Form", "очистить"))
        self.pushButton.setText(_translate("Form", "Загрузить"))
        self.pushButton_4.setText(_translate("Form", "удалить запись"))
        self.pushButton_3.setText(_translate("Form", "Добавить запись"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
