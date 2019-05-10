
import os
import shutil


datadir="/mnt/sources2/data/2019/tuomo_bidui/3_qingli/"
cslist=os.listdir(datadir)
for cs in cslist:
    csdir=datadir+cs+"/"
    pplist=os.listdir(csdir)
    pplist.sort()
    for pp in pplist:
        with open('./7zitibiao.txt', 'a') as f:
            f.writelines('\n'+cs+"/"+pp+" ")  
        ppdir=csdir+pp+"/"
        zflist=os.listdir(ppdir)
        zflist.sort()
        pre=""
        for zf in zflist:
            labeldir=ppdir+zf+"/"
            labellist=os.listdir(labeldir)
            labellist.sort()
            if "起止符1" in zf:
                pre = "star1_"
            if "起止符2" in zf:
                pre = "star2_"
            print(labellist)

            for i in range(0,len(labellist)-1):
                labellist[i]=labellist[i]+"/"
            for i in range(0,len(labellist)):
                labellist[i]=pre+labellist[i]
                
                
            with open('./7zitibiao.txt', 'a') as f:
                f.writelines(labellist)
                # f.writelines( ) 
                pre=""  
            with open('./7zitibiao.txt', 'a') as f:
                f.writelines(" ") 
















#def mkdir(path):
 #	folder = os.path.exists(path)
 #	if not folder:
#		os.makedirs(path) 
           
# for line in open("./test2/3_qingli.txt"):
#     line1 = line.strip('\n')
#     line2 = line1.split('/',11)
#     if len(line2) is 11:
#         with open('./test2/list.txt', 'a') as f:
#              f.writelines(line1 + '\n')
             
             
# last_cs="start"
# last_pp="yaya"
# last_zf="haha"
# last_la="enen"
# for line in open("./test2/list.txt"):
#     line3 = line.strip('\n')
#     line4 = line3.split('/',10)
#     cs=line4[7]
#     pp=line4[8]
#     zifu=line4[9]
#     label=line4[10]

# #    save_pa="/mnt/sources2/data/2019/tuomo_bidui/3_xiaotu_all/"+cs+"/"+new+"/"+zifu+"/"+label+"/"
#   #  mkdir(save_pa)
#    # save=save_pa+imgname
#     #shutil.copy(line3, save)

#     if cs != last_cs or pp != last_pp:
#         last_cs = cs
#         last_pp = pp
#         with open('./test2/zitibiao.txt', 'a') as f:
#             f.writelines('\n'+cs+"/"+pp+" ") 
#     print (zifu)
#     print (last_zf)
#     if zifu == last_zf :        
#         with open('./test2/zitibiao.txt', 'a') as f:
#             f.writelines("@")
    
#     if zifu != last_zf :        
#         last_zf = zifu            
#     if "起" in zifu :
#         label = "start_"+label
    
#     with open('./test2/zitibiao.txt', 'a') as f:
#         f.writelines(label+" ")

    

    
