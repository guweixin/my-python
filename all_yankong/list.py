import os
import shutil

for line in open("./tmp.txt"):
    line1 = line.strip('\n')
    if "/img/" in line1:
         with open('./img.txt', 'a') as f:
             f.writelines(line1 + '\n')
         line2=line1.replace("/img/","/gray/")
         with open('./gray.txt', 'a') as f:
             f.writelines(line2 + '\n')     
