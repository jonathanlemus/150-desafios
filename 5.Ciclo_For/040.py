"""
Pide un número menor a 50 y luego cuenta regresivamente desde 50 hasta ese número, asegurándote de mostrar el número que ingresaron en la salida.
"""

num = int(input("Ingresa un número menor a 50: "))

for i in range(50, num-1, -1):
  print(i)