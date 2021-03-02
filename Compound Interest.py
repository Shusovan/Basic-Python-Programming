#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Compound_Interest():
    P=int(input('Enter the principle'))
    r=int(input('Enter the rate of interest'))
    t=int(input('Enter the time'))
    A=P*((1-r/100)**t)
    return A
print('Compuond Interest',Compound_Interest())

