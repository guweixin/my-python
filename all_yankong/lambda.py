# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:21:32 2018

@author: guweixin
"""

f=lambda x:x+1

print (f(4))
from functools import reduce 
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print (list(filter(lambda x: x % 3 == 0, foo)))
#[18, 9, 24, 12, 27]

print (list(map(lambda x: x * 2 + 10, foo)))
#[14, 46, 28, 54, 44, 58, 26, 34, 64]

print (reduce(lambda x, y: x + y, foo))