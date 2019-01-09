# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pianzhang.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 550)
        self.Label_Show = QtWidgets.QLabel(Form)
        self.Label_Show.setGeometry(QtCore.QRect(20, 20, 571, 511))
        self.Label_Show.setText("")
        self.Label_Show.setTextFormat(QtCore.Qt.AutoText)
        self.Label_Show.setPixmap(QtGui.QPixmap("back.png"))
        self.Label_Show.setWordWrap(False)
        self.Label_Show.setObjectName("Label_Show")
        self.Upload = QtWidgets.QPushButton(Form)
        self.Upload.setGeometry(QtCore.QRect(620, 50, 81, 41))
        self.Upload.setObjectName("Upload")
        self.Photo = QtWidgets.QPushButton(Form)
        self.Photo.setGeometry(QtCore.QRect(620, 140, 81, 41))
        self.Photo.setObjectName("Photo")
        self.Table = QtWidgets.QPushButton(Form)
        self.Table.setGeometry(QtCore.QRect(620, 230, 81, 41))
        self.Table.setObjectName("Table")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Upload.setText(_translate("Form", "上传文本"))
        self.Photo.setText(_translate("Form", "关键词提取"))
        self.Table.setText(_translate("Form", "图谱分析"))

