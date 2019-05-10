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


dadir="/mnt/sources2/data/2019/11/铭牌/2323/"
sadir="/mnt/sources2/data/2019/11/铭牌/2323/"
num=0
imglist=os.listdir(dadir)
for img in imglist:
    num=num+1
    #img_tmp=img.split('_',2)
  #  sa=sadir+img_tmp[0]+"/"
   # mkdir(sa)
    #new="u铭牌"+img_tmp[0]+"_"+str(num)+"_"+img_tmp[3]
       
    # new="u"+ ww + "_0106-"+ str(num)+"_"+nimg+".jpg"
  #  img1=img1.replace("_不合格","_※→←")
  #  img1=img.replace("_合格","_→←")
    #img1=img1.replace("_合格","_↑↓")
    #img1=img.replace("_未通过","_〓↑↓")
   # img1=img1.replace("_合格","_↑↓")
   # new=new.replace("cjh","车架号")
   # new=new.replace("fdj","发动机号")
   # new=new.replace("pl","排量")
   # new=new.replace("zzny","制造年月") 
   # new=new.replace("%","@")
    img1=img.replace("：",":")
       
  
    
   # str_1=img_tmp[2]
    #str_list=list(str_1)
    #str_list.insert(1,'.')
    #str_2="".join(str_list)
    #print str_2

    shutil.move(dadir+img, sadir+img1)