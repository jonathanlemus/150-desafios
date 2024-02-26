# Pide al usuario que ingrese su primer nombre. Si la longitud de su primer nombre es menor a cinco caracteres, pídeles que ingresen su apellido y únelos (sin espacio) y muestra el nombre en mayúsculas. Si la longitud del primer nombre es de cinco caracteres o más, muestra su primer nombre en minúsculas.

nombre = input("Ingresa tu primer nombre: ")

if len(nombre) < 5:
  apellido = input("Ingresa tu apellido: ")
  nombre = nombre+apellido
  print(nombre.upper())
else:
  print(nombre.lower())