"""
Pide al usuario que ingrese su nombre y un número. Si el número es menor que 10, muestra su nombre esa cantidad de veces; de lo contrario, muestra el mensaje "Demasiado alto" tres veces.
"""

nombre = input("Ingresa tu nombre: ")
num = int(input("Ingresa un número: "))

if num < 10:
  for i in range(0, num):
    print(nombre)
else:
  for i in range(0, 3):
    print("Demasiado alto.")