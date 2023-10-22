"""
Escribir un programa que reciba como entrada los coeficientes A, B y C de una
ecuacion de segundo grado, e imprima por pantalla los valores de x. Asumir que
la ecuacion siempre tiene solucion en numeros reales. Recordar que la solucion
de una ecuacion de segundo grado viene dada por:

x = -b -+ sqrt(b² - 4ac) / 2a
"""
import math

a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))
c = float(input("Ingresar el valor de c: "))

try:
    x1 = -b + (math.sqrt(b*b - 4 * (a * c))) / (2 * a)
    x2 = -b - (math.sqrt(b*b - 4 * (a * c))) / (2 * a)

    print(f"El valor de x1 = {x1}")
    print(f"El valor de x2 = {x2}")
except:
    print("Error, no se puede calcular la raiz cuadrada de un numero negativo.")

