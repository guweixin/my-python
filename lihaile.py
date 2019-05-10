# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:43:07 2017

@author: guweixin
"""

import os

import shutil

for line in open("/mnt/sources/data/chejian/chejiahao_buchong/1.txt"):
    
 name = line.strip('\n')

 xmldir="/mnt/sources/data/chejian/chejiahao_buchong/Jsz-b_chejiahao=0/"

 xml_savedir="/mnt/sources/data/chejian/chejiahao_buchong/111/"

 xmlpath=xmldir+name+".png"
 
 if os.path.exists(xmlpath):

  shutil.move(xmlpath, xml_savedir +name+".png")