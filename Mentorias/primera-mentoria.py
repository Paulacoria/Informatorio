

# crear una colección de facturas y sacar el promedio
# usar una lista para este ejercicio
# pedir al usuario primero la cantidad de facturas


facturas = []

numero_de_facturas = int(input("ingrese el número de facturas: "))

for num in range(1, numero_de_facturas+1):

    monto = int(input(f"ingrese monto de factura {num}: "))
    facturas.append(monto)


suma = 0
for monto in facturas:
    suma += monto

promedio = suma / numero_de_facturas

print("El promedio de las facturas es: ", promedio)






