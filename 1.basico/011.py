# 011
# Pide al usuario que ingrese un número mayor a 100 y luego ingrese un número menor a 10. Indícales cuántas veces el número más pequeño cabe en el número más grande en un formato fácil de entender para el usuario.

num_mayor = int(input("Ingresa un número mayor a 100: "))
num_menor = int(input("Ingresa un número menor a 100: "))

respuesta = num_mayor // num_menor

print(f"{num_menor} cabe {respuesta} veces en {num_mayor}")