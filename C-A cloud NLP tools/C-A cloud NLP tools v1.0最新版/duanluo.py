# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'duanluo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 550)
        self.textEdit_In = QtWidgets.QTextEdit(Form)
        self.textEdit_In.setGeometry(QtCore.QRect(70, 120, 451, 231))
        self.textEdit_In.setObjectName("textEdit_In")
        self.Lable_Hint = QtWidgets.QLabel(Form)
        self.Lable_Hint.setGeometry(QtCore.QRect(70, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Lable_Hint.setFont(font)
        self.Lable_Hint.setObjectName("Lable_Hint")
        self.pushButton_EA = QtWidgets.QPushButton(Form)
        self.pushButton_EA.setGeometry(QtCore.QRect(580, 220, 91, 41))
        self.pushButton_EA.setObjectName("pushButton_EA")
        self.Label_SetNum = QtWidgets.QLabel(Form)
        self.Label_SetNum.setGeometry(QtCore.QRect(70, 390, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Label_SetNum.setFont(font)
        self.Label_SetNum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_SetNum.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_SetNum.setObjectName("Label_SetNum")
        self.Label_SetColor = QtWidgets.QLabel(Form)
        self.Label_SetColor.setGeometry(QtCore.QRect(200, 390, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Label_SetColor.setFont(font)
        self.Label_SetColor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Label_SetColor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_SetColor.setStyleSheet("background-color:rgb(255, 89, 92)")
        self.Label_SetColor.setText("")
        self.Label_SetColor.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_SetColor.setObjectName("Label_SetColor")
        self.OCRButton = QtWidgets.QPushButton(Form)
        self.OCRButton.setGeometry(QtCore.QRect(580, 140, 91, 41))
        self.OCRButton.setObjectName("OCRButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Lable_Hint.setText(_translate("Form", "请输入用于分析的段落："))
        self.pushButton_EA.setText(_translate("Form", "情感分析"))
        self.Label_SetNum.setText(_translate("Form", "10.00"))
        self.OCRButton.setText(_translate("Form", "上传图片"))

