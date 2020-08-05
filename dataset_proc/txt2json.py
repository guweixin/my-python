# -*- coding=utf-8 -*-
"""将模型跑出来的.txt文件生成.json，实现预标注"""
import json
import os
from glob import glob
import cv2
import base64

def custombasename(fullname):
    return os.path.basename(os.path.splitext(fullname)[0])

def txt2json(IN_PATH, OUT_PATH, IMG_PATH):
    file_list = glob(IN_PATH + "/*.txt")
    for i in range(len(file_list)):
        with open(file_list[i]) as f:
            data_json = {}
            data_json['version'] = "4.5.5"
            data_json['flags'] = {}

            # 读取txt，获取预标注数据
            label_str = f.read()
            label_str_list = label_str.split('\n')

            # 加载图像，获取相关长宽信息，以及base64编码
            img_name = custombasename(file_list[i]) + ".jpg"
            img_name = img_name.replace("res_", "")
            img = cv2.imread(IMG_PATH + img_name)
            h, w, _ = img.shape
            data_json['imagePath'] = img_name
            data_json['imageHeight'] = h
            data_json['imageWidth'] = w
            with open(img_name, 'rb') as f_img:
                base64_data = base64.b64encode(f_img.read())
                s = base64_data.decode()
                data_json['imageData'] = s

            shapes = []
            for label_point in label_str_list:
                label_point_list = label_point.split(',')
                # 此处是将x1,y1,x2,y2,x3,y3,x4,y4转为json
                if len(label_point_list) != 8:
                    continue
                label_point_list = [float(x) for x in label_point_list]
                points = []
                point = []
                for index, x in enumerate(label_point_list):
                    point.append(x)
                    if len(point) == 2:
                        points.append(point)
                        point = []
                # 将坐标值写入
                shape = {}
                shape["label"] = "text"
                shape["points"] = points
                shape["group_id"] = None
                shape["shape_type"] = "polygon"
                shape["flags"] = {}
                shapes.append(shape)
            data_json['shapes'] = shapes

            # 保存json文件
            out_file = OUT_PATH + "/" + custombasename(file_list[i]) + ".json"
            out_file = out_file.replace("res_", "")
            fout = open(out_file, "w")
            fout.write(json.dumps(data_json))
            fout.close()

if __name__ == "__main__":
    IN_PATH = "/Users/fiona/Desktop/txt2json/submit_ic15/"
    OUT_PATH = "/Users/fiona/Desktop/txt2json/img/"
    IMG_PATH = "/Users/fiona/Desktop/txt2json/img/"
    os.chdir(IMG_PATH)
    # 查看当前工作目录
    print("当前的工作目录为：%s" % os.getcwd())
    txt2json(IN_PATH, OUT_PATH, IMG_PATH)
