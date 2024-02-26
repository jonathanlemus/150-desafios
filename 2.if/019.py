# 019
# Pide al usuario que ingrese 1, 2 o 3. Si ingresan 1, muestra el mensaje "Gracias"; si ingresan 2, muestra "Bien hecho"; si ingresan 3, muestra "Correcto". Si ingresan cualquier otra cosa, muestra "Mensaje de error".

num = int(input("Ingresa el número 1, 2, o 3: "))

if num == 1:
  print("Gracias.")
elif num == 2:
  print("Bien hecho.")
elif num == 3:
  print("Correcto.")
else:
  print("Mensaje de error.")