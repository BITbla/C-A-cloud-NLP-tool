import os

def cutLineBreak(str):
    for i in range(len(str)):
        str[i]=str[i].replace('\n','')
    return str

def getPathAndFile(fullpath):
    path, filename = os.path.split(fullpath)
    path = path + '/'
    return path,filename

def getPath(fullpath):
    path, filename = os.path.split(fullpath)
    path = path + '/'
    return path

def getFile(fullpath):
    path, filename = os.path.split(fullpath)
    return filename

def getExt(fullpath):
    path, filename = os.path.split(fullpath)
    path = path + '/'
    name, ext = os.path.splitext(filename)
    return ext

def getName(fullpath):
    path, filename = os.path.split(fullpath)
    path = path + '/'
    name, ext = os.path.splitext(filename)
    return name

def listToStr(li):
    str = ''
    for i in li:
        str = str + i
    return str

def cutExt(fullpath):
    path, filename = os.path.split(fullpath)
    path = path + '/'
    name, ext = os.path.splitext(filename)
    return path + name