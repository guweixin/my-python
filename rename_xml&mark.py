import os
import shutil


img_datadir="/mnt/sources2/train_data/ssd_wenbenkeymsg/shuju/0813_cpcjh/mark/"
img_savedir="/mnt/sources2/train_data/ssd_wenbenkeymsg/shuju/0813_cpcjh/JPEGImages/"

xml_datadir="/mnt/sources2/train_data/ssd_wenbenkeymsg/shuju/0813_cpcjh/xml/"
xml_savedir="/mnt/sources2/train_data/ssd_wenbenkeymsg/shuju/0813_cpcjh/Annotations/"

imglist=os.listdir(img_datadir)
k=0
for img in imglist:
 name=img
 k=k+1
 img_datapath=img_datadir+name
 xml_datapath=xml_datadir+name.replace("jpg","xml")
 img_save_name='jybg_qinghai_'+str(k)+".jpg"
 xml_save_name='jybg_qinghai_'+str(k)+".xml"
 img_savepath=img_savedir+img_save_name 
 xml_savepath=xml_savedir+xml_save_name 

 #if os.path.exists(img_datapath):
 shutil.copy(img_datapath, img_savepath)
  
 #if os.path.exists(xml_datapath):
 shutil.copy(xml_datapath, xml_savepath)  