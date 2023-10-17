"""
Escriba un programa que lea un número de cuatro digitos y muestre en pantalla el número escrito en reverso.
Por ejemplo, si el numero leido es 5432, la salida deberia ser 2345.
"""

numero = input("Ingresa un numero: ")
indice = len(numero) - 1
numero_reversa = ""

for i in range(len(numero)):
    numero_reversa += numero[indice]
    indice -= 1

# numero_reversa = join("", lista_numero_reversa)

print(f"El numero ingresado fue: {numero} y el numero al reves seria: {numero_reversa}.")


