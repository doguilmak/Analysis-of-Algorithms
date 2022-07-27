# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:32:23 2022

@author: doguilmak
"""
import numpy as np

tam = 1000
n = 3
an=np.zeros(tam)
an[0] = 0
an[1] = 0
an[2] = 0

while n < tam:
    an[n] = (((n - 3) * an[n - 1]) / n) + 1
    print(an[n])
    n+=1
    
print(f"Answer of the question : {an[999]}")