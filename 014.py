"""
Pide al usuario que ingrese un número entre 10 y 20 (inclusive). Si ingresan un número dentro de este rango, muestra el mensaje "Gracias"; de lo contrario, muestra el mensaje "Respuesta incorrecta".
"""

num = int(input("Ingresa un número entre 10 y 20: "))

if num >= 10 and num <= 20:
  print("Gracias 🫂")
else:
  print("Respuesta incorrecta.")