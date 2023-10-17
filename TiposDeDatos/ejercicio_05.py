"""
Escriba un programa que, dadas las longitudes de los catetos de un triángulo rectángulo
calcule la longitud de su hipotenusa
La formula para calcular la hipotenusa es:
	c² = a² + b²
"""
import math

a = float(input("Ingresa el valor del cateto opuesto: "))
b = float(input("Ingresa el valor del cateto adyacente: "))

c_sqrt = math.pow(a, 2) + math.pow(b, 2)
c = math.sqrt(c_sqrt)

print(f"""
	El triangulo que tiene como valor {a} en su cateto opuesto y {b} en su cateto adyacente
	tiene un hipotenusa con valor {c}
	""")