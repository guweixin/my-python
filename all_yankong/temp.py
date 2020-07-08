#!/usr/bin/env python

# -*- coding:utf-8 -*-

import os



rootdir="/mnt/sources/gkj/"

labelList={}

cnt=0

for line in open("/mnt/sources/gkj/z_label/123.txt"):

    line = line.strip('\n')

    labelList[line]=cnt
    
    savepath1=line+" "+str(cnt)
    with open('/mnt/sources/gkj/z_label/t.txt', 'a') as f:
        f.writelines(savepath1 + '\n')
    
    
    cnt=cnt+1
    
print labelList



fileList=os.listdir(rootdir)

for file in fileList:

    tmp=file.split('_',1)

    if len(tmp)==1:

        continue

    else:

        cnt_tmp=labelList[file]

        subdir=rootdir+file+"/"

        nameList=os.listdir(subdir)

        for name in nameList:

            savepath=subdir+name+" "+str(cnt_tmp)

            with open('/mnt/sources/gkj/z_label/test.txt', 'a') as f:

                f.writelines(savepath + '\n')











