# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 23:33:28 2022

@author: Alkhorayef
"""

def direction(ciudad,calle,barrio):
    print("la direccion de envio es: ")
    print("sector la ", barrio )
    print("en la calle ", calle )
    print("en la ciudad de: ", ciudad)
    
cl=input("ingrese la calle: ")
ba=input("ingrse el sector de domicilio: ")
ci=input("ingrese la ciudad: ")

direction(ci , cl, ba)

