# 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Inserte un número entero: "))

if (numero % 2 == 0) and (numero % 3 ==0):
    print("El número", numero, "es múltiplo de 2 y de 3 a la vez")

else:
    print("El número", numero, "no es múltiplo de 2 y de 3 a la vez")







