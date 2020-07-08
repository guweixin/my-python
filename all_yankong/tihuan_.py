# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:13:05 2018

@author: guweixin
"""

import os
import shutil
data="/mnt/sources2/train_data/lstm_tongyong_data_1/error/替换/1/"
xxx_save="/mnt/sources2/train_data/lstm_tongyong_data_1/error/替换/2/"
c=0
for wj in open("/mnt/sources2/train_data/lstm_tongyong_data_1/error/替换/1.txt"): 
    wjj=wj.strip('\n')
    for line in open("/mnt/sources2/train_data/lstm_tongyong_data_1/error/替换/all.txt"):
        line2=line.strip('\n')
        name=line2.split("_",2)
        c=c+1
        datadir=data+wjj+"/"
        xxx_savedir=xxx_save+wjj+"/"
        imglist=os.listdir(datadir)
        for img in imglist:
            datapath=datadir+line2+".jpg"
            xmlpath=xxx_savedir+name[0]+"_"+name[1]+"_"+wjj+".jpg"
            if os.path.exists(datapath):
                shutil.move(datapath, xmlpath)          
    print c