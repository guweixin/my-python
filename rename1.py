import os 
import shutil
import os.path as osp

path = "/work/01_project/00_datasets/big_obj/temp_xml"

for line in os.listdir(path):
	org = osp.join(path, line)
	new_line = line.rstrip('.jpg')
	tar = osp.join(path, new_line)
	shutil.move(org, tar)
# for line in os.listdir(path):
	# org = osp.join(path, line)
# new_line = line + '.jpg'
# print(new_line+'\n')
# tar = osp.join(path, new_line)
# shutil.move(org, tar)

