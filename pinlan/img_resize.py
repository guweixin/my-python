import os
import shutil
from PIL import Image
import cv2
import numpy as np

imgdir ='/data/Dataset/ocr/rec_data/english/'
imgdir_save ='./data/'

images = os.listdir(imgdir)
print(len(images))
num = 0
max_len=35
for image in images:
    img_path = imgdir +image
    imgsave_path = imgdir_save +image
    image=image.replace('.jpg','')
    if len(image)>= max_len:
        print('11')
        # max_len=len(image)
    else:
        shutil.move(img_path,imgsave_path)

    num = num + 1
    # img_path = imgdir +image
    # imgsave_path = imgdir_save +image.replace('newtrain','')
    # img = Image.open(img_path).convert('L')
    # width, height = img.size[0], img.size[1]
    #
    # if width == 280 and height == 32:
    #     shutil.move(img_path,imgsave_path)
    # else:
    # # # # 此处为将图片按原比例进行压缩补白
    #     img = cv2.cvtColor(np.asarray(img), cv2.COLOR_GRAY2BGR)
    #     img_padding = np.zeros((32, 280, 3), np.uint8)
    #     img_padding.fill(255)
    #     radio_net = float(280 / 32)
    #     radio = width / height
    #     if radio > radio_net:
    #         resized = cv2.resize(img, (280, int(280 / radio)), cv2.INTER_CUBIC)
    #         img_padding[:int(280 / radio), :] = resized
    #     if radio < radio_net:
    #         resized = cv2.resize(img, (int(32 * radio), 32), cv2.INTER_CUBIC)
    #         img_padding[:, :int(32 * radio)] = resized
    #     cv2.imwrite(imgsave_path, img_padding)
    #
    if num % 1000 == 0:
        print(num)
print('max_len:',max_len)