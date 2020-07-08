#!/usr/bin/env python

# -*- coding:utf-8 -*-

import os
import shutil
rootdir="/mnt/sources/data/chejian/jianzhaopian/77/"
dstDir="/mnt/sources/data/chejian/jianzhaopian/7/"
fileList=os.listdir(rootdir)

cnt=0

for file in fileList:

        
        srcImg=rootdir+file
        dstImg=dstDir+file+'.jpg'
        shutil.copy(srcImg,dstImg)

