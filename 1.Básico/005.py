"""
Pide al usuario que ingrese tres números. Suma los dos primeros números y luego multiplica este total por el tercero. Muestra la respuesta como "La respuesta es [respuesta]".
"""

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
respuesta = (num1 + num2) * num3

print(f"La respuesta es {respuesta}")