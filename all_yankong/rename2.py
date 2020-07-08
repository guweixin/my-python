# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:56:32 2017

@author: guweixin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:27:14 2017

@author: guweixin
"""

import os

import shutil



datadir="/mnt/sources2/data/0905_tongyongold/old/1done/bxd_chechuanshui/"

savedir="/mnt/sources2/data/0905_tongyongold/done_un/ccs/"

imglist=os.listdir(datadir)
kk=1
for img in imglist:
    
    img_tmp=img.split('_',2)
    oldname=img_tmp[2]
  #  old=oldname.replace("@","≥")
  #  o=old.replace("#","@")
  #  img_=o.replace("!","≤")    
  #  img_ne=img_.replace("X","×")
  #  img_e=img_ne.replace("-","-")
  #  imme=img_e.replace("+","+")
  #  iame=imme.replace("(","（")
  #  img_name=iame.replace(")","）")       
    # ±
    old=oldname.replace("y","￥")
    ol=old.replace(";","：") 
    img_name=ol.replace("r","元") 
   
    datapath=datadir+img
    savepath=savedir+str(kk)+"_"+img_name
    kk=kk+1
    if os.path.exists(datapath):

        shutil.copy(datapath, savepath)
  