"""
Pide al usuario que ingrese dos números. Utiliza la división entera para dividir el primer número por el segundo y también calcula el resto. Muestra la respuesta de una manera amigable para el usuario (por ejemplo, si ingresan 7 y 2, muestra "7 dividido por 2 es 3 con 1 de resto").
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
respuesta1 = num1 // num2
respuesta2 = num1 % num2

print(f"{num1} dividido por {num2} es {respuesta1} con {respuesta2} de resto.")