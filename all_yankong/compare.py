# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:48:17 2017

@author: guweixin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:12:31 2017

@author: guweixin
"""



#!/usr/bin/env python

# -*- coding:utf-8 -*-



import os

import shutil



odir="/mnt/sources/data/wuhan/new/"

pdir="/mnt/sources/data/wuhan/0203/"

qdir="/mnt/sources/data/wuhan/33/"


imglist=os.listdir(pdir)

for img in imglist:

    img_tmp=img.split('_',2)

    img_name=img_tmp[2]
    
    ppath=pdir+img_tmp[0]+"_"+img_tmp[1]+"_"+img_tmp[2]
    
    opath=odir+img_name+".jpg"
    
    if os.path.exists(opath):

        shutil.move(ppath, qdir+img_tmp[0]+"_"+img_tmp[1]+"_"+img_tmp[2]+".jpg")

