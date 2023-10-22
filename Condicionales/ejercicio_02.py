"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
ingresos iguales o superiores a 500$ mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
tiene que atributar o no.
"""

nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
ingresos = float(input("Ingresa los ingresos mensuales: "))

if edad < 16 or ingresos < 500:
    print(f"Lo sentimos {nombre}, no puedes tributar.")
else:
    print(f"{nombre} ya puedes tributar.")
