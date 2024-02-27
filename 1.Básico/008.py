"""
Pregunta por el precio total de la cuenta, luego pregunta cuántos comensales hay. Divide el total de la cuenta entre el número de comensales y muestra cuánto debe pagar cada persona.
"""

total = int(input("Total de la cuenta a pagar: "))
comensales = int(input("¿Cuántos comensales son?: "))
pagar = total / comensales

print(f'Cada persona debe pagar ${pagar}.')