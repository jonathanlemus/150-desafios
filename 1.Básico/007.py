"""
Pide al usuario su nombre y edad. Suma 1 a su edad y muestra el resultado "[Nombre] en tu próximo cumpleaños tendrás [nueva edad]".
"""

nombre = input("¿Cuál es tu nombre?: ")
edad = int(input("¿Cuántos años tienes?: "))
nueva_edad = edad + 1

print(f"{nombre}, en tu próximo cumpleaños tendrás {nueva_edad}")