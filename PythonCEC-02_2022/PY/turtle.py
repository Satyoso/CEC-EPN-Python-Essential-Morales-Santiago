# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:24:05 2022

@author: Alkhorayef
"""

from turtle import *
color("red" , "yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
