"""
El IMC resulta de la division de la masa del individuo (kilogramos) entre 
el cuadrado de la estatura (metros). El indice de masa corporal es un indicador del peso de una persona en relacion con su altura.

    (a) menor a 16: criterio de ingreso
    (b) 16 a 16.9: infrapeso
    (c) 17 a 18.4: bajo peso
    (d) 18.5 a 24.9: peso normal
    (e) 25 a 29.9: sobrepeso
    (f) 30 a 34.9: obesidad premorbida
    (g) 40 a 45: obesidad morbida
    (h) mayor a 45: obesidada hipermorbida

Escriba un programa que dado el peso de una persona en libras (1 libra = 0.453592 kg) y su estatura en centimetros, calcule su 
IMC e indique como salida el peso en kilogramos, el valor de IMC de la persona y la categoria en la cual fue clasificado.
"""
import math

masa_individuo = float(input("Ingresa la masa corporal en libras: ")) * 0.453592
estatura = float(input("Ingresa la estatura en centimetros: ")) / 100

IMC = masa_individuo / math.pow(estatura, 2)

if(IMC < 16):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: criterio de ingreso
    """)
elif(IMC >= 19 and IMC <= 16.9):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: infrapeso
    """)
elif(IMC >= 17 and IMC <= 18.4):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: bajo peso
    """)
elif (IMC >= 18.5 and IMC <= 24.9):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: peso normal
    """)
elif (IMC >= 25 and IMC <= 29.9):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: sobrepeso
    """)
elif (IMC >= 30 and IMC <= 34.9):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: obesidad promorbida
    """)
elif (IMC >= 40 and IMC <= 45):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: obesidad morbida
    """)
elif(IMC > 45):
    print(f"""
    El peso de la persona es de: {masa_individuo} kilogramos.
    El IMC es de {IMC}
    La persona tiene: obesidad hipermorbida
    """)
