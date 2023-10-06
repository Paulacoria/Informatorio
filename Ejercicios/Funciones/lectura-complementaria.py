# Las funciones son bloques de código reutilizables que realizan una tera específica.

#sentencia def - definiendo una función
def saludar(nombre): #nombre es un parámetro
    print(f"Hola, {nombre}")
saludar("Info") #Info es un argumento

def suma(a,b):
    resultado = a + b
    return resultado

resultado_suma = suma(3,4)
print(resultado_suma)

#Parámetro: es una variable que se define en la declaración de una función.
#Argumento: es el valor real que se pasa a una función cuando se la llama.


def calcular_area(base, altura):
    ''''
    Calcula el área del triángulo.

    Parámetros:
    - base: la base del triángulo.
    - altura: la altura del triángulo.

    Retorna: 
    - El área del triángulo.
    
    
    '''
    area = (base * altura) / 2
    return area

area_triangulo = calcular_area(5,3)
print(area_triangulo)
print(calcular_area.__doc__)


def contar_hasta_cinco():
    for i in range(1,6):
        print(i)

contar_hasta_cinco()


def obtener_promedio(lista):
    if len(lista) == 0:
        return None
    # Por qué acá no va un else?
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

numeros = [4, 6, 8, 10]
promedio_numeros = obtener_promedio(numeros)
print(promedio_numeros)

vacio = []
promedio_vacio = obtener_promedio(vacio)
print(promedio_vacio)

# PARÁMETROS POR POSICIÓN
# Se refieren a la forma en que se pasan los argumentos a una función en Python
# Los argumentos a la función en el mismo orden en el que se definen los 
# parámetros en la declaración de la función.

def calcular_precio_total(precio_unitario, cantidad):
    precio_total = precio_unitario * cantidad
    return precio_total

precio_final = calcular_precio_total(10, 5)
print(f"El precio final es: {precio_final}")

#PARÁMETROS POR NOMBRE
# Permiten laasignación de argumentos a una función en python mediante
# la especificación del nombre del parámetro correspondiente.

def saludar(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años.")

saludar(nombre = "Juan", edad = 25)

#LLAMADA SIN ARGUMENTOS/PARAMETROS POR DEFECTO
# Los valores predeterminados son valores asignados a los parámetros
# en la definción de la función

def saludar(nombre = "Usuario"):
    print(f"Hola {nombre}")

saludar()
saludar("Juan")



