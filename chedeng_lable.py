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



for line in open("/mnt/sources2/data/2019/tuomo_bidui/6_xiaotuall/6.txt"):

    line = line.strip('\n')

    if ".jpg" in line:
        tmp=line.split('/',12)
        name= tmp[12]
        ntmp=name.split('_',2)
        num=ntmp[2]
        
        with open('/mnt/sources2/data/2019/tuomo_bidui/6_xiaotuall/a6.txt', 'a') as f:
            f.writelines(num + '\n')
   # labelList[line]=cnt

    #cnt=cnt+1



        

    #if len(tmp)==1:

     #   continue

    #else:

     #   if not labelList.has_key(file):
       #     continue
      #  cnt_tmp=labelList[file]

        #subdir=rootdir+file+"/"

        #nameList=os.listdir(subdir)

        #for name in nameList:

         #   savepath=subdir+name+" "+str(cnt_tmp)

          #  with open('/mnt/sources/data/chejian/lenet_chedeng/test.txt', 'a') as f:

           #     f.writelines(savepath + '\n')