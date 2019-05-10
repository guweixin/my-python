# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:06:43 2018

@author: guweixin
"""

import os

import shutil

#da="/mnt/sources2/data/0917_tongyong_bxd/done_cp/"

#imglist=os.listdir(da)
#for img in imglist:
 #   datapath=da+img
  #  savepath="/mnt/sources2/data/0917_tongyong_bxd/9-号牌号码内容/苏"+img
   # shutil.move(datapath, savepath)
    
da="/mnt/sources2/data/0917_tongyong_bxd/9-号牌号码内容/"

imglist=os.listdir(da)
k=0
for img in imglist:
    k=k+1
    im=img.split('_',1)
    i=im[0]
    datapath=da+img
    
    savepath="/mnt/sources2/data/0917_tongyong_bxd/done_un/cp/"+str(k)+"_"+i+".jpg"
    shutil.move(datapath, savepath)