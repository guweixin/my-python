import os
import shutil

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:
		os.makedirs(path)
  
#num=0
#for linealll in open("./data_alll.txt"):
  #  num=num+1
  #  line1 = linealll.strip('\n')
   # line2 = line1.split('/',10)
    #if len(line2) is 11:
     #   with open('./data_all.txt', 'a') as f:
      #      f.writelines(line1 + '\n')

nu=0  
lastpp="start"
lastcs="start1"
sa= "/mnt/sources2/data/2019/tuomo_bidui/1_data/"
for line22 in open("./data_all.txt"):
    lineaa = line22.strip('\n')
    print lineaa
    linebb = lineaa.split('/',10)
    changshang= linebb[8]
    pinpai = linebb[9]
    imgname =linebb[10]
       
    if pinpai != lastpp or changshang != lastcs:
        lastpp = pinpai
        lastcs = changshang
        num = 0
    nu=nu+1
    print nu
    bili = nu%10
    
    if (bili< 7):
      #  print bili
        saa="data_train/"
        with open('./data_train.txt', 'a') as f:
            f.writelines(sa+saa+changshang+"/"+pinpai+"/"+imgname + '\n')
    else:
        saa="data_test/"
        with open('./data_test.txt', 'a') as f:
            f.writelines(sa+saa+changshang+"/"+pinpai+"/"+imgname + '\n')
            
    save_p=sa+saa+changshang+"/"+pinpai+"/"
    mkdir(save_p)  
    shutil.copy( lineaa , save_p+imgname )
    #print bili
    

        
        
        
    
  #  if len(line2) is 11:
   #     with open('./data_all.txt', 'a') as f:
    #        f.writelines(line1 + '\n')