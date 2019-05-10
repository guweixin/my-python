#coding: utf-8
import os
import shutil
import cv2

# 图片文件名
image_path = "/work/00_data/cheliang_leixing/整理的的数据备份/cheliang_type_part4/orig"
save_path = "/home/niezhongliang/桌面/cheliang/"
brand_name = "帝豪"

files = os.listdir(image_path)
for image in files:
    img = cv2.imread(image_path + "/"+image)
    cv2.namedWindow("hehe")
    cv2.imshow("hehe",img)

    print(save_path + brand_name + "/" + image)
    key = cv2.waitKey()
    # print key
    if (key == 1048603):    # ESC
        break
    elif (key == 1048586): # Enter
        shutil.move(image_path+"/"+image, save_path+brand_name+"/"+image)
    else:
        continue