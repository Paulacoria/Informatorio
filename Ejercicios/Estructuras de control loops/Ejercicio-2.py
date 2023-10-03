# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos los números naturales del 1 hasta ese número.

suma = 0
i = 0

numero = int(input("Ingrese un número: "))

while numero >= 1:
    suma += numero
    i += 1

print("La suma es: ", suma)






