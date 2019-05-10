# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:20:31 2018

@author: guweixin
"""

import os
import shutil
datadir="/mnt/sources2/data/0928baidu/buidu_AI/cp/res/"
filelist=os.listdir(datadir)
for file in filelist:
    
    datapath=datadir+file
    nn=file.split('.',1)
    savepath= datadir+nn[0]+".txt"
    shutil.move(datapath, savepath)