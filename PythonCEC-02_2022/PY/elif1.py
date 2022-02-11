# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:15:18 2022

@author: Alkhorayef
"""

acl=int(input("ingrese el # de acl "))
if acl >=1 and acl <=99:
    print("la acl es estandar")
elif acl >=100 and acl <=199:
    print("la acl es extendida")
else:
    print("el dato ingresado no es de un acl")


nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
ubicacion=input("ingrese su ubicacion: ")
edad=input("ingrese su edad: ")
space= " "
print("hola1", nombre+space+apellido + "tu ubicacion es: " 
      +ubicacion+space + "tienes cuantos años:", edad, 
      space+"años")




    