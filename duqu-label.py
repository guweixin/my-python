# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:09:28 2017

@author: guweixin
"""

cnt=0
for line in open("/mnt/sources/gkj/123.txt"):  
    line = line.strip('\n')
    with open('/mnt/sources/gkj/label.txt', 'a') as f:
        f.writelines(line+" "+str(cnt)+"\n")
    cnt=cnt+1
