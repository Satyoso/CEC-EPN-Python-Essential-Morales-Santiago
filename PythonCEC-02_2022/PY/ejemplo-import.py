# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:29:38 2022

@author: Alkhorayef
"""

from math import pi as p, radians as r, degrees as d, sin as s, cos as c, tan as t, asin as ars

ad = 90
ar = r(ad)
ad = d(ar)

print(ad == 90.)
print(ar == p / 2.)
print(s(ar) / c(ar) == t(ar))
print(ars(s(ar)) == ar)