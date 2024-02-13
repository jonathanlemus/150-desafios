# 018
# Pide al usuario que ingrese un número. Si es menor a 10, muestra el mensaje "Demasiado bajo"; si su número está entre 10 y 20, muestra "Correcto"; de lo contrario, muestra "Demasiado alto".

num = int(input("Ingresa un número: "))

if num < 10:
  print("Demasiado bajo.")
elif num > 10 and num < 20:
  print("Correcto.")
else:
  print("Demasiado alto.")
