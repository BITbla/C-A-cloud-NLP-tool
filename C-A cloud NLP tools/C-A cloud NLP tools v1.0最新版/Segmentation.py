import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from Common import *
import argparse
from strProcess import *

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputFile', required=False, help = '输入的文件名（.jpg；.png）')
parser.add_argument('-o', '--outputFile', required=False, help = '输出的文件名（.png）')
parser.add_argument('-p', '--backgroundPicture', required=False, help= '背景图片(.jpg;.png)')
parser.add_argument('-pa', '--workPath',  required=False, help = '工作路径')
args = parser.parse_args()

# print(args)
# args.intputFile = 'sanguojiexuan.txt'
# args.backgroundPicture = 'timg.jpg'

def Segmentation(args):
    print(args.inputFile)
    f = open(args.inputFile, 'r+')
    cry=f.read()
    f.close()
    crylist=list(jieba.cut(cry))
    crydict={}
    for word in crylist:
        if len(word)==1:
            continue
        else:
            crydict[word]=crydict.get(word,0)+1

    wordlist=list(crydict.items())
    wordlist.sort(key=lambda x:x[1],reverse=True)

    path = '/'
    if (args.workPath != None):
        path = args.workPath
    fre = open(path + getName(args.inputFile)+ 'Fre.txt','w+')
    for a in range(15):
        fre.write(str(wordlist[a])+ '\n')
        print(wordlist[a])

    fre.close()

    backgroud_Image=plt.imread(args.backgroundPicture)

    wc = WordCloud(
        background_color='white',# 设置背景颜色
        mask=backgroud_Image,# 设置背景图片
        font_path='/usr/share/fonts/chinese/TrueType/STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=20, # 设置最大现实的字数
        stopwords=STOPWORDS,# 设置停用词
        max_font_size=100,# 设置字体最大值
        random_state=10# 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.generate_from_frequencies(crydict)
    plt.imshow(wc)
    outFile = cutExt(args.inputFile) + 'wc.png'
    if(args.outputFile != None):
        outFile = args.outputFile
    print(outFile)
    plt.savefig(outFile)
    plt.show()

if __name__ == '__main__':
    Segmentation(args)