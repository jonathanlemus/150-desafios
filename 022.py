# 022
# Pide al usuario que ingrese su nombre y apellido en minúsculas. Cambia las mayúsculas a mayúsculas iniciales y únelos. Muestra el resultado final.

nombre = input("Escribe tu nombre en minúsculas: ")
apellido = input("Escribe tu apellido en minúsculas: ")

nombre = nombre.title()
apellido = apellido.title()

nombre_completo = nombre + " " + apellido

print(nombre_completo)
