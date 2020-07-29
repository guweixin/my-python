import os
import shutil

datadir = "/Users/fiona/Dataset/海天/收货单/111/1/"
xmldir = "/Users/fiona/Dataset/海天/收货单/0_超市收货凭证测试/"

xml_savedir = "/Users/fiona/Dataset/海天/收货单/111/收货单-标注/"
# xxx_savedir="/mnt/sources2/data/1015/00/"
imglist = os.listdir(datadir)



for img in imglist:
    print(img)
    #img_name=img_tmp[0]+"_jianyan.jpg"#img_t[0]+"_"+img_t[1]+"_"+img_t[2]+"_"+img_t[3]+"_"+img_tmp[0]+".jpg"
    #print img_name
    #xml=img.replace(".png",".txt")
    datapath = datadir+img
    xmlpath = xmldir+img

    if not os.path.exists(xmlpath):
        #print "bucunzai "
        shutil.move(datapath, xml_savedir+img)#_name)
    #if not os.path.exists(xmlpath):
     #   shutil.move(datapath, xxx_savedir+img)#_name)