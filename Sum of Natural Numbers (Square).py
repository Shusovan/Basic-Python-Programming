# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:56:22 2020

@author: SHUSOVAN CHAKRABORTY
"""

def NaturalNumber():
    n=int(input('Enter a number'))
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i*i)
    return sum
print(NaturalNumber())