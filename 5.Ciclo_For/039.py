# Pide al usuario que ingrese un número entre 1 y 12 y luego muestra la tabla de multiplicar de ese número.

num = int(input("Escribe un número entre el 1 y el 12: "))

#print(f"Elegiste el número {num}\nSu tabla de multiplicación es:\t")

for i in range(1, 13):
  multi = i * num
  print(f"{i} x {num} = {multi}")