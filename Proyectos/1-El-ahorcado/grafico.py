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
juego_perdido = '''
___
    O
   /|\\
   / \\
   
'''

intentos_restantes_1 = '''
___
    O
   /|\\
   /
'''
intentos_restantes_2 = '''
___
    O
   /|\\
   
'''

intentos_restantes_3 = '''
___
    O
   /|
'''

intentos_restantes_4 = '''
___
    O
    |

'''
intentos_restantes_5 = '''
___
    O
    
'''

def dibujar_intentos(intento):
    
    if intento == 0:
        print(juego_perdido)    
    elif intento == 1:
        print(intentos_restantes_1)
    elif intento == 2:
        print(intentos_restantes_2)
    elif intento == 3:
        print(intentos_restantes_3)
    elif intento == 4:
        print(intentos_restantes_4)
    elif intento == 5:
        print(intentos_restantes_5)

    
    



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