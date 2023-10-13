
from random import randint
from grafico import dibujar_intentos

palabras = ["rapido", "nublado", "estructura", "naranja", "materia", "disfraz" ]
indice_max_palabras = len(palabras) - 1

indice_aleatorio = randint(0, indice_max_palabras)
palabra_aleatoria = palabras[indice_aleatorio]

palabra_oculta = [" x "] * len(palabra_aleatoria)
print(palabra_oculta)

intentos = 6

adivinadas =[]
incorrectas = []

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't' , 'u', 'v', 'w', 'x', 'y', 'z']


letra_ingresada = input("Ingrese una letra: ")

while intentos > 0:
   
    if letra_ingresada in letras:
        ind = 0 
        letra_correcta = False
        for letra in palabra_aleatoria:
            if letra == letra_ingresada:
                letra_correcta = True
                palabra_oculta[ind] = letra_ingresada
        ind += 1      
    else:
        print("Ya ha ingresado esa letra")   

    if letra_correcta:
        adivinadas.append(letra_ingresada)
    else:
        incorrectas.append(letra_ingresada)
        intentos -= 1
        dibujar_intentos(intentos)
        print("Incorrecto, te quedan", str(intentos), "intentos")
    
    letras.remove(letra_ingresada) 
  
    print(f"Letras adivinadas: {adivinadas}")
    print(f"Letras incorrectas: {incorrectas}")
    
    letra_ingresada = input("Ingrese una letra: ")

if intentos == 0:
    print("Juego finalizado")

