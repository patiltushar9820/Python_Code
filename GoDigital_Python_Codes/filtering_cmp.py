# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:38:15 2021

@author: Tushar patil
"""
#filtering comprehension
def even(x):
    if x%2==0:
        return x
    else:
        return False
dict1={i for i in range(10) if even(i)}
print('even numbers :',dict1)