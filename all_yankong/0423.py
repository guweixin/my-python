# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:15:16 2019

@author: em
"""

import os
import shutil

datadir="/data_2/train_data/ssd_big_obj/Annotations/"
imglist=os.listdir(datadir)

for line in open("/data_2/train_data/ssd_big_obj/ImageSets/Main/0423/trainval.txt"):
    line = line.strip('\n')
    datapath=datadir+line+".xml"
    if os.path.exists(datapath):
        with open('/data_2/train_data/ssd_big_obj/ImageSets/Main/0423/train11.txt', 'a') as f:
            f.writelines(line+ '\n')