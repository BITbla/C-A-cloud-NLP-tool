# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow_Login):
        MainWindow_Login.setObjectName("MainWindow_Login")
        MainWindow_Login.resize(578, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Login)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 150, 150, 25))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 72, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 100, 150, 25))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow_Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Login)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Login.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Login)
        MainWindow_Login.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow_Login.setTabOrder(self.lineEdit_2, self.pushButton_2)
        MainWindow_Login.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, MainWindow_Login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Login.setWindowTitle(_translate("MainWindow_Login", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow_Login", "Login"))
        self.label_2.setText(_translate("MainWindow_Login", "password"))
        self.pushButton.setText(_translate("MainWindow_Login", "Register"))
        self.label.setText(_translate("MainWindow_Login", "username"))

