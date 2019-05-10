#coding=utf-8
import numpy as np
import cv2
import random
import math
import os


def segmap2bimg(img):
    if len(img.shape) > 2:
        if img.shape[2] != 1:
            # 灰度化
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#       b, g, r = cv2.split(img)
#       img = b
    # 值大于0的都为255
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    return thresh

# 获得每个字符的最小外接矩形框的四个点的坐标[array([,],[,],[,],[,])]
def getBoundingRect(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    item_num = max([max(img[i,:]) for i in range(img.shape[0])])
    boxs = []
    for i in range(item_num):
        mask = cv2.inRange(img, i+1, i+1)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,  17)
        # 寻找连通矩形
        image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            rect = cv2.minAreaRect(contour)
            box = np.int0(cv2.boxPoints(rect))
            boxs.append(box)
            # centor = np.mean(box, axis=0)
            # img = cv2.polylines(img, [box], True, (255, 0, 0))
    return boxs

# 得到垂直矩形框
def getSimpleBounding(image, filename):
    img = image.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取像素类别
    item_nums = set([])
    for i in range(len(img)):
        item_nums |= set(img[i].tolist())
    # item_num = max([max(img[i,:]) for i in range(img.shape[0])])
    print('item: ', item_nums)
    rects = []
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))
    for i in item_nums:
        if i == 0:
            continue
        if i == 255:
            continue
        mask = cv2.inRange(img, i, i)
        
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,  kernel)
        # 寻找连通矩形
        _, contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_path = str(i)
        if not os.path.exists(num_path):
            os.makedirs(num_path)
        count = 0
        for contour in contours:
            rect = cv2.boundingRect(contour)
            num_save_path = num_path + '/' + str(count) + '_' + filename
            count += 1
            x,y,w,h = rect
            cv2.imwrite(num_save_path, segmap2bimg(image[y:y+h, x:x+w]))
            rects.append(rect)
    return rects

def main():
    with open('/mnt/sources/data/chejian/chejiahao_segnet/shujubugeide /gray.txt', 'r') as f:
        for line in f.readlines():
            img_path = line.strip()
            img = cv2.imread(img_path)
            if type(img) == type(None):
                continue
            filename = img_path[80:]
            rects = getSimpleBounding(img, filename)
            if len(rects) != 17:
                for i in rects:
                    x,y,w,h = i
                    img = segmap2bimg(img)
                    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0,0), 2)
                cv2.imshow(filename, img)
                cv2.waitKey(0)
        cv2.destroyAllWindows()
    # filepath = '/media/hena/e23b4863-55d1-4de6-88ae-89d0ee37cab7/data/gray_bihua/chejiahao_segmap_22.png'
    # img = cv2.imread(filepath)
    # filename = filepath[82:]
    # rects = getSimpleBounding(img, filename)
    # print(len(rects))
    # for i in rects:
    #     x,y,w,h = i
    #     img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0,0), 2)
    # # cv2.imwrite('aaaaaaaaaaaaaaaaa.jpg', img)
    # cv2.imshow('error', img)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()