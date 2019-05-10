import os
import shutil

save_path = "/home/guweixin/共享/0115_yhl/"
rootdir = '/mnt/sources2/train_data/lenet_chebiao/train/'

list = os.listdir(rootdir)
for i in range(0,len(list)):
    path = os.path.join(rootdir, list[i])
    print (path)
    print (os.path.isdir(path))
    if(os.path.isdir(path)):
        os.mkdir(save_path + list[i])
        list_sub = os.listdir(path)
        cnt = 0
        for j in range(0,len(list_sub)):
            path_pic = os.path.join(path, list_sub[j])
            shutil.copy(path_pic,save_path + list[i])
            cnt += 1
            if(cnt > 5):
                break



