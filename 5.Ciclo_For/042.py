"""
Establece una variable llamada total en 0. Pide al usuario que ingrese cinco números y después de cada entrada pregúntales si desean que ese número se incluya. Si lo desean, entonces agrega el número al total. Si no lo desean incluir, no lo agregues al total. Después de que hayan ingresado los cinco números, muestra el total.
"""

total = 0

for i in range(0, 5):
  num = int(input("Ingresa un número: "))
  res = input("¿Deseas que este número se incluya? (y/n) ")
  if res == "y":
    total = total + num

print(total)