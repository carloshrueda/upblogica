#función factorial
def factorial(x):
	f=1
	if x > 0:
		for i in range(1, x+1):
			f = f * i
	elif x < 0:
		#no existe factorial de un número negativo
		f= -1
	
	return f

#función combinatoria
def combinatoria(n, m):
	if m >= n:
		return factorial(m) / ( factorial(n) * factorial(m - n) )
	else:
		#no existe combinatoria para n < m
		return -1

#*** PROGRAMA PRINCIPAL ***
a= int(input("ingrese el valor de n?: "))
b= int(input("ingrese el valor de m?: "))

resultado= combinatoria(a, b)

if resultado != -1:
	#str(num): str() es una función que combierte el número (num) en texto
	print("\nEl resultado de " + str(a) + "C" + str(b) + "= ", resultado)
else:
	print("\n>>>Error. Datos inválidos")
	
