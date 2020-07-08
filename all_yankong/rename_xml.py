import os
import shutil


datadir="/mnt/sources2/data/0827_shenzhenbiaozhu/0/xml/"

savedir="/mnt/sources2/data/0827_shenzhenbiaozhu/0/xm/"

filelist=os.listdir(datadir)

for file in filelist:
    
 img_name=file
 
 name=img_name.split('__',1)
 
 #print file
 save_name=name[0]+"_"+name[1]#'jybg_shenzhen_'+name[3]#[1]
 datapath=datadir+img_name
 savepath=savedir+save_name#+".xml"

 if os.path.exists(datapath):
  shutil.move(datapath, savepath)