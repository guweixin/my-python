# -*- coding=utf-8 -*-
'''将.json格式的标注文件转换为txt后，进行扣图'''
'''将.json格式的标注文件转换为txt后，进行扣图'''
import cv2
import glob
import os
import numpy as np


def four_point_transform(image, rect):
    """
    提取倾斜矩形图像并矫正
    :param image:输入为原始大图，格式为cv2
    :param rect:倾斜矩形四个顶点坐标，顺序为左上，右上，右下，左下
    :return warped:裁剪矫正后的矩形图像
    """
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def order_points(pts):
    """
    求矩形顶点重新排序
    :param pts:矩形四个顶点坐标，顺序不固定
    :return rect list:矩形四个顶点坐标，调整顺序为左上，右上，右下，左下
    """
    rect = np.zeros((4, 2), dtype="float32")

    s = np.sum(pts, axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def crop_image(txt_path,image):
    boxes = []
    f = open(txt_path)
    old_box = f.readlines()
    for i in old_box:
        boxes.append(i.split(',')[:-1])
    for j,box_temp in enumerate(boxes):
        box_temp = [int(i) for i in box_temp]
        cnt = [[box_temp[0], box_temp[1]], [box_temp[2], box_temp[3]], [box_temp[4], box_temp[5]],
               [box_temp[6], box_temp[7]]]
        cnt = np.array(cnt)  # 必须是array数组的形式
        print('cnt', cnt)
        rect = cv2.minAreaRect(cnt)  # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
        box_temp = order_points(box)
        img_temp = four_point_transform(image, box_temp)
        img_name = os.path.basename(txt_path).split('.')[0]+str(j)+'.jpg'
        cv2.imwrite(os.path.join('/Users/cecilia/Desktop/crop', img_name), img_temp)


if __name__=='__main__':
    img_list = glob.glob('/Users/cecilia/Desktop/label/*.jpg')
    for img in img_list:
        print(img)
        image = cv2.imread(img)
        txt_path = img.replace('jpg', 'txt')
        crop_image(txt_path, image)