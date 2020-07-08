# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:05:09 2018

@author: guweixin
"""

import os
import shutil

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:
		os.makedirs(path)

file_pa = "/mnt/sources2/data/1219_tongyong_shenzhou/xsqy_lstm_tongyong/"
save_pa = "/mnt/sources2/data/1222_tongyong_ssqy/fenlei/"
imglist=os.listdir(file_pa)
for img in imglist:
    img_tmp=img.split('_',3)
    ssqy=img_tmp[2]
    mkdir(save_pa+ssqy)    
    
    shutil.move(file_pa+img, save_pa+ssqy+"/" + img)
    
    