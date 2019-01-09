import sys
from Serve import *
from MainWindowUi import *
from Login import *
from register import *
from info import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Serve import Serve


class infoWindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(infoWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.confirmEvent)

    def confirmEvent(self):
        self.hide()


class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.loginEvent)
        self.pushButton.clicked.connect(self.registerEvent)

    # 定义登录按钮的功能
    def loginEvent(self):
        username = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if(not serve.checkUsername(username)):
            self.showErrInfo("用户名不存在！")
        elif(not serve.checkPasswd(username,passwd)):
            self.showErrInfo("账户密码不匹配！")
        else:
            self.hide()
            self.dia = LeftTabWidget()
            self.dia.show()

    #定义注册按钮功能
    def registerEvent(self):
        self.hide()
        self.dia = RegisterWindow()
        self.dia.show()

    def showErrInfo(self,str):
        self.dia = infoWindow()
        self.dia.label.setText(str)
        self.dia.show()


class RegisterWindow(QtWidgets.QWidget, Ui_registerForm):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setupUi(self)
        self.confirmButton.clicked.connect(self.confirmEvent)

    def confirmEvent(self):
        username = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        confirm = self.lineEdit_3.text()

        users = serve.getUsers()
        if(users.count(username)>=1):
            self.showErrInfo("用户名已存在！")
        elif(passwd != confirm):
            self.showErrInfo("两次输入密码不匹配！")
        elif(username==''):
            self.showErrInfo("用户名不能为空！")
        elif(passwd==''):
            self.showErrInfo("密码不能为空！")
        else:
            serve.register(username,passwd)
            self.hide()
            self.dia = LoginWindow()
            self.dia.show()
        # elif(not serve.checkPasswd(username,passwd)):
        #     self.showErrInfo("账户密码不匹配")

    def showErrInfo(self,str):
        self.dia = infoWindow()
        self.dia.label.setText(str)
        self.dia.show()

serve = Serve()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
