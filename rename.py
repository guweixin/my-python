# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:03:40 2017

@author: guweixin
"""

import os

import shutil

labelList={}

cnt=0

savedir="/mnt/sources2/data/0730_mingpai/lstm/cjh/"

for line in open("/mnt/sources2/data/0730_mingpai/lstm/4.txt"):

    line = line.strip('\n')

    labelList[line]=cnt

    cnt=cnt+1
    
    cntt=str(cnt)
    
    new_name="luntai_char_0205_"+cntt

    oldpath=line

   #if os.path.exists(oldpath):

    shutil.copy(oldpath, savedir + new_name+".xml")