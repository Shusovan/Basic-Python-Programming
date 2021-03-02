#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input('Enter a number: '))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print('Its is not prime',n)
            break
    else:
        print('It is prime',n)
else:
     print('It is not prime',n)           

