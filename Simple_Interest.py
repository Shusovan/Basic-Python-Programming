#!/usr/bin/env python
# coding: utf-8

# In[13]:


def Simple_Interest():
    P=int(input('Enter the principle amt: '))
    r=float(input('Enter the rate of interest: '))
    t=int(input('Enter the time: '))
    S=P*t*r/100
    return S
print('Simnple interst',Simple_Interest())


# In[ ]:




