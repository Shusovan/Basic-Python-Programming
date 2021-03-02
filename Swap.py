#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Swap():
    lst=[]
    n=int(input('Enter the size: '))
    for i in range(n):
        value=int(input())
        lst.append(value)
    print('List: ',lst)
    pos1=int(input('Enter 1st position: '))
    pos2=int(input('Enter 2nd position: '))
    lst[pos1], lst[pos2]=lst[pos2], lst[pos1]
    print('\nSwapped List: ')
    return lst
print(Swap())


# In[ ]:





# In[ ]:




