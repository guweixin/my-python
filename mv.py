import os
import shutil


save="/mnt/sources2/train_data/big_obj/JPEGImages/"

for line in open("/mnt/sources2/data/2019/0301_tongyong/剔除的数据.txt"):
    line22=line.strip('\n')
    shutil.move(save+line22,"/mnt/sources2/train_data/big_obj/1/"+line22)
        
