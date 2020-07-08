# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 17:31:40 2018

@author: guweixin
"""

import os
import cv2
datadir="/mnt/sources2/data/1219_tongyong_shenzhou/need/long/"
savedir="/mnt/sources2/data/1219_tongyong_shenzhou/need/11/"
imglist=os.listdir(datadir)
for img in imglist:
    image = cv2.imread(datadir+img)  
    print image.shape
    col=image.shape[0]
    row=image.shape[1]
    print col 
    print row
    yb=row/2
    print yb
    cropImg = image[0:col, 0:yb] 
    cv2.imwrite(savedir+"1-"+img,cropImg) 
    cropImg = image[0:col, yb:row] 
    
    cv2.imwrite(savedir+"2-"+img,cropImg) 