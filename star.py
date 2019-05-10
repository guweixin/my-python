# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:37:40 2018

@author: guweixin
"""
import os
import shutil

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:
		os.makedirs(path)
  
num=0
for line in open("/mnt/sources2/data/2019/tuomo_bidui/list1.txt"):
    print(num)
    num=num+1
    img_pa = line.strip('\n')
    if "star" in img_pa:
        line1=img_pa.replace("1220_sz","1226_sz")
        line1=line1.replace("star","star_")
        
        k = line1.rfind("/")
        path=line1[:k]
      #  line1 = line1[:k] + "" + line1[k+1:]
        mkdir(path)
        #line1=line1.replace("_","")
        print line1
        shutil.copy(img_pa, line1)
        