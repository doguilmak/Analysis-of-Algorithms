# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:55:53 2022

@author: doguilmak
"""

import numpy as np

tam = 100
n = 2
an=np.zeros(tam)

an[0] = 0
an[1] = 1

while n < tam:
    an[n] = (9 * an[n - 1]) - (20 * an[n - 2])
    if n >= 2 and n <=100:
        print(f"a[{n}] = ", an[n])
    n+=1

print("\n ====== \n")

tam = 100
n = 2 
while n < tam:
    aux = an[n]/an[n - 1]
    aux = float(aux)
    if n >= 2 and n <= 100:
        print(f"aux[{n}] = ", aux)
    n+=1
