# Pide al usuario que escriba la primera línea de una canción infantil y muestra la longitud de la cadena. Pregunta por un número de inicio y un número de finalización, y luego muestra solo esa sección del texto (recuerda que en Python se empieza a contar desde 0 y no desde 1).

frase = input("Escribe una frase célebre: ")
print("Esta frase tiene", len(frase), "letras.")

inicio = int(input("Escribe un número de inicio: "))
final = int(input("Escribe un número de final: "))

parte = (frase[inicio:final])

print(parte)