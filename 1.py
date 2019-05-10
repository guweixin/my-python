# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:27:14 2017
@author: guweixin
"""

import os
import shutil

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

alldir="/mnt/sources2/data/2018/1222_tongyong_ssqy/fenlei/"
sjbdir ="/mnt/sources2/data/2018/1222_tongyong_ssqy/shujubu/"
savedir="/mnt/sources2/data/2018/1222_tongyong_ssqy/banjie/"

wenlist=os.listdir(sjbdir)
for wen in wenlist:
    wen1=wen.replace("√","")
    imglist=os.listdir(sjbdir+wen+"/")
    print wen
    for img in imglist:
        xmlpath=alldir+wen1+"/"
        print xmlpath
        if os.path.exists(xmlpath):
            mkdir(savedir+wen1+"/")
            shutil.move(xmlpath+img, savedir+wen1+"/" + img)
