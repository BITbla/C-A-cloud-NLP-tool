#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ftplib import FTP
import sys
import importlib
importlib.reload(sys)

def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)

    ftp.connect(host, 21)
    ftp.set_pasv(False)
     # 如果被动模式由于某种原因失败，请尝试使用活动模式。
    print(ftp.getwelcome())
    ftp.login(username, password)
    return ftp

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从服务器下载文件到本地
def downloadfile(ftp, filename, remotepath, localpath):
	bufsize = 1024 #设置缓冲块大小
	fp = open(localpath + filename,'wb') #以写模式在本地打开文件
	ftp.retrbinary('RETR ' + remotepath + filename, fp.write, bufsize) #接收服务器上文件并写入本地文件
	ftp.set_debuglevel(0) #关闭调试
	fp.close()

def downloadfileByfullpath(ftp, remotepath, localpath):
    bufsize = 1024  # 设置缓冲块大小
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()

#Test

ftp = ftpconnect("39.105.204.20","ftpuser2","ftpuser2")
# # downloadfile(ftp, 'NLPTest.py','/usr/cloudComputing/', '' )
# # #uploadfile(ftp,"baidu.py","E:\\Study\\ProfessionalCourse\\Python项目\\OCR\\baidu.py")
# uploadfile(ftp,"/usr/cloudComputing/test2.jpg","test2.jpg")
uploadfile(ftp,"/usr/cloudComputing/baidu.py","baidu.py")
uploadfile(ftp,"/usr/cloudComputing/Common.py","Common.py")
uploadfile(ftp,"/usr/cloudComputing/Segmentation.py","Segmentation.py")
uploadfile(ftp,"/usr/cloudComputing/Emotion_Evaluation.py","Emotion_Evaluation.py")
uploadfile(ftp,"/usr/cloudComputing/strProcess.py","strProcess.py")
# uploadfile(ftp,"/usr/cloudComputing/dict/neg.txt","dict/neg.txt")
# uploadfile(ftp,"/usr/cloudComputing/dict/no.txt","dict/no.txt")
# uploadfile(ftp,"/usr/cloudComputing/dict/plus.txt","dict/plus.txt")
# uploadfile(ftp,"/usr/cloudComputing/dict/pos.txt","dict/pos.txt")

uploadfile(ftp,"/usr/cloudComputing/sanguojiexuan.txt","sanguojiexuan.txt")
uploadfile(ftp,"/usr/cloudComputing/report.txt","report.txt")