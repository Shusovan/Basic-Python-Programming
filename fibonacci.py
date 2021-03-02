# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 08:49:37 2020

@author: SHUSOVAN CHAKRABORTY
"""


def Fibonacci():
    f=0
    s=1
    count=0
    n=int(input('Enter a number: '))
    if n<0:
        print('Incorrect input')
    if n==1:
        return f
    else:
        print('Fibonacci Series')
        while count<n:
            print(f)
            next=f+s
            f=s
            s=next
            count+=1
print(Fibonacci()) 