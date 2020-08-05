'''
功能：生成不定长数字语料txt
'''
# -*- coding:utf-8 -*-
import os
import numpy as np

def create_num(num_len,list_len):
    with open('./number.txt', 'a') as f:
        for line in range(list_len):
            num_rand_len = int(num_len * np.random.random())
            if num_rand_len >0:
                for i in range(0,num_rand_len):
                    rand=str(np.random.random_integers(0,9))
                    f.writelines(rand)
                f.writelines('\n')

def create_cn(num_len,list_len,txt):
    with open('./cn.txt','a') as f:
        with open(txt,'r') as f_read:
            for l in f_read.read().splitlines():
                l=l.replace(" ","")
                l=l.replace("/","")
                line_len = len(l)
                if line_len > 0:
                    num_rand_len = np.random.random_integers(0,num_len)   #随机一个label字符串长度
                    if num_rand_len >0:
                        print(l)
                        print(num_rand_len)
                        print(line_len//num_rand_len+1)
                        for i in range(line_len//num_rand_len +1 ):
                            writeline = l [num_rand_len*i:num_rand_len*(1+i)] + '\n'
                            f.writelines(writeline)


txt_path = './小说/6028.txt'
num_len=30
# list_len=1000000
list_len=1000000
# create_num(num_len,list_len)
create_cn(num_len,list_len,txt_path)