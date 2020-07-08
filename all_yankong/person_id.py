#coding: utf-8
from aip import AipOcr
import os
import json

APP_ID = "14310442"
API_KEY = "RhDWkPAPo26Xnhy2GZlKb4ma"
SECRET_KEY = "kzR1QbkWyfNGoqQkEoNMW19CMduHsiIO"

# save_path = "/home/niezhongliang/桌面/sfz/res"
# image_path =  "/home/niezhongliang/桌面/sfz/image"
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# files = os.listdir(image_path)
# files.sort()
# for f in files: 
#     name_path = os.path.join(image_path, f)
#     print name_path
#     image = get_file_content(name_path)
#     idCardSide = "front"
#     client.idcard(image, idCardSide)
#     options = {}
#     options["detect_direction"] = "true"
#     options["detect_risk"] = "true"

#     results = client.idcard(image, idCardSide, options)
#     json_save = os.path.join(save_path, f.rstrip(".jpg")+".json")    
#     # print json.dumps(results, ensure_ascii=False)
#     with open(json_save, "w+") as jp:
#         content = json.dumps(results,ensure_ascii=False)
#         jp.write(content.encode('utf-8'))

save_path = "/home/niezhongliang/桌面/xsz/res"
image_path =  "/home/niezhongliang/桌面/xsz/img"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

files = os.listdir(image_path)
files.sort()
for f in files: 
    name_path = os.path.join(image_path, f)
    print name_path
    image = get_file_content(name_path)
    # client.vehicleLicense(image)
    options = {}
    options["detect_direction"] = "true"

    results = client.vehicleLicense(image, options)
    json_save = os.path.join(save_path, f.rstrip(".png")+".json")    
    # print json.dumps(results, ensure_ascii=False)
    with open(json_save, "w+") as jp:
        content = json.dumps(results,ensure_ascii=False)
        jp.write(content.encode('utf-8'))