#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xml.dom.minidom
import json
import os
import collections
def xml2json(xmlFile,savePath):
    if not os.path.getsize(xmlFile):
        print xmlFile
        return
    nameList=xmlFile.split('/',xmlFile.count('/'))
    fileName=nameList[-1].strip('.xml')

    dom=xml.dom.minidom.parse(xmlFile)
    root=dom.documentElement
    objects=root.getElementsByTagName("object")

    objectDic={}
    objectList=[]
    for object_ in objects:
        labelDic=collections.OrderedDict()
        rectList=[]
        subnode1=object_.getElementsByTagName("name")
        subnode2=object_.getElementsByTagName("bndbox")

        label=subnode1[0].childNodes[0].nodeValue
        # labelDic['label']=label
        #print (label)

        xmin=subnode2[0].getElementsByTagName("xmin")
        xmax=subnode2[0].getElementsByTagName("xmax")
        ymin=subnode2[0].getElementsByTagName("ymin")
        ymax=subnode2[0].getElementsByTagName("ymax")


        x1=int(xmin[0].childNodes[0].nodeValue)
        y1=int(ymin[0].childNodes[0].nodeValue)
        x2=int(xmax[0].childNodes[0].nodeValue)
        y2=int(ymax[0].childNodes[0].nodeValue)
        recWidth=x2-x1
        recHeight=y2-y1
        rectList.extend([x1,y1,recWidth,recHeight])
        labelDic['label'] = label
        labelDic['rect']=rectList

        #sorted(labelDic.keys())

        objectList.extend([labelDic])
    objectDic['objects']=objectList
    with open(savePath+fileName+".jpg.json",'w') as f:
        json.dump(objectDic,f,separators=(',',':'))
        # print xmin[0].childNodes[0].nodeValue
        # print xmax[0].childNodes[0].nodeValue
        # print ymin[0].childNodes[0].nodeValue
        # print ymax[0].childNodes[0].nodeValue


xmldir="/data_1/data/huanbaodan/0814/nanning_hbd/xml/"
xmlList=os.listdir(xmldir)
savepath="/data_1/data/huanbaodan/0814/nanning_hbd/json1/"
for xmlSingle in xmlList:
    xml2json(xmldir+xmlSingle,savepath)

