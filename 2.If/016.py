"""
Pregunta al usuario si está lloviendo y convierte su respuesta a minúsculas para que no importe en qué caso la escriban. Si responden "sí", pregunta si hace viento. Si responden "sí" a esta segunda pregunta, muestra la respuesta "Hace demasiado viento para un paraguas"; de lo contrario, muestra el mensaje "Lleva un paraguas". Si no respondieron "sí" a la primera pregunta, muestra la respuesta "Disfruta tu día".
"""

lloviendo = input("¿Está lloviendo ⛈️?: ")
lloviendo = str.lower(lloviendo)

if lloviendo == "si":
  viento = input("¿Está haciendo viento 🌬️?: ")
  viento = str.lower(viento)
  if viento == "si":
    print("Hace demasiado viento para un paraguas 🌂.")
  else:
    print("Lleva paraguas ☂️.")
else:
  print("¡Disfruta tu día 😙!")