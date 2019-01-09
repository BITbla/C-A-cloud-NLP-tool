#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
from aip import AipOcr
import argparse
from strProcess import *

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputFile', required=True, help = '输入的文件名（.jpg；.png）')
parser.add_argument('-o', '--outputFile', required=False, help = '输出的文件名（.jpg；.png）')
parser.add_argument('-t', '--textFile', required=False, help= 'ocr的结果')
args = parser.parse_args()

#print(args)

def main(args):
    """ 你的 APPID AK SK  图2的内容"""
    APP_ID = '15092570'
    API_KEY = 'tFve89Ea4ccLc0t9j4Aq4WkM'
    SECRET_KEY = 'pCeeSECSGyj6KqWchFxKtaMGusy8zfz8'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    fname = args.inputFile

    image = get_file_content(fname)

    """ 调用通用文字识别, 图片参数为本地图片 """
    results = client.general(image)["words_result"]  # 还可以使用身份证驾驶证模板，直接得到字典对应所需字段

    img = cv2.imread(fname)

    textName= getName(fname)+'Text.txt'
    if args.textFile!=None:
        textName =args.textFile
    file = open(textName, 'w+')
    for result in results:
        text = result["words"]
        location = result["location"]
        file.write(text+'\n')

        print(text)
        # 画矩形框
        cv2.rectangle(img, (location["left"], location["top"]),
                      (location["left"] + location["width"], location["top"] + location["height"]), (0, 255, 0), 2)

    file.close()
    if args.outputFile == None :
        cv2.imwrite(getName(fname)+"Result.jpg", img)
    else:
        cv2.imwrite(args.outputFile, img)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    main(args)
