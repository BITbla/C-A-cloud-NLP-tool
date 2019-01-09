import jieba
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from Common import *

def Segmentation():
    f=open(Com.Seg_Path,'r')
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

    for a in range(15):
        print(wordlist[a])

    backgroud_Image=plt.imread(Com.Seg_Photo)

    wc = WordCloud(
        background_color='white',# 设置背景颜色
        mask=backgroud_Image,# 设置背景图片
        font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=20, # 设置最大现实的字数
        stopwords=STOPWORDS,# 设置停用词
        max_font_size=100,# 设置字体最大值
        random_state=10# 设置有多少种随机生成状态，即有多少种配色方案
    )
    wc.generate_from_frequencies(crydict)
    plt.imshow(wc)
    plt.savefig('wordcloud.png')
    plt.show()


Segmentation()