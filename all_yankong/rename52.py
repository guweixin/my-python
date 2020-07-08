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

ssss_dir="/mnt/sources2/data/1224_cjh/1/"
save_dir="/mnt/sources2/data/1224_cjh/new/"

ww="tuomo"

graydir=ssss_dir+ww+"/gray/"
imgdir =ssss_dir+ww+"/img/"
sa_graydir=save_dir+ww+"/gray/"
sa_imgdir =save_dir+ww+"/img/"
mkdir(sa_graydir)
mkdir(sa_imgdir)

#graydir="/mnt/sources2/train_data/se_chejiahao/1_arc/huxing/img/"
imlist=os.listdir(graydir)
num = 2546
for name in imlist:
    num=num+1
    new_name= "tm_"+str(num)+".png"
   
  #  name1=name.replace("hx_","hx")    
 #   shutil.move(graydir+name, graydir+name1)
    shutil.copy(graydir+name, sa_graydir + new_name)
    #name=name.replace("gray","img")
    shutil.copy(imgdir+name, sa_imgdir + new_name)
