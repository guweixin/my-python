import cv2
import numpy as np
import shutil
img = cv2.imread("./5.jpg")
cv2.namedWindow("original",0)
cv2.imshow("original", img)


rows,cols = img.shape[0:2]

for line in open("./5.txt","r"):
    line = split("::postion,",1)
    
    
