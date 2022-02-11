# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:28:36 2022

@author: Alkhorayef
"""

def suma(*args):
    print("\nTipo de datos del argumentos: ", 
        type(args))
    sum = 0
    for n in args:
        sum +=n
        #sum=sum+n
        
    print("sum:",sum)
    
suma(3)
suma(1)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,4,5,6)
suma(1,2,3,4,5,6,7,8,9,10)

     
    
    