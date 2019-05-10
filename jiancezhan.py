# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:38:04 2018

@author: guweixin
"""

import os 
import shutil

rootdir = "/mnt/sources2/zhidong_try/11/"
savedir = "/mnt/sources2/zhidong_try/all/"
imglist = os.listdir(rootdir)
for img in imglist:
     
    img_tmp=img.split('=',2)

    print img_tmp[0] +"_"+ img_tmp[1] +"_"+ img_tmp[2]   
    #img_name = img_tmp[1]
    img_name = img_tmp[0] +"_"+ img_tmp[1] +"_"+ img_tmp[2] 
    #print img_name
    
    xmlpath=rootdir+img
    
    if os.path.exists(xmlpath):

        shutil.move(xmlpath, savedir + img_name)