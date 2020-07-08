# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:19:07 2018

@author: guweixin
"""



c=0


import os
import shutil
    
  
for line in open("/mnt/sources2/train_data/lenet_chebiao/chebiao.txt"):
    line22=line.strip('\n')
    if ".jpg" in line:
        line=line22
        name=line.split("/",7)
        nam=name[6] 
        for line1 in open("/mnt/sources2/data/0918_cheliangleixing/orig.txt"):
            line1=line1.strip('\n')  
            if line1 in line:
                shutil.move(line,"/mnt/sources2/train_data/lenet_chebiao/3000/"+nam+"/"+line1)
        
        
        
        
        #if line1 in line:
         #   with open('/mnt/sources2/0915check/test_error.txt', 'a') as f:
          #      f.writelines(line+ '\n')
   # else:
      #  with open('/mnt/sources2/0915check/test_2.txt', 'a') as f:
    #        f.writelines(line+ '\n')
            

#for line1 in open("/mnt/sources2/data/0917_chebiaofenlei/11.txt"):
#
 #   line1 = line1.strip('\n')
    
  #  blank1=".jpg"
    
   # if blank1 in line1:
    #    c=c+1
   #else:
    #    with open('/mnt/sources2/data/0917_chebiaofenlei/111.txt', 'a') as f:
     #       f.writelines(line1+ '\n')