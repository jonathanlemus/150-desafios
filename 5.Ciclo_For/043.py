"""
Pregunta en qué dirección desea contar el usuario (hacia arriba o hacia abajo). Si seleccionan hacia arriba, pídeles el número máximo y luego cuenta desde 1 hasta ese número. Si seleccionan hacia abajo, pídeles que ingresen un número menor a 20 y luego cuenta regresivamente desde 20 hasta ese número. Si ingresaron algo diferente a "hacia arriba" o "hacia abajo", muestra el mensaje "No entiendo".
"""

direccion = input("¿En qué dirección deseas contar? (arriba/abajo): ")

if direccion == "arriba":
  num = int(input("Escribe un número máximo: "))
  for i in range(1, num+1):
    print(i)
elif direccion == "abajo":
  num = int(input("Escribe un número menor a 20: "))
  for i in range(20, num-1, -1):
    print(i)
else:
  print("No entiendo.")