# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:41:32 2022

@author: doguilmak
"""

import numpy as np

tam = 972
n = 4
an=np.zeros(tam)

an[0] = 1
an[1] = 1
an[2] = 1

while n < tam:
    an[n] = (9 * an[n // 3]) + n
    n+=1

tam = 972
n = 0 
an_arr = []
while n < tam:
    if n >= 0 and n <=972:
        print(f"a[{n}] = ", an[n])
        an_arr.append(an[n])
    n+=1

import matplotlib.pyplot as plt
plt.plot(an_arr)
plt.grid()
plt.xlabel('n')
plt.ylabel('$a_n$')
plt.title('Recurrence Periodic')
plt.savefig('recurrence_periodic.png')
plt.show()
