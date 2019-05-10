# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:37:42 2018

@author: guweixin
"""

import json as js
import io
import os
import shutil
import cv2

jsondir="/mnt/sources2/data/0827_ty_shenqingbiao/json/"
imgdir="/mnt/sources2/data/0827_ty_shenqingbiao/mark/"
savedir="/mnt/sources2/data/0827_ty_shenqingbiao/zz/"
jsons=os.listdir(jsondir)
imgs =os.listdir(imgdir)
s=0
for json in jsons:
    jsonpath=jsondir+json
    imgpath =imgdir +json.replace("jpg.json","jpg")
    img=cv2.imread(imgpath)
    with open(jsonpath, 'r') as f:
        datas=js.load(f)
        data=datas["objects"]
        num=len(data)
        s=s+num
        h_box=[]
        w_box=[]
        for i in range(0,num):
            i=i+1
            da=data[i-1]
            cnt=da["polygon"] 
            x=[]
            y=[]
            for k in range(0,len(cnt)):
                cn=cnt[k-1]
                x.append(cn[0])
                y.append(cn[1])
            xmin=min(x)
            xmax=max(x)
            ymin=min(y)
            ymax=max(y)
            b=(xmin+ymin+xmax+ymax)
            w=xmax-xmin
            h=ymax-ymin
            if cmp(w,h)==-1:
                h_savepa=savedir+"height/"
                hhh=[b,xmin,xmax,ymin,ymax]
                h_box.append(hhh)
                #print hhh
            if cmp(w,h)==1:
                w_savepa=savedir+"width/"
                www=[b,xmin,xmax,ymin,ymax]
                w_box.append(www)
        h_box.sort(reverse=False)
        w_box.sort(reverse=False)
       # print h_box
        
        
        for ih in range(0,len(h_box)):
            hh=h_box[ih-1]
            xmin=hh[1]
            xmax=hh[2]
            ymin=hh[3]
            ymax=hh[4]
            roiimg=img[ymin:ymax,xmin:xmax]
            if not os.path.exists(h_savepa):
                os.mkdir(h_savepa)    
            h_savepath=h_savepa+str(ih)+"/"
            if not os.path.exists(h_savepath):
                os.mkdir(h_savepath) 
            h_save=h_savepath+json.replace(".jpg.json","")+"_"+str(ih)+".jpg"
            #cv2.imwrite(h_save,roiimg)

        for iw in range(0,len(w_box)):
            ww=w_box[iw-1]
            xmin=ww[1]
            xmax=ww[2]
            ymin=ww[3]
            ymax=ww[4]            
            roiimg=img[ymin:ymax,xmin:xmax]
            if not os.path.exists(w_savepa):
                os.mkdir(w_savepa)    
            w_savepath=w_savepa+str(iw)+"/"
            if not os.path.exists(w_savepath):
                os.mkdir(w_savepath)                 
            w_save=w_savepath+json.replace(".jpg.json","")+"_"+str(iw)+".jpg"
            #cv2.imwrite(w_save,roiimg)
print s