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


#*** PROGRAMA PRINCIPAL ***
n= int(input("ingrese un numero entero positivo: "))


resultado= factorial(n)

if resultado != -1:
	#str(num): str() es una función que combierte el número (num) en texto
	print("\nEl resultado de " + str(n) + "!= ", resultado)
else:
	print("\n>>>Error. Datos inválidos")
	
