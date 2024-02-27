"""
Pide al usuario que ingrese su primer nombre y luego pídeles que ingresen su apellido. Únelos con un espacio entre ellos y muestra el nombre completo junto con la longitud total del nombre.
"""

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_completo = nombre + " " + apellido

print(nombre_completo)
print(len(nombre_completo))