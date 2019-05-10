# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:46:00 2018

@author: guweixin
"""

c=0


import os
import shutil
data="/mnt/sources2/train_data/lstm_general/test/"
xxx_savedir="/mnt/sources2/data/2019/0124_ls_general_check/test/error/"
for line in open("/mnt/sources2/data/2019/0124_ls_general_check/test/no.txt"):
    
    line2=line.strip('\n')
    if ".jpg" in line2:
        nn=line2.split("/",8)
        imgname=nn[8]
        noj=imgname.split(".jpg",1)
        name=noj[0].split("_",2)
    
    
      #  wenjian=name[0].replace("u","")                         ##unsure
     #   datadir=data+"data_unsure/"+wenjian+"/"                 ##unsure

        datadir=data+nn[6]+"/"+nn[7]+"/"                ##guding
        imglist=os.listdir(datadir)
        for img in imglist:
            datapath=datadir+imgname
            xmlpath=xxx_savedir+imgname
            if os.path.exists(datapath):
                c=c+1
                print datapath
                shutil.move(datapath, xmlpath)
            
            print c