# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 18))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 171, 18))
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(30, 250, 351, 20))
        self.labelAmount.setObjectName("labelAmount")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(230, 60, 131, 24))
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlives = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlives.setGeometry(QtCore.QRect(230, 90, 121, 24))
        self.checkBoxOlives.setObjectName("checkBoxOlives")
        self.checkBoxSausages = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausages.setGeometry(QtCore.QRect(230, 120, 141, 24))
        self.checkBoxSausages.setObjectName("checkBoxSausages")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $ 10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
        self.labelAmount.setText(_translate("Dialog", "TextLabel"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra cheese $ 1"))
        self.checkBoxOlives.setText(_translate("Dialog", "Extra Olives $ 1"))
        self.checkBoxSausages.setText(_translate("Dialog", "Extra Sausages $ 1"))
