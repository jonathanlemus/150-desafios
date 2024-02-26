"""

Pide al usuario que ingrese un número menor a 20. Si ingresan un número igual o mayor a 20, muestra el mensaje "Demasiado alto"; de lo contrario, muestra "Gracias".

"""

num = int(input("Ingresa un número menor a 20: "))

if num >= 20:
  print("Demasiado alto")
else:
  print("Gracias")