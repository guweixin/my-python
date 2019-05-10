# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:49:20 2018

@author: guweixin
"""
import os 
import json
import io
import shutil


filepath="/home/guweixin/1/"
savepath="/home/guweixin/0/"
fileList=os.listdir(filepath)
l=0
k=0
i=0
for file in fileList:
    with io.open(filepath+file, encoding='utf-8') as f:
        line=f.readline()
        print str(line)
        a=str(line)
        line=a.split("}")    
        for i in range(0,len(line)):
            i=i+1            
            if "smallCar" in line[i-1]:
                k=k+1
                print k
            if "bigCar" in line[i-1]:
                l=l+1
                print l
        if (k!=7 or l!=1):
             shutil.move(filepath+file, savepath+file)
            