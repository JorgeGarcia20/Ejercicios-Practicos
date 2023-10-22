"""
Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logistica les cobra por peso de
cada paquete asi que deben calcular el peso de los payasos y muñecas que saldran
en cada paquete a demanda. Cada payaso tiene un peso de 112 g y cada muñeca 75g.
Escribe un programa que lea el numero de payasos y muñecas vendidos en el ultimo
pedido y calcule el peso total del paquete que será enviado.
"""

numero_payasos = int(input("Ingresa el numero de payasos a enviar: "))
numero_muñecas = int(input("Ingresa el numero de muñecas a enviar: "))
peso_por_payaso = 112
peso_por_muñeca = 75
peso_paquete = (numero_payasos * peso_por_payaso) + (numero_muñecas * peso_por_muñeca)

print(f"Se enviaran {numero_payasos} payasos y {numero_muñecas} muñecas, el paquete tendra un peso de {peso_paquete} g")
