'''
Representación gráfica del munieco del juego del ahorcado
___
   O
  /|\
  / \
 





cantidad de intentos:
5 - pierna 2
4 - pierna 1
3 - mano 2
4 - mano 1
2 - cuerpo
1 - cabeza



'''
intento_1 = ''''
___
    O
'''

intento_2 = '''
___
    O
    |
'''
intento_3 = '''
___
    O
    |\\
'''

intento_4 = '''
___
    O
   /|\\
'''

intento_5 = '''
___
    O
   /|\\
   /

'''
intento_6 = '''
___
    O
   /|\\
   / \\

'''

def dibujar_intentos(intento):
    print(f"gráfico intento restante {intento}: ")

    if intento == 1:
        print(intento_1)    
    elif intento == 2:
        print(intento_2)
    elif intento == 3:
        print(intento_3)
    elif intento == 4:
        print(intento_4)
    elif intento == 5:
        print(intento_5)
    elif intento == 6:
        print(intento_6)

'''
if __name__ == "__main__":
probamos nuestra función:

for intento in range(6, 0, -1):
    dibujar_intentos(intento)
'''

'''
cuando voy al archivo del proyecto, agregar:
from grafico import (dibujar_intentos)
'''