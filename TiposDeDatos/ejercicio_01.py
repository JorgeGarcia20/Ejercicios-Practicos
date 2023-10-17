"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas
y el coste por hora. Después debe mostrar por pantalla la paga total correspondiente.
"""

horas = float(input("Ingresa el numero de horas laboradas: "))
coste_hora = float(input("Ingresa el conste por hora: "))

paga_total = horas * coste_hora

print(f'El usuario trabajo {horas} horas las cuales son pagadas a {coste_hora} pesos por hora, en total el usuario gano: {paga_total} pesos')