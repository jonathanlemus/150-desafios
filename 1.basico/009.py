# 009
# Escribe un programa que pregunte por un número de días y luego muestre cuántas horas, minutos y segundos hay en ese número de días.

dias = int(input("Ingresa el número de días: "))

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")