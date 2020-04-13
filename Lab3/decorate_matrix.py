#!/usr/bin/env python
# coding: utf-8

# In[5]:


# -*- coding: utf-8 -*-
import numpy as np

def decorate_matrix(N):
    if N<1:
        return None
    matrix=np.zeros((N,N))
    matrix[:]=1
    if N>2:
        matrix[1:-1, 1:-1]=0
    return matrix

N = int(input("Enter matrix size: "))
matrix = decorate_matrix(N)
matrix


# In[ ]:




