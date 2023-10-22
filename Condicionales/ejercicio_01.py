"""
Escribir un programa que pida al usuario dos numeros y muestre por pantalla
su division. Si el divisor es cero, el programa debe de mostrar un mensaje
de error.
"""

dividendo = float(input("Ingresa el valor del dividendo: "))
divisor = float(input("Ingresa el valor del divisor: "))

if divisor != 0:
    cociente = dividendo / divisor
    print(f"El cociente de dividir {dividendo} entre {divisor} es: {cociente}")
else:
    print("Error al dividir entre cero.")   