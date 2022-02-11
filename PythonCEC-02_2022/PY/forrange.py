# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:47:00 2022

@author: Alkhorayef
"""

print("comienzo")
for i in range(1,10,3):
    print(i,end=" ")
    print()
    print("final")
    
       
result=0
n=10
for i in range(1,n+1,1):
        print(i)
        result += i
        #print(result)
        #this ^^ is the shorthand for
        # result = result + i
print("el resultado de la suma de 1 hasta ", n ,"es: ",result)


veces=int(input("cuantas veces quieres que te salude"))
for i in range(1,veces+1,1):
    print("hola", end="")
print()
print("adios")
