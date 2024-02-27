"""
Pregunta cuántas personas desea invitar el usuario a una fiesta. Si ingresan un número menor a 10, pide los nombres y después de cada nombre muestra "[nombre] ha sido invitado". Si ingresan un número igual o mayor a 10, muestra el mensaje "Demasiadas personas".
"""

invitados = int(input("¿Cuántas personas deseas invitar a la fiesta?: "))

if invitados < 10:
  for i in range(0, invitados):
    nombre = input("Ingresa el nombre de los invitados: ")
    print(f"{nombre} ha sido invitad@")
else:
  print("Demasiadas personas.")