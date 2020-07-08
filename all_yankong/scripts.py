#coding: utf-8
import os
import shutil

with open("./remove.txt") as f:
    lines = f.readlines()

with open("./ImageSets/Main/trainval.txt") as train_f:
    lines_train = train_f.readlines()

with open("./ImageSets/Main/test.txt") as test_f:
    lines_test = test_f.readlines()

trainval = [line for line in lines_train if line not in lines]

test = [line for line in lines_test  if line not in lines]

with open("./trainval.txt", "w") as w_train:
    for i in trainval:
        w_train.writelines(i)

with open("./test.txt", "w") as w_test:
    for i in test:
        w_test.writelines(i)
