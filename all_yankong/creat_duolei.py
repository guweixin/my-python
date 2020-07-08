
import os
import shutil


datadir="/mnt/sources2/data/2019/tuomo_bidui/7_0118_gkj/g/"
cslist=os.listdir(datadir)
cslist.sort()
for cs in cslist:
    csdir=datadir+cs+"/"
    pplist=os.listdir(csdir)
    pplist.sort()
    for pp in pplist:
        with open('./need.txt', 'a') as f:
            f.writelines('\n'+cs+"/"+pp+" "+'\n')  
        ppdir=csdir+pp+"/"
        zflist=os.listdir(ppdir)
        zflist.sort()
        pre=""
        for zf in zflist:
            labeldir=ppdir+zf+"/"
            labellist=os.listdir(labeldir)
            if "起止符1" in zf:
                pre = "star1_"
            if "起止符2" in zf:
                pre = "star2_"
            
            labellist.sort()
           # print(labellist)
            for i in range(0,len(labellist)-1):
                labellist[i]=labellist[i]+"/"
            for i in range(0,len(labellist)):
                labellist[i]=pre+labellist[i]
                
            if len(labellist) != 1:
                with open('./need.txt', 'a') as f:
                    f.writelines(labellist)
                with open('./need.txt', 'a') as f:
                    f.writelines('\n')
                # f.writelines( ) 
                pre=""  
           # with open('./need.txt', 'a') as f:
            #    f.writelines(" ")
