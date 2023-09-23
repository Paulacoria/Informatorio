if True:
    print("Voy a hacer esta tarea")
    print("Se cumplió esta condición")

edad = 19
if edad >= 16:
    print("Usted puede votar") 

edad = 15 
if edad >=16:
    print("Usted puede votar")
if edad < 16:
    print("Usted NO puede votar")

notas = [6,8,8,8,9]
suma = 0
for value in notas:
    suma = suma + value

cantidad_elementos = len(notas)
promedio = suma / cantidad_elementos
print("El promedio es:", promedio)

notas = [6,8,8,8,9]
print ("El promedio es:", sum(notas)/len(notas))


