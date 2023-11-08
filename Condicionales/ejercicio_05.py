"""
Escribir un programa que reciba como entrada un numero entre 1 y 12 e imprima el nombre del mes
correspondiente. Tomar en cuenta errores en la entrada.
"""

numero_dia: int = int(input("Ingresa un numero entre 1 y 12 correspondiente a un mes: "))

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

if(numero_dia in meses.keys()):
    print(meses.get(numero_dia))
else:
    print("Numero incorrecto")