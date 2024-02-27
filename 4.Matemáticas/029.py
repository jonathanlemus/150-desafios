"""
Pide al usuario que ingrese un número entero que sea mayor a 500. Calcula la raíz cuadrada de ese número y muéstrala con dos decimales.
"""

import math

num = int(input("Escribe un número entero mayor a 500: "))
respuesta = math.sqrt(num)

print(round(respuesta, 2))