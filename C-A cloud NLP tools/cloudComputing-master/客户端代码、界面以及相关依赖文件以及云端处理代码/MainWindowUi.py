#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget, QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFileDialog
import User
import cihui
import duanluo
import pianzhang
from Serve import Serve, UserControl
from strProcess import *


class MainWindow1(QWidget,User.Ui_Form):
    def __init__(self):
        super(MainWindow1, self).__init__()
        self.setupUi(self)


class MainWindow2(QWidget,cihui.Ui_Form):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.setupUi(self)

    def setPhoto(self,filename):
        pix = QPixmap(filename).scaled(570,570)
        self.Label_Show.setGeometry(20, 20, 570, 510)
        self.Label_Show.setPixmap(pix)


class MainWindow3(QWidget,duanluo.Ui_Form):
    def __init__(self):
        super(MainWindow3, self).__init__()
        self.setupUi(self)

class MainWindow4(QWidget,pianzhang.Ui_Form):
    def __init__(self):
        super(MainWindow4, self).__init__()
        self.setupUi(self)

class LeftTabWidget(QWidget):
    '''左侧选项栏'''

    def __init__(self, username, identity):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')

        self.setWindowTitle('C-A云自然语言分析工具')
        with open('QListWidgetQSS.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.main_layout = QHBoxLayout(self, spacing=0)  # 窗口的整体布局
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = QListWidget()  # 左侧选项列表
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self.userWidget = MainWindow1()
        self.cihuiWidget = MainWindow2()
        self.duanluoWidget = MainWindow3()
        self.pianzhangWidet = MainWindow4()

        self._setup_ui()
        self.userControl = UserControl(username, identity)
        self.serve = Serve()

        self.userWidget.Label_UserName_2.setText(username)
        self.userWidget.Label_UserMassege_2.setText(identity)

        self.cihuiWidget.Upload.clicked.connect(self.openFile)
        self.userWidget.pushButton_SetPhoto.clicked.connect(self.openPhoto)
        self.duanluoWidget.OCRButton.clicked.connect(self.ImageOcr)
        self.duanluoWidget.pushButton_EA.clicked.connect(self.EEButton)


    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)  # list和右侧窗口的index对应绑定
        self.setGeometry(300,300,850,600)
        self.setFixedSize(850,550)
        self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['个人界面', '词汇分析', '段落分析', '篇章分析']
        #url_list = ['job_num_wordcloud.html', 'edu_need.html', 'salary_bar.html', 'edu_salary_bar.html']

        for i in range(4):
            self.item = QListWidgetItem(list_str[i], self.left_widget)  # 左侧选项的添加
            self.item.setSizeHint(QSize(30, 60))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示
            if i==0:
                self.right_widget.addWidget(self.userWidget)
            elif i==1:
                self.right_widget.addWidget(self.cihuiWidget)
            elif i==2:
                self.right_widget.addWidget(self.duanluoWidget)
            elif i==3:
                self.right_widget.addWidget(self.pianzhangWidet)
            #self.browser = QWebEngineView()  # 右侧用QWebView来显示html网页
            #self.browser.setUrl(QUrl.fromLocalFile('D://python//code//vision//%s' % url_list[i]))
            #self.right_widget.addWidget(self.browser)

    def openFile(self):
        openfile_name, fileType = QFileDialog.getOpenFileName(self, '选择文件', '', 'Text files(*.txt)')
        print(openfile_name)
        # self.cihuiWidget.setPhoto(openfile_name)
        self.uploadFileAtWorkSpace(openfile_name)
        return openfile_name

    def uploadFileAtWorkSpace(self, fullpath):
        path, filename = getPathAndFile(fullpath)
        ext = getExt(fullpath)
        if (ext == '.jpg' or ext == '.png' or ext == '.JPG' or ext == '.PNG'):
            self.serve.uploadFileAtWorkSpace(self.userControl.getUsername(), path, filename)

    def openPhoto(self):
        openfile_name, fileType = QFileDialog.getOpenFileName(self, '选择文件', '', '*.jpg;;*.png')
        ext = getExt(openfile_name)
        if (ext == '.jpg' or ext == '.png' or ext == '.JPG' or ext == '.PNG'):
            self.cihuiWidget.setPhoto(openfile_name)

    def ImageOcr(self):
        openfile_name, fileType = QFileDialog.getOpenFileName(self, '选择文件', '', '*.jpg;;*.png')
        ext =getExt(openfile_name)
        filename = getFile(openfile_name)
        if(ext=='.jpg'or ext == '.png' or ext =='.JPG'or ext == '.PNG'):
            self.uploadFileAtWorkSpace(openfile_name)
            text = self.serve.getTextOCR(filename, self.userControl.getUsername())
            self.duanluoWidget.textEdit_In.setText(text)

    def EEButton(self):
        text = self.duanluoWidget.textEdit_In.toPlainText()
        print(text)
        self.serve.writeFileAtWorkSpace(self.userControl.getUsername(),text, 'ee.txt')
        point = self.serve.getPoint('ee.txt', self.userControl.getUsername())
        self.duanluoWidget.Label_SetNum.setText(point)

def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget('test','test')
    main_wnd.show()

    # win = MainWindow()
    # win.show()
    app.exec()


if __name__ == '__main__':
    main()