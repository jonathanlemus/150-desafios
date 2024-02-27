"""
Pig Latin toma la primera consonante de una palabra, la mueve al final de la palabra y agrega un "ay". Si una palabra comienza con una vocal, solo agregas "way" al final. Por ejemplo, pig se convierte en igpay, banana se convierte en ananabay, y aadvark se convierte en aadvarkway. Crea un programa que pida al usuario que ingrese una palabra y la convierta en Pig Latin. Asegúrate de que la nueva palabra se muestre en minúsculas.
"""

palabra = input("Por favor, ingresa una palabra: ")
primero = palabra[0]
largo = len(palabra)
resto = palabra[1:largo]

if primero != "a" and primero != "e" and primero != "i" and primero != "o" and primero != "u":
  nueva_palabra = resto + primero + "ay"
else:
  nueva_palabra = palabra + "way"
  print(nueva_palabra.lower())