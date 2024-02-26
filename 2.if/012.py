"""
Pide dos números. Si el primero es mayor que el segundo, muestra primero el segundo número y luego el primero; de lo contrario, muestra primero el primer número y luego el segundo.
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))


if num1 > num2:
  print(num2, num1)
else:
  print(num1, num2)