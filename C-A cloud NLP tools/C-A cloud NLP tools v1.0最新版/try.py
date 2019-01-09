import os
import cv2
import numpy as np
##image_out_text    image_out_head

dst_dir1="./result_word/"#产出目录1
dst_dir2="./result_num/"#产出目录2
min_val=1000#最小行像素和
min_val_y=500
min_range_y=30
min_range=30#最小行宽
#peek_ranges=[]
#行化分割，返回每个行的起止区间
def extract_peek(array_vals, minimun_val, minimun_range):#参数说明：行像素元组，用于筛选的行像素最小值
    start_i = None
    end_i = None
    peek_ranges = []
    for i, val in enumerate(array_vals):
        if val > minimun_val and start_i is None:#有文字
            start_i = i#确定起始行
        elif val > minimun_val and start_i is not None:#有文字
            pass
        elif val < minimun_val and start_i is not None:#文字终结
            if i - start_i >= minimun_range:#行长度大于设定最小值
                end_i = i#确定结束行
                print(end_i - start_i)#打印行块大小
                peek_ranges.append((start_i, end_i))#记录行块大小
                start_i = None#重置初始值
                end_i = None
        elif val < minimun_val and start_i is None:
            pass
        else:
            raise ValueError("cannot parse this case...")
    return peek_ranges

def cutImage(img,peek_ranges,vertical_peek_ranges2d):
    count=0
    for i, peek_range in enumerate(peek_ranges):
        for j,vertical_range in enumerate(vertical_peek_ranges2d[i]):
            x = vertical_range[0]
            y = peek_range[0]
            w = vertical_range[1] - x
            h = peek_range[1] - y
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            count = count+1
            # if (peek_range[1]-y) > (vertical_range[1]-x):
            #     img1 = img[y:peek_range[1], x:x+(peek_range[1]-y)]
            # else:
            #     img1 = img[y:y+(vertical_range[1]-x), x:vertical_range[1]]
            img1 = img[y:peek_range[1], x:vertical_range[1]]
            new_shape = (100, 100)
            img1 = cv2.resize(img1, new_shape)
            # cv2.imshow("Test", img1)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if i==2 and j>2:
                cv2.imwrite(dst_dir2 + str(count) + ".png", img1)
            elif j==2:
                pass
            else:
                cv2.imwrite(dst_dir1 + str(count) + ".png", img1)
            # cv2.rectangle(img, pt1, pt2, color)

def Get_text(image):
    size = image.shape
    print("原图像大小（高，宽，颜色类型）：")
    print(size)  # 输入图像的大小

    # 缩放图片
    # 等比缩放不同图像处理的结果不一样，弃之
    # image_out1=cv2.resize(image,(round(size[1]*0.5),round(size[0]*0.5)),cv2.INTER_LINEAR)
    image_out1 = cv2.resize(image, (1209, 765), cv2.INTER_LINEAR)  # 中间是缩放图像的大小元组（宽，高）
    # 截取文字部分
    image_out_text = image_out1[280:650, 150:610]  # 第一个参数是高，第二个参数是宽
    #转化为灰度图
    image_out_text_gray = cv2.cvtColor(image_out_text, cv2.COLOR_RGB2GRAY)
    #图像平滑
    kernel = np.ones((2, 2), np.uint8)
    #dst1 = cv2.erode(image_out_text_gray, kernel, iterations=1)
    dst = cv2.morphologyEx(image_out_text_gray, cv2.MORPH_CLOSE, kernel)
    #ret,binary=cv2.threshold(image_out_text_gray,50,255,cv2.THRESH_BINARY_INV)
    # 自适应的阈值
    binary = cv2.adaptiveThreshold(dst, 255, \
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                   cv2.THRESH_BINARY_INV,15,15)
    #单字分割
    horizontal_sum = np.sum(binary, axis=1)#计算单行像素和 产出一个元组序列（行数，像素值总和）
    peek_ranges = extract_peek(horizontal_sum, min_val, min_range)
    line_seg_adaptive_threshold = np.copy(binary)
    for i, peek_range in enumerate(peek_ranges):
        x = 0
        y = peek_range[0]
        w = line_seg_adaptive_threshold.shape[1]
        h = peek_range[1] - y
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(line_seg_adaptive_threshold, pt1, pt2, 255)
    # cv2.imshow("Test", line_seg_adaptive_threshold)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    vertical_peek_ranges2d = []#垂直分割
    for peek_range in peek_ranges:
        start_y = peek_range[0]
        end_y = peek_range[1]
        line_img = binary[start_y:end_y, :]
        vertical_sum = np.sum(line_img, axis=0)
        vertical_peek_ranges = extract_peek(vertical_sum, min_val_y, min_range_y)
        vertical_peek_ranges2d.append(vertical_peek_ranges)
    cutImage(binary,peek_ranges,vertical_peek_ranges2d)
    #print(ret)
    #测试
    # cv2.imshow("Test", binary)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def Get_head(image):
    size = image.shape
    print("原图像大小（高，宽，颜色类型）：")
    print(size)  # 输入图像的大小

    # 缩放图片
    # 等比缩放不同图像处理的结果不一样，弃之
    # image_out1=cv2.resize(image,(round(size[1]*0.5),round(size[0]*0.5)),cv2.INTER_LINEAR)
    image_out1 = cv2.resize(image, (1209, 765), cv2.INTER_LINEAR)  # 中间是缩放图像的大小元组（宽，高）
    img_head=image_out1[275:700,810:1150]
    cv2.imshow("Test", img_head)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=cv2.imread("test1.jpg")
#饭卡上单字的截取
Get_text(image)
#饭卡上头像的截取
# Get_head(image)
#image_out_head=image_out1[290:710,800:1160]

