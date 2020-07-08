import os
import shutil


datadir_img="/mnt/sources2/data/0912_tongyong_all/111/ma/"

savedir_img="/mnt/sources2/data/0912_tongyong_all/done/MA/"

imglist=os.listdir(datadir_img)
aa=0
for img in imglist:
    
 img_name=img
 #save_name='jby_jida_'+img_name
 name=img_name.split("_",2)
 aa=aa+1
 #save_name=name[0]+"_"+name[1]+"_"+name[2]+".jpg"
 save_name="MA"+str(aa)+"_MA.jpg"#name[2]
 datapath_img=datadir_img+img
 savepath_img=savedir_img+save_name #+".jpg"

 if os.path.exists(datapath_img):

  shutil.move(datapath_img, savepath_img)
  