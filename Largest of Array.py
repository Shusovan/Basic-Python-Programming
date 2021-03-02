#!/usr/bin/env python
# coding: utf-8

# In[13]:


def LargestOfArray():
    n=int(input('Enter no. of elements of array: '))
    arr=range(n)
    max=arr[0]
    for i in range(0,n):
        if arr[i]>max:
            max=arr[i]
    print('The Largest of array is')
    return max
print(LargestOfArray())

