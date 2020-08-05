# -*- coding:utf-8 -*-
import os
rootdir="/Users/fiona/Project/pinlan-weiquan-dataset/size训练集/train/"

labelList={}
num=0
cnt=0

for line in open("/Users/fiona/Project/pinlan-weiquan-dataset/size训练集/label.txt"):
    line = line.strip('\n')
    labelList[line]=cnt
    cnt=cnt+1

fileList=os.listdir(rootdir)
for file in fileList:
    # if not labelList.has_key(file):
    #     continue
    cnt_tmp=labelList[file]
    subdir=rootdir+file+"/"
    nameList=os.listdir(subdir)

    for name in nameList:
        num=num+1
        print (num)
        savepath=subdir+name+" "+str(cnt_tmp)

        # i=num%10
        # if i in range(0,8):
        with open('/Users/fiona/Project/pinlan-weiquan-dataset/size训练集/train.txt', 'a') as f:
            f.writelines(savepath + '\n')
        # else:
        #     with open('/mnt/sources2/train_data/lenet_chebiao/val.txt', 'a') as f:
        #         f.writelines(savepath + '\n')