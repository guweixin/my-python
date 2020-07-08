from xml.dom.minidom import parse
import xml.dom.minidom
import os,shutil
import numpy as np
import cv2
from PIL import Image, ImageDraw
##########################################################
root="/mnt/sources2/data/2019/0415_bigobj_xcjly/"
#only need to change these
##########################################################
#annroot=root+'0A/'
#picroot=root+'0J/'
annroot=root+'xml/'
picroot=root+'img/'
#annroot=root+'Annotations/'
#picroot=root+'JPEGImages/'
anns=os.listdir(annroot)
imgs=os.listdir(picroot)
for ann in anns:
    #print ann
    annpath=annroot+ann
    picpath=picroot+ann.replace("xml","jpg")
#    savepath = root+'Saveimg/'+"0821_"+ann.replace("xml","jpg")
    savepath = root+'check1/'+ann.replace("xml","jpg")
    #print (picpath)
    im = Image.open(picpath)
    img = cv2.imread(picpath)
    draw = ImageDraw.Draw(im)
    DOMTree = xml.dom.minidom.parse(annpath)
    collection = DOMTree.documentElement
    objects = collection.getElementsByTagName("object")
    for object_ in objects:
        #print (object_)
        a=object_.getElementsByTagName("name")[0].childNodes[0].nodeValue
    #    if a!="hebeichepai":
     #       print ann+"=========================="
        bndboxs = object_.getElementsByTagName("bndbox")
        for bndbox in bndboxs:
            xmin = bndbox.getElementsByTagName('xmin')[0].childNodes[0].nodeValue
            ymin = bndbox.getElementsByTagName('ymin')[0].childNodes[0].nodeValue
            xmax = bndbox.getElementsByTagName('xmax')[0].childNodes[0].nodeValue
            ymax = bndbox.getElementsByTagName('ymax')[0].childNodes[0].nodeValue
            xtmp1=xmin.split('.',1)
            xmin1=xtmp1[0]
            xtmp2= xmax.split('.', 1)
            xmax1 = xtmp2[0]
            xtmp3=ymin.split('.',1)
            ymin1=xtmp3[0]
            xtmp4=ymax.split('.',1)
            ymax1=xtmp4[0]

        xmin = int(xmin1)
        ymin = int(ymin1)
        xmax = int(xmax1)
        ymax = int(ymax1)
        
        #width=xmax-xmin
        #height=ymax-ymin
        #xmin=xmin-width/4
        #xmax=xmax+width/4
        #ymin=ymin-height/2
        #ymax=ymax+height/2
        if xmin<0:
            xmin=0
        if ymin<0:
            ymin=0
        sp=img.shape
        if xmax>sp[1]:
            xmax=sp[1]
        if ymax>sp[0]:
            ymax=sp[0]
        draw.rectangle((xmin, ymin, xmax, ymax), outline = "red")
        #roiimg=img[ymin: ymax, xmin:xmax]
        im.save(savepath)
        #cv2.imwrite(savepath,roiimg)
