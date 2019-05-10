import os
import cv2
import shutil

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)

num=0
right=0

img_width  = 512
img_height = 128
img_channel= 3
jvzhen = img_width * img_height * img_channel

for line in open("./1.txt"):
    img_pa = line.strip('\n')
    if ".png" in img_pa:
	num=num+1
	print  "all_img: "+str(num)
	img = cv2.imread(img_pa)
	if img.size != jvzhen:
	    with open('./error.txt', 'a') as f:
                f.writelines(line)
	else:
	    right=right+1
	    print "right  : "+str(right)
	print "-----------------------------"
