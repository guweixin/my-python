# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:15:48 2018

@author: guweixin
"""
import json
import os
import shutil

def sub(string,p,c):
    new = []
    for s in string:
        new.append(s)
    new[p] = c
    return ''.join(new)



srcdir="/mnt/sources2/data/1113_手写车牌/train/打印/冀/"
xml_savedir="/mnt/sources2/data/1113_手写车牌/train/打印/冀/"
imglist=os.listdir(srcdir)
num=0
nu=0
for img in imglist:
    num=num+1
    # print file
    imgpath=srcdir+img
    nodot=img.split(".jpg",1)
    ss=nodot[0].split("_",2)
    answer=ss[2]
    print("an:"+answer)
    
    answer=answer.replace("0","０")
    answer=answer.replace("1","１")
    answer=answer.replace("2","２")
    answer=answer.replace("3","３")
    answer=answer.replace("4","４")
    answer=answer.replace("5","５")
    answer=answer.replace("6","６")
    answer=answer.replace("7","７")
    answer=answer.replace("8","８")
    answer=answer.replace("9","９")
    answer=answer.replace("A","Ａ")
    answer=answer.replace("B","Ｂ")
    answer=answer.replace("C","Ｃ")
    answer=answer.replace("D","Ｄ")
    answer=answer.replace("E","Ｅ")
    answer=answer.replace("F","Ｆ")
    answer=answer.replace("G","Ｇ")
    answer=answer.replace("H","Ｈ")
    answer=answer.replace("I","Ｉ")
    answer=answer.replace("J","Ｊ")
    answer=answer.replace("K","Ｋ")
    answer=answer.replace("L","Ｌ")
    answer=answer.replace("M","Ｍ")
    answer=answer.replace("N","Ｎ")
    answer=answer.replace("O","Ｏ")
    answer=answer.replace("P","Ｐ")
    answer=answer.replace("Q","Ｑ")
    answer=answer.replace("R","Ｒ")
    answer=answer.replace("S","Ｓ")
    answer=answer.replace("T","Ｔ")
    answer=answer.replace("U","Ｕ")
    answer=answer.replace("V","Ｖ")
    answer=answer.replace("W","Ｗ")
    answer=answer.replace("X","Ｘ")
    answer=answer.replace("Y","Ｙ")
    answer=answer.replace("Z","Ｚ")
    answer=answer.replace("a","ａ")
    answer=answer.replace("b","ｂ")
    answer=answer.replace("c","ｃ")
    answer=answer.replace("d","ｄ")
    answer=answer.replace("e","ｅ")
    answer=answer.replace("f","ｆ")
    answer=answer.replace("g","ｇ")
    answer=answer.replace("h","ｈ")
    answer=answer.replace("i","ｉ")
    answer=answer.replace("j","ｊ")
    answer=answer.replace("k","ｋ")
    answer=answer.replace("l","ｌ")
    answer=answer.replace("m","ｍ")
    answer=answer.replace("n","ｎ")
    answer=answer.replace("o","ｏ")
    answer=answer.replace("p","ｐ")
    answer=answer.replace("q","ｑ")
    answer=answer.replace("r","ｒ")
    answer=answer.replace("s","ｓ")
    answer=answer.replace("t","ｔ")
    answer=answer.replace("u","ｕ")
    answer=answer.replace("v","ｖ")
    answer=answer.replace("w","ｗ")
    answer=answer.replace("x","ｘ")
    answer=answer.replace("y","ｙ")
    answer=answer.replace("z","ｚ")
                                       
    print "re:"+answer
    
    #answer=sub(answer,0,"F")
    
    
    
    img_name = ss[0]+"_"+ss[1]+"_冀"+answer+".jpg"
    
    shutil.move(imgpath, xml_savedir + img_name)
