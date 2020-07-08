import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import cv2
import glob
import shutil
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

images = glob.glob(
    os.path.join(
        "../data/",         #测试数据目录
        "image_padding/", "*.png",
    )
)

def image_padding(img, target_size):
    """
    功能：将图片按照原图比例进行缩放至目标尺寸
    Args:
        img: 需要进行缩放的图片，应为BGR格式。
        target_size: 目标尺寸，(height,width)
    Returns:
        {res_img} 缩放后的图片，BGR格式。
    """
    h, w, _ = img.shape
    resize_h, resize_w = target_size
    if h != resize_h or w != resize_w:
        # 使用黑色填充图片区域
        img_padding = np.zeros((resize_h, resize_w, 3), np.uint8)
        img_padding.fill(0)
        resize_ratio = float(resize_w / resize_h)
        ratio = w / h

        if ratio >= resize_ratio:
            # 对图片上下进行padding
            resize_h_new = int(np.ceil(resize_w / ratio))
            if resize_h_new == 0:
                resize_h_new = 1
            resized = cv2.resize(img, (resize_w, resize_h_new), cv2.INTER_CUBIC)
            start_h = (resize_h - resize_h_new) // 2
            img_padding[start_h:start_h+resize_h_new, :] = resized
            res_img = img_padding.copy()

        else:
            # 对图片左右进行padding
            resize_w_new = int(np.ceil(resize_h * ratio))
            if resize_w_new == 0:
                resize_w_new = 1
            resized = cv2.resize(img, (resize_w_new, resize_h), cv2.INTER_CUBIC)
            start_w = (resize_w - resize_w_new) // 2
            img_padding[:, start_w:start_w+resize_w_new] = resized
            res_img = img_padding.copy()
    else:
        # 图片为目标尺寸，无需缩放
        res_img = img.copy()
    return res_img

for image_path in images:
    img = Image.open(image_path)
    showimg = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    h, w, d = showimg.shape
    print('-'*100)
    target_size = (224, 224)

    newimg = image_padding(showimg, target_size)
    hh, ww, dd = newimg.shape

    print('height:    ' + str(h), '\tweight:    ' + str(w))
    print('new-height:' + str(hh), '\tnew-weight:' + str(ww))
    cv2.imshow('src', showimg)
    cv2.imshow('new', newimg)
    cv2.waitKey(0)
