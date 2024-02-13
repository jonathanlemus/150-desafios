"""
Pregunta la edad del usuario. Si tienen 18 años o más, muestra el mensaje "Puedes votar"; si tienen 17 años, muestra el mensaje "Puedes aprender a conducir"; si tienen 16 años, muestra el mensaje "Puedes comprar un boleto de lotería"; si son menores de 16 años, muestra el mensaje "Puedes salir a pedir dulces en Halloween".
"""

edad = int(input("¿Cuántos años tienes?: "))

if edad >= 18:
  print("Puedes votar.")
elif edad == 17:
  print("Puedes aprender a conducir.")
elif edad == 16:
  print("Puedes comprar un boleto de lotería.")
else:
  print("Puedes salir a pedir dulces en Halloween 🎃.")
  