import os
import shutil


rootdir = '/Users/fiona/Dataset/Airliquide/air_rec/crop_img/'
fileList = os.listdir(rootdir)

for file in fileList:
    file_path = rootdir + file
    label = file.split('_')[-1].replace('.jpg', '')
    with open(rootdir+'gt.txt', 'a') as f:
        f.writelines(file_path + '\t' + label + '\n')