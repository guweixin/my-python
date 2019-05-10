# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:11:20 2018

@author: guweixin
"""
import os
import shutil

#sa="/mnt/sources2/data/0918_cheliangleixing/111聂/hkuang/大众/"
for line in open("/mnt/sources2/train_data/lstm_tongyong/train.txt"):
    line = line.strip('\n') 
    with open('/mnt/sources2/train_data/lstm_tongyong/train_.txt', 'a') as f:
        f.writelines(line +' 7117 7117 7117 7117 7117'+'\n')