
import os
import shutil

def mkdir(path):
 	folder = os.path.exists(path)
 	if not folder:
		os.makedirs(path)

datadir="/mnt/sources2/data/2019/tuomo_bidui/6_xiaotuall/right/"
savedir="/mnt/sources2/data/2019/0115_cjhhf_gkj/111/"

cslist=os.listdir(datadir)
for cs in cslist:
    csdir=datadir+cs+"/"
    pplist=os.listdir(csdir)
    for pp in pplist:
        ppdir=csdir+pp+"/"
        zflist=os.listdir(ppdir)
        for zf in zflist:
            labeldir=ppdir+zf+"/"
            labellist=os.listdir(labeldir)
            for label in labellist:
                savepath=savedir+label
                folder = os.path.exists(savepath)
            	if folder:
                     imgdir=labeldir+label+"/"
                     imglist=os.listdir(imgdir)
                     for img in imglist:
                         shutil.move(imgdir+img,savepath+"/"+img )
                    
