# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:25:42 2018

@author: guweixin
"""
import os
import shutil
save="/mnt/sources2/train_data/lstm_tongyong/data_sqb/机动车所有人（代理人）签字：/"
for line in open("/mnt/sources2/train_data/lstm_tongyong/data_sqb/1.txt"):
    line=line.strip('\n')
    name=line.split("/",7)
    imgname=name[7]
    
    
    a=imgname.split("_",2)
    aaa=a[0]+"_"+a[1]+"：_"+a[2]
    print aaa
    shutil.move(line, save+aaa)