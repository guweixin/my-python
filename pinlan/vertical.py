import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def split_str(charlist, text, bbox):
    ''' 通过字符间隔均值，切分字符串'''
    seg_results = []
    strlist = []
    sum=0
    start = 0

    for i in range(1, len(charlist)):
        sum = sum + (charlist[i][2]-charlist[i-1][2])
    mean = sum // (len(charlist)-1)

    for i in range(1, len(charlist)):
        if (charlist[i][2] - charlist[i - 1][2]) > mean:
            str1 = [start, i-1]
            strlist.append(str1)
            start = i
        if i == len(charlist)-1:
            str1 = [start, i]
            strlist.append(str1)

    for val in strlist:
        index_start, index_end = val
        x0,y0,y1 = bbox[0], bbox[1] ,bbox[3]
        new_bbox = [x0+charlist[index_start][0], y0, x0+charlist[index_end][1], y1]
        new_text = text[index_start:index_end+1]
        seg_result = [new_bbox, new_text]
        seg_results.append(seg_result)

    # print('len_text:    ',len(text))
    # print('len_charlist: ',len(charlist))
    # print('len_strlist: ', len(strlist))
    # print(strlist)
    # print(text)
    return seg_results

def split_char(a, img, text):
    '''根据垂直投影值选定行分割点,切分出每个字符'''
    h, w, _ = img.shape
    lfg = [0 for col in range(w)]
    incol = 1
    start = 0
    j = 0
    charlist = []
    showimg = img.copy()
    for i in range(0, w):
        if incol == 1 and a[i] > 0:     # 从空白区进入文字区
            start = i                   # 记录起始列分割点
            incol = 0
        elif (i - start > 2) and a[i] <= 0 and incol == 0:  # 从文字区进入空白区
            incol = 1
            lfg[j] = start - 1          # 保存列分割位置
            lfg[j] = i + 1
            x1 = start - 1
            x2 = i + 1
            j = j + 1
            cv2.rectangle(showimg, (x1, 0), (x2, h), (255, 0, 0), 1)
            bbox =[x1, x2, (x1+x2)/2]
            charlist.append(bbox)

    if len(charlist) != len(text):
        print('-'*50)
        print('len_text:    ',len(text))
        print('len_charlist: ',len(charlist))
        print(text)
        cv2.imshow('aaa',showimg)
        cv2.waitKey(0)
        if len(charlist) < len(text):

            print('ddsddssdsfsdshzsdfghjkl;sdfghjk')


    return charlist

def vertical(img):
    """
    对粘连的小图进行垂直投影
    Args:
        img: 在检测过程中出现粘连的小图
    Returns:
        a=[]: 图像垂直方向上的投影信息
    """
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将BGR图转为灰度图
    ret, thresh1 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY)  # 将图片进行二值化(130,255)之间的点均变为255(背景),返回值ret为阈值
    # 3 为Block size, 5为param1值
    # thresh1 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
    (h, w) = thresh1.shape              # 返回高和宽
    a = [0 for z in range(0, w)]        # 初始化一个长度为w的数组，用于记录每一列的黑点个数
    # 记录每一列的波峰
    for j in range(0, w):               # 遍历一列
        for i in range(0, h):           # 遍历一行
            if thresh1[i, j] == 0:      # 如果改点为黑点
                a[j] += 1               # 该列的计数器加一计数
                thresh1[i, j] = 255     # 记录完后将其变为白色

    for j in range(0, w):               # 遍历每一列
        for i in range((h - a[j]), h):  # 从该列应该变黑的最顶部的点开始向最底部涂黑
            thresh1[i, j] = 0           # 涂黑

    if 1:
        # #     此时的thresh1便是一张图像向垂直方向上投影的直方图
        # #     如果要分割字符的话，其实并不需要把这张图给画出来，只需要的到a=[]即可得到想要的信息
        plt.imshow(thresh1, cmap=plt.gray())
        plt.show()
        cv2.imshow('gray',GrayImage)
        cv2.imshow('img', thresh1)
    return a

def segmentation(image , bbox, text):
    seg_results = []
    img = image[bbox[1]:bbox[3], bbox[0]:bbox[2]]
    a = vertical(img)
    charlist = split_char(a, img, text)
    if len(charlist) != 1:
        seg_results = split_str(charlist, text, bbox)
    cv2.imshow('imgimg', img)
    cv2.waitKey(0)
    return seg_results