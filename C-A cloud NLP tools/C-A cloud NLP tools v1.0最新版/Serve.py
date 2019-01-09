from ssh import *
from ftp import uploadfile, downloadfile, ftpconnect,downloadfileByfullpath
import time
from strProcess import *

def getTime():
    timeStamp = int(time.time())
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

class Serve:
    def __init__(self):
        self.ssh = InitSSH()
        self.ftp = ftpconnect('39.105.204.20','ftpuser2','ftpuser2')

    def getUsers(self):
        users = getUsersList(self.ssh)
        return users

    def checkUsername(self, username):
        users = getUsersList(self.ssh)
        if(users.count(username)>=1):
            return True
        else:
            return False

    def checkPasswd(self,username,passwd):
        passwdInServe = getPasswd(username,self.ssh)[0]
        if(passwdInServe == passwd):
            self.writeLog(username, 'Login Sucessful!')
            return True
        else:
            # print(passwd)
            # print(passwdInServe)
            return False

    def register(self,username,passwd):
        createDir(username,self.ssh)
        createDir('workSpace', self.ssh, '/usr/cloudComputing/users/' + username + '/')
        createFile(username,self.ssh)
        createFile('log.txt',self.ssh)
        writeFile(username, 'passwd.txt', passwd,self.ssh)
        self.writeLog(username,'Register the account!')
        chmodDirAll(username,self.ssh)

    def deleteUser(self,username):
        deleteDir(username,self.ssh)

    def writeLog(self, username, transaction):
        writeFileAtEnd(username, 'log.txt', '----' + getTime() + '-----\n', self.ssh)
        writeFileAtEnd(username, 'log.txt', transaction + '\n', self.ssh)
        writeFileAtEnd(username, 'log.txt', '-------------------\n', self.ssh)

    def uploadFileAtWorkSpace(self, username, localpath, filename):
        remotepath = '/usr/cloudComputing/users/'+ username  + '/workSpace/' + filename
        print('re = '+remotepath)
        print('lo = ' +localpath+filename)
        uploadfile(self.ftp, remotepath , localpath + filename)
        self.writeLog(username,"Upload File " + filename)

    def getTextOCR(self, filename, username):
        self.writeLog(username, "OCR " + filename)
        return runOCR(filename, username, self.ssh)

    def getPoint(self, filename, username):
        self.writeLog(username, "Emotion_Evalution " + filename)
        return runEE(filename, username, self.ssh)

    def writeFileAtWorkSpace(self, username, text, filename):
        self.writeLog(username, "write " + text)
        writeFileAny('ee.txt', '/usr/cloudComputing/users/'+ username  + '/workSpace/', text, self.ssh )

    def getWDAndFre(self, workFile, backImage, username):
        inputFile = '/usr/cloudComputing/users/'+ username  + '/workSpace/' + workFile
        print("i= "+inputFile)
        runSeg(inputFile, ' /usr/cloudComputing/users/'+ username  + '/workSpace/' + backImage,
               username, ' /usr/cloudComputing/users/'+ username  + '/workSpace/', self.ssh)
        downloadfileByfullpath(self.ftp, cutExt(inputFile) + 'wc.png', getName(inputFile)+ 'wc.png' )
        downloadfileByfullpath(self.ftp, cutExt(inputFile) + 'Fre.txt', getName(inputFile) + 'Fre.txt')
        self.writeLog(username, "词频统计和词云生成！" )
        #downloadfile(self.ftp, )


class UserControl:
    def __init__(self, username, identity):
        self.username = username
        self.identity = identity
        #本机的工作目录
        self.workDir = os.getcwd()
        #远程的工作文件
        self.workFile = 'report.txt'
        self.backImage = 'timg.jpg'

    def getUsername(self):
        return self.username

    def getIdentity(self):
        return self.identity

    def setWorkDir(self,path):
        self.workDir =path

    def setWorkFile(self, filename):
        self.workFile = filename
#Test

serve = Serve()
#print(serve.getPoint('ee.txt','test'))
serve.getWDAndFre('report.txt', 'timg.jpg', 'test')
#chmodDir('test3',serve.ssh)
#serve.register( 'test', 'test')
#serve.writeFileAtWorkSpace('test','北京理工大学BEIJING INSTITUTE OF TECHNOLOGY姓名:张浩性别:男编号:1120161903单位:计算机学院', 'ee.txt')
# print(serve.checkUsername('test2'))
#serve.uploadFileAtWorkSpace( 'test','test1.jpg','test1.jpg')