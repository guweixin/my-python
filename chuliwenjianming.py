# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:21:10 2018

@author: guweixin
"""

import os 

import shutil

srcdir="/mnt/sources/data/test/0123_luntai/"

imglist=os.listdir(srcdir)

for img in imglist:
    
    name=img
    new=name.replace(".jpg","")
    print new
    img_tmp=new.split('_',3)
    print img_tmp[3]
    img_tm=img_tmp[3].replace(".","")
    img_t=img_tm.replace("-","")
    img_=img_t.replace("A","")
    print img_
    srcpath=srcdir+img
    savedir="/mnt/sources/data/test/000/"
    print savedir
    if os.path.exists(srcpath):
        shutil.move(srcpath, savedir+img_tmp[0]+"_"+img_tmp[1]+"_"+img_tmp[2]+"_"+img_+".jpg")
    
    