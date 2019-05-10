# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:34:34 2018

@author: guweixin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 19:25:51 2018

@author: guweixin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:54:22 2017

@author: guweixin
"""



#!/usr/bin/env python

# -*- coding:utf-8 -*-

import os

labelDic={'b-0':0,'b-1':1,'f-0':2,'f-1':3}

rootdir="/mnt/sources/data/chejian/lenet_chedeng/"

fileList=os.listdir(rootdir)

for file in fileList:
    if file in labelDic:
        for fileName in os.listdir(os.path.join(rootdir,file)):
            path_tmp=os.path.join(rootdir,file)+'/'+fileName
            with open('/mnt/sources/data/chejian/lenet_chedeng/tt.txt', 'a') as f:
                f.writelines(path_tmp+" " + str(labelDic[file])+'\n')
            
    
    

    

        