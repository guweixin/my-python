# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:46:24 2018

@author: guweixin
"""
import cv2

tongji=[33]
#for line in  open("/mnt/sources2/train_data/segnet_chejiahao/111.txt"):
for cc in range(0,2):
    #line = line.strip('\n')
    img=cv2.imread("/mnt/sources2/train_data/segnet_chejiahao/gray/ningbo_0904_1_nopass.png",0)
    print img.ndim
    #cv2.imshow("1", img)  
    #cv2.waitKey (0) 
    for row in range(0,100):#img.height):            #遍历高
        for col in range(0,100):#img.weight):         #遍历宽
                i=img[row,col]
                tongji[i]=tongji[i]+1
                print tongji
                print i
print tongji