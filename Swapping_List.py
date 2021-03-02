#!/usr/bin/env python
# coding: utf-8

# In[4]:


def swapList(): 
    lst=[]
    size=int(input('Enter the size of array: '))
    for i in range(1,size+1):
        n=int(input('enter the elements: '))
        lst.append(n) 
        
    temp = lst[0] 
    lst[0] = lst[size - 1] 
    lst[size - 1] = temp 
    
    return lst
  
print(swapList()) 

