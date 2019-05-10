import os
import shutil

def mkdir(path):
      folder = os.path.exists(path)
      if not folder:
           os.makedirs(path)

datadir="/mnt/sources2/data/2019/tuomo_bidui/2_xiaotu_all/"
savedir="/mnt/sources2/data/2019/tuomo_bidui/5_star/data/"
cslist=os.listdir(datadir)
for cs in cslist:
      csdir=datadir+cs+"/"
      pplist=os.listdir(csdir)
      for pp in pplist:
           ppdir=csdir+pp+"/"
           zflist=os.listdir(ppdir)
           for zf in zflist:
	           if "起止符" in zf:
            	 #if "起止符1" in zf:
                  #   pre = "zstar1"
            	 #if "起止符2" in zf:
                  #   pre = "zstar2"
            	      labeldir=ppdir+zf+"/"
            	      labellist=os.listdir(labeldir)
            	      for label in labellist:
                            savepath=savedir+cs+"/"+pp+"/"+zf+"/"+label+"/"
                            mkdir(savepath)
                            imgdir=labeldir+label+"/"
                            imglist=os.listdir(imgdir)
                            for img in imglist:
                                 shutil.copy(imgdir+img,savepath+img )
