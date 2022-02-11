# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:11:58 2022

@author: Alkhorayef
"""

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
