# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:50:19 2018

@author: guweixin
"""
wenjian=["/≥60.jpg/","/@-.jpg/","/@-@-@.jpg/","/@-@-@-.jpg/","/0.1.jpg/","/0.2.jpg/","/0.2m@km.jpg/","/0.3.jpg/","/0.4.jpg/",
"/0.4m@km.jpg/","/0.5m@km.jpg/","/0.6.jpg/","/0.7.jpg/","/0.8.jpg/","/0.9.jpg/","/1.0.jpg/","/1.0m@km.jpg/","/1.1.jpg/",
"/1.2m@km.jpg/","/1.3.jpg/","/1.5.jpg/","/1.6.jpg/","/1.6m@km.jpg/","/1.7.jpg/","/1.8.jpg/","/1.8m@km.jpg/","/1.jpg/",
"/2.3.jpg/","/2.9m@km.jpg/","/3.1.jpg/","/3.7m@km.jpg/","/4.7.jpg/","/5.0~5.0.jpg/","/5.0~5.0（m@km）.jpg/","/5.0~5.0m@km.jpg/",
"/5.0~+5.0.jpg/","/5.0m@km.jpg/","/5.0m@km~5.0m@km.jpg/","/5.0m@km~+5.0m@km.jpg/","/5.1~5.0m@km.jpg/","/5~+5.jpg/",
"/5~+6.jpg/","/5m@km~+5m@km.jpg/","/20.jpg/","/50~300.jpg/","/50~~300.jpg/","/50~-300.jpg/","/58.jpg/","/60.jpg/","/75.jpg/",
"/80.jpg/","/81.jpg/","/84.jpg/","/86.jpg/","/89.jpg/","/91.jpg/","/93.jpg/","/95.jpg/","/96.jpg/","/100~350.jpg/","/100~-350.jpg/",
"/102.jpg/","/103.jpg/","/104.jpg/","/106.jpg/","/109.jpg/","/111.jpg/","/112.jpg/","/113.jpg/","/114.jpg/","/115.jpg/","/116.jpg/",
"/123.jpg/","/124.jpg/","/125.jpg/","/126.jpg/","/127.jpg/","/129.jpg/","/131.jpg/","/132.jpg/","/135.jpg/","/142.jpg/","/143.jpg/","/149.jpg/",
"/150.jpg/","/152.jpg/","/154.jpg/","/158.jpg/","/160.jpg/","/161.jpg/","/164.jpg/","/165.jpg/","/166.jpg/","/168.jpg/","/169.jpg/","/171.jpg/",
"/173.jpg/","/175.jpg/","/177.jpg/","/178.jpg/","/179.jpg/","/180.jpg/","/184.jpg/","/185.jpg/","/189.jpg/","/190.jpg/","/192.jpg/","/193.jpg/",
"/194.jpg/","/196.jpg/","/199.jpg/","/201.jpg/","/202.jpg/","/206.jpg/","/208.jpg/","/211.jpg/","/212.jpg/","/214.jpg/","/216.jpg/","/218.jpg/","/219.jpg/",
"/220.jpg/","/221.jpg/","/222.jpg/","/224.jpg/","/226.jpg/","/228.jpg/","/230.jpg/","/231.jpg/","/234.jpg/","/236.jpg/","/237.jpg/","/238.jpg/","/239.jpg/",
"/242.jpg/","/244.jpg/","/246.jpg/","/250.jpg/","/252.jpg/","/253.jpg/","/254.jpg/","/256.jpg/","/257.jpg/","/259.jpg/","/261.jpg/","/264.jpg/","/267.jpg/",
"/271.jpg/","/273.jpg/","/278.jpg/","/280.jpg/","/281.jpg/","/283.jpg/","/284.jpg/","/290.jpg/","/295.jpg/","/297.jpg/","/300.jpg/","/302.jpg/","/306.jpg/",
"/308.jpg/","/317.jpg/","/350.00~~100.00.jpg/","/350.00~-100.00.jpg/","/500≤~-300.jpg/","/@-.jpg/","/@-@-@-.jpg/","/0.2.jpg/","/0.03.jpg/","/0.9m@km.jpg/",
"/0.12m@km.jpg/","/1.3.jpg/","/2.3.jpg/","/4.1.jpg/","/5.0~5.0.jpg/","/5.0~5.0（m@km）.jpg/","/5.0~5.0m@km.jpg/","/5.0~+5.0.jpg/","/5~+5.jpg/","/20.jpg/",
"/50~-300.jpg/","/51.jpg/","/60.jpg/","/100~-350.jpg/","/131.jpg/","/139.jpg/","/143.jpg/","/149.jpg/","/182.jpg/","/213.jpg/","/239.jpg/","/242.jpg/","/247.jpg/",
"/248.jpg/","/249.jpg/","/251.jpg/","/265.jpg/","/283.jpg/","/300.jpg/"]
for line in open("/mnt/sources2/train_data/lstm_tongyong/data_unsure/test.txt"):
    line = line.strip('\n')    
    for i in range(0,len(wenjian)):
        if wenjian[i] in line:
            print line
            line=line.replace(wenjian[i],"/检验项内容/")
            print line
    with open('/mnt/sources2/train_data/lstm_tongyong/data_unsure/new_test.txt', 'a') as f:
        f.writelines(line + '\n')