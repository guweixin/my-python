# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:44:38 2018

@author: guweixin
"""

import os
import shutil

srcdir="/mnt/sources2/0424/zzl&lbgd/"
savedir="/mnt/sources2/0424/save/"

imglist=os.listdir(srcdir)

for line in open("/mnt/sources2/0424/zongzhiliang.txt"):

    img_newname = line.strip('\n')
    
    imgf=img_newname.split('_',3)
    
    img_name=imgf[0]+"_"+imgf[1]+"_"+imgf[2]+".jpg"
    
    srcpath=srcdir+img_name
    savepath=savedir+img_newname+".jpg"

    if os.path.exists(srcpath):

       shutil.copy(srcpath, savepath)