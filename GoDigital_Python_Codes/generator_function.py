# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:14:58 2021

@author: Tushar patil
"""

#generator functions 
#generator function 
def gen123():
    print("one")
    print("two")
    yield 1
    yield 2
    yield 3
    
    
"""
    g=gen123()
    
    next(g)
"""