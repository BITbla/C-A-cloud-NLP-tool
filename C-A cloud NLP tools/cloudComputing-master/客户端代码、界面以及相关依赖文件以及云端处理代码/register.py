# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_registerForm(object):
    def setupUi(self, registerForm):
        registerForm.setObjectName("registerForm")
        registerForm.resize(610, 440)
        self.label_2 = QtWidgets.QLabel(registerForm)
        self.label_2.setGeometry(QtCore.QRect(190, 160, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(registerForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 160, 150, 25))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(registerForm)
        self.label_3.setGeometry(QtCore.QRect(190, 230, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(registerForm)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 230, 150, 25))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.confirmButton = QtWidgets.QPushButton(registerForm)
        self.confirmButton.setGeometry(QtCore.QRect(250, 320, 93, 28))
        self.confirmButton.setObjectName("confirmButton")
        self.label_4 = QtWidgets.QLabel(registerForm)
        self.label_4.setGeometry(QtCore.QRect(190, 90, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(registerForm)
        self.lineEdit.setGeometry(QtCore.QRect(300, 90, 150, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(registerForm)
        QtCore.QMetaObject.connectSlotsByName(registerForm)
        registerForm.setTabOrder(self.lineEdit, self.lineEdit_2)
        registerForm.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        registerForm.setTabOrder(self.lineEdit_3, self.confirmButton)

    def retranslateUi(self, registerForm):
        _translate = QtCore.QCoreApplication.translate
        registerForm.setWindowTitle(_translate("registerForm", "Form"))
        self.label_2.setText(_translate("registerForm", "password"))
        self.label_3.setText(_translate("registerForm", "confirm"))
        self.confirmButton.setText(_translate("registerForm", "confirm"))
        self.label_4.setText(_translate("registerForm", "username"))

