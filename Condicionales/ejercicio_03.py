"""
Escribir un programa que imprima "Capicúa" si un número de entrada de cuatro digitos es capicua,
o "No lo es" en caso contrario. Un numero es capicua si se escribe igual al derecho y al revez.
Por ejemplo, 1551 es un numero capicua.
"""

numero = input("Ingresa un numero: ")
nuevo_numero = ""

if len(numero) == 4:
    numero_len = len(numero)
    for n in range(numero_len):
        nuevo_numero += numero[n]
        numero_len -= 1
    
    if numero != nuevo_numero:
        print(f"El numero {numero} no es capicua")
    else:
        print(f"El numero {numero} es capicua")

else:
    print("El numero no es de cuatro digitos")



