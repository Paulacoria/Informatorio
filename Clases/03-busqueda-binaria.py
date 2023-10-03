# Ejercicio 19 guía
# Escribe un programa que pida al ususario un número y luego imprima si ese número es un número perfecto o no.
# Un número perfecto es aquel que es igual a la suma de sus divisores propios
# (ecluyendo el propio número)
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se puede dividir entre 1, 2, 3,
# y cuando sumas esos números, el resultado es 6.

numero = int(input("Ingrese un número: "))

divisores = []
suma= 0

for numero_menor in range(1,numero):
    if numero % numero_menor == 0:
        #print(f"{numero_menor} es divisor")
       divisores.append(numero_menor)

suma =  sum(divisores)

if suma == numero:
    perfecto = True
else:
    perfecto =  False


if perfecto:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")




