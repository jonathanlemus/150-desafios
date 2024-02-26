# Modifica el programa 035 para que pida al usuario que ingrese su nombre y un número, y luego muestre su nombre esa cantidad de veces.

nombre = input("Ingresa tu nombre: ")
num = int(input("Ingresa un número: "))

for i in range(0, num):
  print(nombre)