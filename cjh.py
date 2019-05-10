# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:26:05 2018

@author: guweixin
"""
for line in open("/home/guweixin/0.txt"):
    line2=line.strip('\n')
    name=line2.split("_",2)
    if len(name[1]) is 17:
        with open('/mnt/sources2/data/1122_xsz_fenlei/cjh.txt', 'a') as f:
            f.writelines(name[1] + '\n')

for line in open("/mnt/sources2/data/1122_xsz_fenlei/cjh.txt"):
    line2=line.strip('\n')
    la="/mnt/sources2/111/"+line2+".txt"
    with open(la, 'a') as f:
        f.writelines("1")