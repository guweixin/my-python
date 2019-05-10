# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:09:29 2018

@author: guweixin
"""

import os 

import shutil

rootdir="/mnt/sources1/waiguan/chebiao/"
savedir="/mnt/sources1/waiguan/chebiao2/"

fileList=os.listdir(rootdir)

for file in fileList:
    subdir=rootdir+file+"/"
     
    imglist=os.listdir(subdir)
    
    for img in imglist:
        
        name=img        
        tmp=img.split('_',1)
        yaya='0111'
        ya=tmp[0]
        #print ya
               
        if yaya==ya:
            rootpath=rootdir+file+"/"+name
            savepath=savedir+file+"/"+name
            shutil.copy(rootpath, savepath)