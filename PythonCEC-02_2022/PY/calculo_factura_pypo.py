# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:02:57 2022

@author: Alkhorayef
"""

from tostadas_pipo.utilidades import calculos
from tostadas_pipo.utilidades.impuestos import impuesto_iva14

monto = int(input("introduzca un monto entero: "))
monto_suma = int(input("introduzca un monto entero a sumar: "))

suma = impuesto_iva14(monto) + calculos.suma_total(monto_suma)
print ("total a facturar: {0} BsS, con iva 14%. ".format(suma) )
