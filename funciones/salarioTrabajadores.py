"""
Hacer un algoritmo que obtenga el salario neto de n trabajadores (n, se lee del teclado) de acuerdo con los siguientes puntos:

- Las 38 horas primeras semanales se cobran a la tarifa ordinaria (valor de la hora)
- Cualquier hora extra a 1.5 veces la tarifa ordinaria
- Las 50.000 pesetas están libres de impuestos; las siguientes 40.000 pesetas tienen un impuesto del 25 por 100 y las restantes del 45 por 100
"""

#Función que calcula salario bruto, salario neto, impuestos
#argumentos hora, tarifas
#devuelve salario bruto, impuestos, salario neto
def salarioImpuesto(h, t):
	sb= 0
	im= 0
	sn= 0
	
	if h <= 38:
		sb= h * t
	else:
		sb= 38 * t + (h - 38) * 1.5 * t
	
	if sb >= 50000:
		if sb <= 90000:
			im= (sb - 50000) * 0.25
		else:
			im= (40000 * 0.25) + (sb - 90000) * 0.45 
	
	sn= sb - im	
	return sb, im, sn
	
#**************************
#*** PROGRAMA PRINCIPAL ***
#**************************

salBruto= 0
impuestos=0 
salNeto= 0

n= int(input("Cuantos empleados?: "))
for i in range(1, n):
	nombre= input("Nombre del empleado?: ")
	horas= int(input("Horas?: "))
	tarifa= int(input("Valor de la hora?: "))
	
	#funcion calcula los salarios y los impuestos apartir de las horas y la tarifa (valor hora)
	[salBruto, impuestos, salNeto]= salarioImpuesto(horas, tarifa)
	
	nombre= nombre.upper()
	print("\n\nEl salario bruto de ", nombre, " es: $", salBruto)
	print("Los impuestos de ", nombre, " es: $", impuestos)
	print("El salario neto de ", nombre, " es: $", salNeto)
	print("-" * 10)
	
