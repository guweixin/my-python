# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:12:31 2017

@author: guweixin
"""



#!/usr/bin/env python

# -*- coding:utf-8 -*-



import os

import shutil




datadir="/mnt/sources2/train_data/ssd_NatureText/img_test/"

xmldir="/mnt/sources2/train_data/ssd_NatureText/xml_test/"

xml_savedir="/mnt/sources2/train_data/ssd_NatureText/1/"

imglist=os.listdir(datadir)



for img in imglist:

    img_tmp=img.split('.',1)

    img_name=img_tmp[0]

    print img_name

    xmlpath=xmldir+img_name+".xml"

    if os.path.exists(xmlpath):

        shutil.move(xmlpath, xml_savedir + img_name+".xml")

