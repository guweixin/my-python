from xml.dom.minidom import parse
import xml.dom.minidom
from PIL import Image, ImageDraw
import numpy as np
import cv2
import os
# import shutil
# 定义过滤规则函数，统计数量分布和提取特征时均调用该函数
def filter_sku(class_name):
    # 瓶装味达美味极鲜 的合并映射规则
    #     if class_name not in ['1LFAT味达美味极鲜酱油', '800ML味达美味极鲜酱油', '300ML味达美味极鲜酱油', '150ML味达美味极鲜酱油', '500ML味达美味极鲜酱油']:
    #         return None
    #     if class_name == '1LFAT味达美味极鲜酱油':
    #         class_name = '800ML味达美味极鲜酱油'
    #     elif class_name in ['300ML味达美味极鲜酱油', '150ML味达美味极鲜酱油']:
    #         class_name = '500ML味达美味极鲜酱油'

    if class_name == '味达美清香米醋190ML':
        class_name = '190ML味达美清香米醋'
    elif class_name == '味达美清香米醋460ML':
        class_name = '460ML味达美清香米醋'

    #############################################################
    #
    # if class_name == '190ML味达美清香米醋':
    #     class_name = '160ML禾然有机酱油'
    #
    # elif class_name == '160ML遵循自然原酿酱油':
    #     class_name = '160ML禾然有机酱油'
    #
    # elif class_name == '190ML味达美臻品料酒':
    #     class_name = '160ML禾然有机酱油'
    #
    # elif class_name == '230G味达美臻品蚝油':
    #     class_name = '160ML禾然有机酱油'
    #
    # elif class_name == '160ML六月鲜柠檬蒸鱼酱油':
    #     class_name = '160ML禾然有机酱油'
    #
    # elif class_name == '460ML味达美清香米醋':
    #     class_name = '500ML禾然有机酱油'
    #
    # elif class_name == '500ML遵循自然原酿酱油':
    #     class_name = '500ML禾然有机酱油'
    #
    # elif class_name == '450ML味达美臻品料酒':
    #     class_name = '500ML禾然有机酱油'
    #
    # elif class_name == '510G味达美臻品蚝油':
    #     class_name = '500ML禾然有机酱油'
    #
    # elif class_name == '380ML六月鲜柠檬蒸鱼酱油':
    #     class_name = '500ML禾然有机酱油'

    if class_name in ['300G葱伴侣六月香甜面酱', '300G葱伴侣六月香豆瓣酱', '300G葱伴侣六月香辣椒酱', '300G禾然有机豆瓣酱',
                      '500G葱伴侣六月香甜面酱', '500G葱伴侣六月香豆瓣酱', '500G葱伴侣六月香辣椒酱', '500G禾然有机豆瓣酱',
                      '800G葱伴侣六月香甜面酱', '800G葱伴侣六月香豆瓣酱', '800G葱伴侣六月香辣椒酱', '800G禾然有机豆瓣酱',
                      '150ML味达美味极鲜酱油', '300ML味达美味极鲜酱油', '500ML味达美味极鲜酱油', '800ML味达美味极鲜酱油',
                      '1.3L味达美味极鲜酱油', '1.8L味达美味极鲜酱油', '1LFAT味达美味极鲜酱油',
                      '150ML味达美味极鲜', '300ML味达美味极鲜', '500ML味达美味极鲜', '800ML味达美味极鲜',
                      '1.3L味达美味极鲜', '1.8L味达美味极鲜', '1LFAT味达美味极鲜',
                      '160ML六月鲜大众红烧酱油', '500ML六月鲜大众红烧酱油',
                      '160ML六月鲜特级酱油', '500ML六月鲜特级酱油',
                      '1.3L六月鲜特级酱油', '1.8L六月鲜特级酱油',
                      ]:
        #     else:
        return None

    return class_name


predict_class_dict = {
    # '300ml': 0,
    # '900ml': 1,
    # '1600ml': 2,
    # '435ml': 3,
    # '950ml': 4
    '160ML禾然有机酱油': 0,
    '500ML禾然有机酱油': 1,
    '190ML味达美清香米醋': 2,
    '460ML味达美清香米醋': 3,
    '160ML遵循自然原酿酱油': 4,
    '500ML遵循自然原酿酱油': 5,
    '190ML味达美臻品料酒': 6,
    '450ML味达美臻品料酒': 7,
    '230G味达美臻品蚝油': 8,
    '510G味达美臻品蚝油': 9,
    '160ML六月鲜柠檬蒸鱼酱油': 10,
    '380ML六月鲜柠檬蒸鱼酱油': 11
}

# colors=['blue','red','green','yellow','pink']

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

##########################################################
root = "/Users/fiona/Dataset/欣和/SKU大小/use/"

# only need to change these
##########################################################



annroot=root+'xml/'
picroot=root+'img/'
# annroot=root+'Annotations/'
# picroot=root+'JPEGImages/'
savepa_small = root +'small_pic/'           #生成保存的小图的文件夹
savepa_paint = root +'paint_pic/'
mkdir(savepa_small)
mkdir(savepa_paint)
anns = os.listdir(annroot)
imgs = os.listdir(picroot)


for ann in anns:
    if '.DS_Store' in ann:
        continue
    num=0
    annpath = annroot + ann
    picpath = picroot + ann.replace("xml", "jpg")
    savepath_paint = savepa_paint + ann.replace("xml", "jpg")

    if not os.path.exists(picpath):
        picpath = picpath.replace('jpg','jpeg')
        if not os.path.exists(picpath):
            continue
        # print (picpath)
    # im = Image.open(picpath)
    img = cv2.imread(picpath)
    print(picpath)
    print()
    showimg = img.copy()
    # draw = ImageDraw.Draw(im)
    DOMTree = xml.dom.minidom.parse(annpath)
    collection = DOMTree.documentElement
    objects = collection.getElementsByTagName("object")
    for object_ in objects:
        # print (object_)
        a = object_.getElementsByTagName("name")[0].childNodes[0].nodeValue
        k = a.split('.', 1)
        kk = k[0]
        cls_name = str(kk)
        # print (b)           #类别名称

        cls_name = filter_sku(cls_name)

        if cls_name is None:
            continue

        for key in predict_class_dict:                  #查字典
            if key in cls_name:
                ml = predict_class_dict[key]    #类别序号
                save_str = key   #类别名称
        # print(ml)
        savepath_small = savepa_small + str(ml)+ '_'+ save_str +"/"
        # savepath_small = savepa_small + "/"
        mkdir(savepath_small)

        # c='chepai'
        if 1:
            #    continue
            bndboxs = object_.getElementsByTagName("bndbox")
            for bndbox in bndboxs:
                num=num+1
                xmin = bndbox.getElementsByTagName('xmin')[0].childNodes[0].nodeValue
                ymin = bndbox.getElementsByTagName('ymin')[0].childNodes[0].nodeValue
                xmax = bndbox.getElementsByTagName('xmax')[0].childNodes[0].nodeValue
                ymax = bndbox.getElementsByTagName('ymax')[0].childNodes[0].nodeValue
                xtmp1 = xmin.split('.', 1)
                xmin1 = xtmp1[0]
                xtmp2 = xmax.split('.', 1)
                xmax1 = xtmp2[0]
                xtmp3 = ymin.split('.', 1)
                ymin1 = xtmp3[0]
                xtmp4 = ymax.split('.', 1)
                ymax1 = xtmp4[0]
            xmin = int(xmin1)
            ymin = int(ymin1)
            xmax = int(xmax1)
            ymax = int(ymax1)
            width=xmax-xmin
            height=ymax-ymin
            # xmin=xmin-width/4
            # xmax=xmax+width/4
            # ymin=ymin-height/2
            # ymin=int(ymin)
            # ymax=ymax+height/2
            if xmin < 0:
                xmin = 0
            if ymin < 0:
                ymin = 0
            sp = img.shape
            if xmax > sp[1]:
                xmax = sp[1]
            if ymax > sp[0]:
                ymax = sp[0]
            # draw.rectangle((xmin, ymin+height/2, xmax, ymax), outline=colors[ml])
            # img = cv2.cvtColor(np.asarray(draw), cv2.COLOR_RGB2BGR)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(showimg, (xmin, ymin), (xmax, ymax), (0, 255, 255), 5)
            cv2.putText(showimg, str(ml), (xmin, int((ymin+ymax)/2)), font, 1.7, (0, 255, 0), 4)
            # cv2.imshow('paint',showimg)
            # cv2.waitKey(0)
            roiimg=img[ymin: ymax, xmin:xmax]#[ymin: ymin+ (xmax-xmin), xmin:xmax]
            savepath_small = savepath_small+ str(num)+"_"+ann.replace('xml', 'jpg')
            # cv2.imshow('small',roiimg)
            # cv2.waitKey(0)
            cv2.imwrite(savepath_small,roiimg)
    cv2.imwrite(savepath_paint,showimg)
    # im.save(savepath_paint)