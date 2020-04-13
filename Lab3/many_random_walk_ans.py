#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import numpy as np
import matplotlib.pyplot as plt

def fsob(walk):
    return (np.abs(walk) >= 30).argmax()

x=np.around(np.linspace(0, 999,999))
walks=np.zeros((5000,1000))
fsob30=[]
for walk in walks:
    position = 0
    for i in x:
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk[int(i)]=position
    fsob30.append(fsob(walk))
#fsob30
#walks
print(("Walks:\n{0}\nFirst step over 30:\n{1}").format(walks,fsob30))


# In[ ]:




