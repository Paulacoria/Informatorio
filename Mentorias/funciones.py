'''
9-Crea una función llamada promedio que tome una lista de números como parámetro
 y devuelva el promedio de esos números.
'''


numeros = []
numero1 = int(input("Ingrese un número:"))
numero2 = int(input("Ingrese otro número:"))


numeros.append(numero1)
numeros.append(numero2)

def promedio(numeros):
    i = 0
    for numero in numeros:
        i += numero
    return i /(len(numeros))

print(promedio(numeros))


#VARIABLES GLOBALES: son las que se definen fuera de las funciones
#VARIABLES LOCALES: son las que se definen dentro de alguna función

'''Como importar los módulos para jugar con números aleatorios'''
from random import randint # siempre va al principio del archivo, al ser una importación

aleatorio = randint(1,20)
print("el número es:", aleatorio)

