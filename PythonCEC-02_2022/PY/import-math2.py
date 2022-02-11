# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:03:11 2022

@author: Alkhorayef
"""

import math
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
    
#El USO DE MIS VARIABLES
print(sin(pi/2))
#EL USO DE LAS VARIABLES DEL MODULO MATH
print(math.sin(math.pi/2))

