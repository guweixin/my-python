import os
import shutil

root_dir = '/Users/fiona/Dataset/海天/收货单/收货单-标注_0723/test/'
img_datadir = root_dir + "mark/"
img_savedir = root_dir + "JPEGImages/"

xml_datadir = root_dir + "xml/"
xml_savedir = root_dir + "Annotations/"

imglist = os.listdir(img_datadir)
k = 0
for img in imglist:
 name = img
 k = k+1
 img_datapath = img_datadir + name
 xml_datapath = xml_datadir + name.replace("jpg", "xml")
 xml_datapath = xml_datapath.replace("png", "xml")
 img_save_name = 'haitian_shd_'+str(k)+".jpg"
 xml_save_name = 'haitian_shd_'+str(k)+".xml"
 img_savepath = img_savedir+img_save_name
 xml_savepath = xml_savedir+xml_save_name

 #if os.path.exists(img_datapath):
 shutil.copy(img_datapath, img_savepath)
  
 #if os.path.exists(xml_datapath):
 shutil.copy(xml_datapath, xml_savepath)  