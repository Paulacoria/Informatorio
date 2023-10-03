# Ejercicio 7. Guíe de estructuras de datos.
# 7-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones. 
# Agregar una cuarta ciudad al diccionario con su respectiva población. Mostrar el diccionario resultante.

ciudades = { "Buenos Aires": 35000000,
            "Chaco": 1000000,
            "Snata Fe": 1500000 }
print(ciudades)

ciudades.update({"Corrientes": 1000000})

print(ciudades)

print("La población de la ciudad de Buenos Aires es", ciudades["Buenos Aires"])
