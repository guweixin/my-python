# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:09:29 2018

@author: guweixin
"""

import os 

import shutil

rootdir="/mnt/sources2/data/0726/ol/"
savedir="/mnt/sources2/data/0726/00/"

fileList=os.listdir(rootdir)

for file in fileList:
    subdir=rootdir+file+"/"
    
    imglist=os.listdir(subdir)
    
    for img in imglist:
        
        name=img        
        #print name
        tmp=img.split('_',2)
     #   tm=tmp[2].split('.',1)
        wenjianjia=tmp[0]
        print (wenjianjia)
        
        rootpath=rootdir+file+"/"+name
        
        #print rootpath
                
        if os.path.exists(rootpath):
            #print "lalala"
            
            sav=savedir+wenjianjia+"/"+name
            if not os.path.exists(savedir+wenjianjia):
                os.mkdir(savedir+wenjianjia)                        
            #print sav
            shutil.move(rootpath, sav)
        