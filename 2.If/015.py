"""
Pide al usuario que ingrese su color favorito. Si ingresan "rojo", "ROJO" o "Rojo", muestra el mensaje "A mí también me gusta el rojo"; de lo contrario, muestra el mensaje "No me gusta [color], prefiero el rojo".
"""

color = input("Ingresa tu color favorito: ")

if color == "rojo" or color =="ROJO" or color == "Rojo":
  print("A mí también me gusta el rojo.")
else:
  print(f"No me gusta el {color}, prefiero el rojo.")