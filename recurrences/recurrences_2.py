# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:52:53 2022

@author: doguilmak
"""

import numpy as np

tam = 100
n = 1
an=np.zeros(tam)
an[0] = 0


while n < tam:
    an[n] = an[n - 1] - ((2 * an[n - 1]) / n) + (2 * (1 - (2 * an[n - 1])/ n))
    print(an[n])
    n+=1
    
print(f"\nAnswer of the question : {an[99]}")