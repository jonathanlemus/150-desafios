""" Muestra el siguiente mensaje:

1) Cuadrado
2) Triángulo

Ingresa un número

Si el usuario ingresa 1, entonces debe solicitarle la longitud de uno de sus lados y mostrar el área. Si seleccionan 2, debe pedir la base y la altura del triángulo y mostrar el área. Si escriben cualquier otra cosa, debería mostrarles un mensaje de error adecuado.
"""

print("1) Cuadrado\n2) Triángulo\n")
menu_opcion = int(input("Ingresa un número: "))

if menu_opcion == 1:
  longitud = int(input("Escribe la longitud de uno de sus lados: "))
  area = longitud * longitud
  print(f"El área de tu cuadrado es {area}")
elif menu_opcion == 2:
  base = int(input("Escribe la base del triángulo: "))
  altura = int(input("Escribe la altura del triángulo: "))
  area = (base * altura) / 2
  print(f"El área de tu triángulo es: {area}")
else:
  print("Opción seleccionada incorrecta.")