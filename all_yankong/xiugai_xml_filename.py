import os  
import os.path  
import xml.dom.minidom  
from xml.dom.minidom import parse
import xml.dom.minidom
import os,shutil
#import numpy as np
#import cv2
import urllib
from PIL import Image, ImageDraw

path="/mnt/sources2/data/0827_shenzhenbiaozhu/0/xm/"  
files=os.listdir(path)
s=[]  
for xmlFile in files:
    imgname=xmlFile.replace(".xml",".jpg")
    if not os.path.isdir(xmlFile): 
        print xmlFile 
        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
        root=dom.documentElement  
        #filename = root.getElementsByTagName("filename").childNodes[0].nodeValue
        #print (filename)
        
        filename1=root.getElementsByTagName('filename')
        n0=filename1[0]
        print n0.firstChild.data
        a=imgname
        #a='jby_jida_'+str(n0.firstChild.data)#urllib.urlopen(n0).read()
        n0.firstChild.data=a
        print n0.firstChild.data
                
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
