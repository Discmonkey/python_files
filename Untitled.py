# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:51:09 2015

@author: maxg
"""

def factorial(N,X):
    if N>1:
        X *= N
        N -=1
        factorial(N,X)
    else:
        print X
    