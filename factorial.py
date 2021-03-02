#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorial():
    n=int(input('Enter a number: '))
    if(n==0 or n==1):
        return 1
    else:
        fact=1
        while(n>1):
            fact=fact*n
            n=n-1
        return fact
print('Factorial of n',factorial())


# In[ ]:




