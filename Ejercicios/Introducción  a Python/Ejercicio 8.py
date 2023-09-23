# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

radio = int(input("Ingrese el radio del círculo: "))

diametro = radio*2
circunferencia = diametro * 3.14159
area = (radio**2) * 3.14159



print("El diámetro del círculo es: ", diametro)
print("La circunferencia del círculo es: ",circunferencia)
print("El área del círculo es: ", area)

