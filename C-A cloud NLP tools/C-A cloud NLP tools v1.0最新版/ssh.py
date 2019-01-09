import paramiko
import os
from strProcess import cutLineBreak

def InitSSH():
    ssh = paramiko.SSHClient()  # 调用paramiko模块下的SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  # 加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
    ssh.connect('39.105.204.20', 22, 'root', 'zh@cloud1903')  # 连接远程主机，SSH端口号为22
    return ssh

def closeSSH(ssh):
    ssh.close()

def getUsersList(ssh):
    stdin, stdout, stderr = ssh.exec_command('ls /usr/cloudComputing/users/')
    li = stdout.readlines()
    li=cutLineBreak(li)
    return li

def getPasswd(username,ssh):
    stdin, stdout, stderr = ssh.exec_command('cat /usr/cloudComputing/users/'+username+'/passwd.txt')
    li = stdout.readlines()
    li = cutLineBreak(li)
    return li

def createDir(dirname , ssh, path = '/usr/cloudComputing/users/'):
    command = 'mkdir ' + path + dirname
    stdin, stdout, stderr = ssh.exec_command(command)

def createFile(filename,ssh):
    stdin, stdout, stderr = ssh.exec_command('cat > /usr/cloudComputing/users/' + filename + '/passwd.txt')

def writeFile(username, filename, str, ssh, path='/usr/cloudComputing/users/'):
    command = 'echo '+ "'" + str + "'"+ '>' + path + username + '/'+ filename
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

def writeFileAny(filename, path, str, ssh):
    command = 'echo ' + "'" + str + "'" + '>' + path + filename
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

def writeFileAtEnd(username, filename, str, ssh, path='/usr/cloudComputing/users/'):
    command = 'echo '+ "'" + str + "'"+ '>>' + path + username + '/'+ filename
    # print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

def deleteDir(dirname, ssh, path='/usr/cloudComputing/users/'):
    command = 'rm -rf ' + path + dirname
    stdin, stdout, stderr = ssh.exec_command(command)

def chmodDir(dirname, ssh, path = '/usr/cloudComputing/users/'):
    command = 'chmod o+w ' + path + dirname
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

def chmodDirAll(dirname, ssh, path = '/usr/cloudComputing/users/'):
    command = 'chmod o+w ' + path + dirname + ' -R'
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

def runOCR(filename, username, ssh, path = '/usr/cloudComputing/users/'):
    command = 'python36 /usr/cloudComputing/baidu.py -i '+ path + username + '/workSpace/' + filename
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)
    str=''
    for i in stdout.readlines():
        str = str + i
    return str

def runEE(filename, username, ssh, path = '/usr/cloudComputing/users/'):
    command = 'python36 /usr/cloudComputing/Emotion_Evaluation.py -i ' + path + username + '/workSpace/' + filename
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)
    point = ''
    for i in stdout.readlines():
        point = point + i
    return point

def runSeg(inputfile, backImage, username, workPath, ssh, path = '/usr/cloudComputing/users/'):
    command = 'python36 /usr/cloudComputing/Segmentation.py -i ' + inputfile + ' -p ' + backImage + ' -pa ' + workPath
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

# def copeFile(filename, username, passwd, ssh, path='/usr/cloudComputing/users/'):
#     file = open("passwd.txt","w")
#     file.write(passwd)
#     file.close()
#     result = os.system('scp E:\Study\ProfessionalCourse\Python项目\CloudComputing\passwd.txt '
#                        'root@39.105.204.20:/usr/cloudComputing/users/test passwd=zh@cloud1903')

#
#ssh = InitSSH()

#runOCR('test2.jpg','test',ssh)
#print(getUsersList(ssh))
# li = getUsersList(ssh)
# passwd=getPasswd('zhanghao',ssh)
# #createDir('test')
# #createFile('test')
# #copeFile('passwd.txt','test','123456',ssh)
# writeFile('test', 'passwd.txt','123456',ssh)
# print(li)
# print(passwd)
