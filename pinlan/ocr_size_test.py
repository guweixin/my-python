import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
image_pa = '/Users/fiona/Downloads/ocr_resize_test/test.jpg'
img = Image.open(image_pa).convert('L')
# print(img.shape)
h, w = img.size[1], img.size[0]
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_GRAY2BGR)

# img = cv2.resize(img, (280, 32), cv2.INTER_CUBIC)

img_padding = np.zeros((32, 280, 3), np.uint8)
# 使用白色填充图片区域,默认为黑色
img_padding.fill(255)
# cv2.imshow("img", img_padding)
# cv2.waitKey(0)
radio_net = float(280/32)
radio = w/h
print(radio)
if radio > radio_net:
    resized = cv2.resize(img, (280, int(280 / radio)), cv2.INTER_CUBIC)
    img_padding[:int(280 / radio), :] = resized
if radio < radio_net:
    resized = cv2.resize(img, (int(32 * radio), 32), cv2.INTER_CUBIC)
    img_padding[:, :int(32 * radio)] = resized
# img = cv2.resize(img, (280, 32), cv2.INTER_CUBIC)
img = Image.fromarray(cv2.cvtColor(img_padding, cv2.COLOR_BGR2GRAY))
print(img)
plt.imshow(img)  #image表示待处理的图像
plt.show()
# cv2.imshow("img", img)
# cv2.waitKey(0)
# if radio > radio_net:
#     resized = cv2.resize(img, (280, int(280/radio)), cv2.INTER_CUBIC)
#     img_padding[:int(280/radio), :] = resized
# if radio < radio_net:
#     resized = cv2.resize(img, (int(32*radio), 32), cv2.INTER_CUBIC)
#     img_padding [:,:int(32*radio)] = resized
#     cv2.imshow("img", img)
#     cv2.imshow("img", img_padding)
#     cv2.waitKey(0)

# start = int((h - w) / 2)
# imgnew[0:h, start: start + w] = img
# img1 = cv2.imread('/Users/fiona/Downloads/ocr_resize_test/test1.jpg')
# print(img1.shape)
#
# resized1 = cv2.resize(img1, (280, 32), cv2.INTER_CUBIC)
# cv2.imshow("img",img1)
# cv2.imshow("img",resized1)
# cv2.waitKey(0)