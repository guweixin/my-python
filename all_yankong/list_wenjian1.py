# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:46:00 2018

@author: guweixin
"""

c=0


import os
import shutil
data="/mnt/sources2/train_data/lstm_tongyong/test/"
xxx_savedir="/mnt/sources2/data/1108_tongyong/delete/te_w/"

  
  
for line in open("/mnt/sources2/data/1108_tongyong/delete/teu.txt"):
    line2=line.strip('\n')
    name=line2.split("_",2)
    c=c+1
    
    
    wenjian=name[0].replace("u","")                         ##unsure
    datadir=data+"data_unsure/"+wenjian+"/"                 ##unsure
    #   datadir=data+"data_"+name[0]+"/"+name[2]+"/"        ##guding
    imglist=os.listdir(datadir)
    for img in imglist:
        datapath=datadir+line2+".jpg"
        xmlpath=xxx_savedir+line2+".jpg"
        if os.path.exists(datapath):
            shutil.move(datapath, xmlpath)
            
    print c