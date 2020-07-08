import os 
import shutil 

with open("/work/01_project/00_datasets/big_obj/remove1.txt") as f: 
    images = f.readlines()

path1 = "/work/01_project/00_datasets/big_obj/Annotations"
path2 = "/work/01_project/00_datasets/big_obj/JPEGImages"
path3 = "/work/01_project/00_datasets/big_obj/dump1"

for image in images: 
    src_img = os.path.join(path2, image.strip()+".jpg")
    src_ann = os.path.join(path1, image.strip()+".xml")

    dst_img = os.path.join(path3, image.strip()+".jpg")
    dst_ann = os.path.join(path3, image.strip()+".xml")

    if os.path.isfile(src_img):
        shutil.move(src_img, dst_img)
    if os.path.isfile(src_ann):
        shutil.move(src_ann, dst_ann)
