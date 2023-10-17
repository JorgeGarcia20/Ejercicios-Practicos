"""
Escribir un programa que pida al usuario dos numeros enteros y muestre
por pantalla el siguiente mensaje:
	- "n1" entre "n2" da un cociente "c" y un resto "r", donde "n1" y "n2" son
		numeros introducidos por el usuario, y "c" y "r" son el cociente y el resto
		de la divicion entera respectivamente.
"""

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un segundo numero: "))

cociente = n1 / n2
residuo = n1 % n2

print(f"""{n1} entre {n2} da un cociente {cociente} y un resto {residuo}, donde {n1} y {n2} son
	numeros introducidos por el usuario, y {cociente} y {residuo} son el cociente y el resto
	de la divicion entera respectivamente.""")