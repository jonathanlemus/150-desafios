"""
Pide el radio y la profundidad de un cilindro y calcula el volumen total (área del círculo * profundidad) redondeado a tres decimales.
"""

import math

radio = int(input("Ingresa el radio del cilindro: "))
profundidad= int(input("Ingresa la profundidad del cilindro: "))
area = math.pi*(radio ** 2)
volumen = area * profundidad

print(round(volumen, 3))