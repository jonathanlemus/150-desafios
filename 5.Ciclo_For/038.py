# Cambia el programa 037 para que también solicite un número. Muestra su nombre (una letra a la vez en cada línea) y repite esto la cantidad de veces que ingresaron.

nombre = input("Ingresa tu nombre: ")
num = int(input("Ingresa un número: "))

for x in range(0, num):
  for i in nombre:
    print(i)