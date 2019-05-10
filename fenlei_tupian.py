# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:09:29 2018

@author: guweixin
"""

import os 

import shutil

rootdir="/mnt/sources2/data/0827_ty_shenqingbiao/11/"
savedir="/mnt/sources2/data/0827_ty_shenqingbiao/fenlei/"

fileList=os.listdir(rootdir)

#for file in fileList:
#    subdir=rootdir+file+"/"
    
imglist=os.listdir(rootdir)
    
for img in imglist:
        
    name=img
    tmp=img.split('_',2)
    tm=tmp[2].split('.',1)
    wenjianjia=tm[0]
    print wenjianjia
    rootpath=rootdir+name
    if os.path.exists(rootpath):
            #print "lalala"
            
        sav=savedir+wenjianjia+"/"+name
        if not os.path.exists(savedir+wenjianjia):
            os.mkdir(savedir+wenjianjia) 
        shutil.move(rootpath, sav)
        