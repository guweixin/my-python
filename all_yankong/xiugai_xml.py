import os  
import os.path  
import xml.dom.minidom  
from xml.dom.minidom import parse
import xml.dom.minidom
import os,shutil
import numpy as np
import cv2
from PIL import Image, ImageDraw

path="/mnt/sources2/data/0827_shenzhenbiaozhu/0/xml/"  

files=os.listdir(path)
s=[]  
k=0
for xmlFile in files:
    k=k+1
    print k
    print xmlFile
    if not os.path.isdir(xmlFile): 
        #print xmlFile  
        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
        root=dom.documentElement  
        objects = root.getElementsByTagName("object")
        for object_ in objects:
            a=object_.getElementsByTagName("name")[0].childNodes[0].nodeValue
            if a=="hb_biaoge":
                print xmlFile  
                name=object_.getElementsByTagName('name')
                n0=name[0]
                n0.firstChild.data='jianyanbaogao' 
               
            with open(os.path.join(path, xmlFile), 'w') as fh:
                dom.writexml(fh)
    #datapath=path+xmlFile
    #savepath="/mnt/sources2/train_data/ssd_wenbenkeymsg/Annotations/"+xmlFile       
    #shutil.move(datapath, savepath)