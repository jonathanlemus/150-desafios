"""
Pide al usuario que ingrese el radio de un círculo (medida desde el punto central hasta el borde). Calcula el área del círculo (π*radio²).
"""

import math

radio = int(input("Ingresa el radio de un círculo: "))
area = math.pi*(radio ** 2)

print(area)