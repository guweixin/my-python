# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:17:17 2019

@author: guweixin
"""

import os
import shutil

imgdir="/mnt/sources2/data/2019/0114_tongyong_不合格/未通过/"
savedir="/mnt/sources2/data/2019/0114_tongyong_不合格/11/未通过/"
imglist=os.listdir(imgdir)
num=0
for img in imglist:
    num=num+1
    new="u手写未通过_0114-"+str(num)+"_〓↑↓.jpg"
    shutil.copy(imgdir+img, savedir+new)