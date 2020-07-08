# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:54:22 2017

@author: guweixin
"""



#!/usr/bin/env python

# -*- coding:utf-8 -*-

import os



rootdir="/mnt/sources2/train_data/lenet_chebiao/train/"

labelList={}
num=0
cnt=0

for line in open("/mnt/sources2/train_data/lenet_chebiao/label_121.txt"):

    line = line.strip('\n')

    labelList[line]=cnt

    cnt=cnt+1



fileList=os.listdir(rootdir)

for file in fileList:
    #tmp=file.split('_',1)

    #if len(tmp)==1:

     #   continue

    #else:
    if not labelList.has_key(file):
        continue
    cnt_tmp=labelList[file]

    subdir=rootdir+file+"/"

    nameList=os.listdir(subdir)

    for name in nameList:
        num=num+1
        print num

        savepath=subdir+name#+" "+str(cnt_tmp)

        i=num%10        
        if i in range(0,8):
            with open('/mnt/sources2/train_data/lenet_chebiao/train.txt', 'a') as f:
                f.writelines(savepath + '\n')
        else:
            with open('/mnt/sources2/train_data/lenet_chebiao/val.txt', 'a') as f:
                f.writelines(savepath + '\n')