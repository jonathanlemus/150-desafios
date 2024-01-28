# 006
# Pregunta cuántas porciones de pizza tenía el usuario y cuántas ha comido. Calcula cuántas porciones le quedan y muestra la respuesta en un formato fácil de entender para el usuario.

porciones_pizza = int(input("¿Cuántas porciones tenía la pizza?: "))
porciones_pizza_comido = int(input("¿Cuántas porciones de pizza te has comido?: "))

porciones_sobrantes = porciones_pizza - porciones_pizza_comido

print(f"Te sobran {porciones_sobrantes} porciones de pizza 🍕")