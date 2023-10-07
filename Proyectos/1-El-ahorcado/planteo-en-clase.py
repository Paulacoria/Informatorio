'''
Requisitos:
1.El juego debe tener una lista de palabras predefinidas de las cuales se elige una palabra aleatoriamente para que el jugador adivine.
2.El jugador tiene un número limitado de intentos para adivinar la palabra (por ejemplo, 6 intentos).
3.Debe mostrar las letras adivinadas y las letras incorrectas.
4.El juego debe verificar si la letra ingresada por el jugador está en la
palabra secreta y actualizar el estado del juego en consecuencia.
5.El juego debe terminar cuando el jugador adivine la palabra o se quede
sin intentos.
6.Debe mostrar un mensaje de victoria o derrota al final del juego. 7.Opcional: debe mostrar una representación gráfica del estado actual del
ahorcado. Puedes usar arte ASCII para esto.

'''

#1.El juego debe tener una lista de palabras predefinidas
# de las cuales se elige una palabra aleatoriamente para que el jugador adivine.


from random import randint


palabras = ["messi", "casa", "auto", "maradona", "river", "bicicleta"]

indice_palabras_max = (len(palabras)) - 1
indice_aleatorio = randint(0, indice_palabras_max)
print(indice_aleatorio)

palabra_aleatoria = palabras[indice_aleatorio] #palabra aleatorio

# El jugador tiene un número limitado de intentos para adivinar la palabra
# (por ejemplo, 6 intentos)

intentos = 6

#Debe mostrar las letras adivinadas y las letras incorrectas.
correctas = []
incorrectas = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't' , 'u', 'v', 'w', 'x', 'y', 'z']
palabra_secreta = ['x'] * len(palabra_aleatoria)
print(palabra_secreta)

#4.El juego debe verificar si la letra ingresada por el jugador está en la
# palabra secreta y actualizar el estado del juego en consecuencia.

letra_ingresada = input("Por favor ingrese una letra: ")

ind = 0
existe_letra = False
for letra in palabra_aleatoria:
    if letra == letra_ingresada:
        existe_letra = True
        palabra_secreta[ind] = letra_ingresada

ind +=1
if existe_letra:
    correctas.append(letra_ingresada)
else:
    incorrectas.append(letra_ingresada)
    intentos -= 1

letras.remove(letra_ingresada)

#5.El juego debe terminar cuando el jugador adivine la palabra o se quede
# sin intentos.




