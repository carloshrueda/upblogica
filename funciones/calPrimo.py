"""
este programa ejemplifica el uso de funciones
El programa muestra varias formas de calcular si un numero es primo o no
"""

#funcion que imprime el menu
#la funcion no recive ningun parametro
def menu():
	print("\n" * 50) #varios cambios de lineas con el fin de limpiar la pantalla
	print("\t\t*** MENU ***\n")
	print("\t1. Primo 1")
	print("\t2. Primo 2")
	print("\t3. Primo 3")
	print("\t0. Salir")

#funcion opcion
#esta funcion muestra el menu, captura y valida la opcion del usuario
#recibe el numero menor, el mayor del menu y la opcion de salida (debe estar en el rango)
#devuelve una opcion valida del usuario
def opcion(min, max, salida):
	opcion= -1
	
	menu() #dibuja el menu
	opcion= int(input("\n\t-> Opcion?: ")) #recibe una opcion del usuario
	while (opcion < min) or (opcion > max):
		print("\n\t>>> Error. Opcion invalida.")
		print("\t    Presione una tecla para continuar ...")
		input() #detiene la ejecucion del programa hasta que se presione una tecla
		
		menu() #dibuja el menu
		opcion= int(input("\n\t-> Opcion?: ")) #recibe una opcion del usuario
	
	return opcion
		
#funcion submenu
#esta funcion muestra el encabezado de un submenu
#no recive ningun parametro (argumento)
#no devuelve ningun valor
def submenu(titulo, mensaje):
	print("\n" * 50) #varios cambios de lineas con el fin de limpiar la pantalla
	#texto.upper() : combierte todo el texto en MAYUSCULAS
	print("\t\t*** " + titulo.upper() + " ***\n")
	
	#el mensaje
	if mensaje != "":
		mensaje= "| " + mensaje + " |"
		lenmsj= len(mensaje)
		print("\t" + "-" * lenmsj)
		print("\t" + mensaje)
		print("\t" + "-" * lenmsj)
	
#funcion capturaOpcion
#funcion captura la opcion del usuario
def capturaOpcion(titulo, mensaje):
	opc = -1
	submenu(titulo, mensaje)
	
	opc = int(input("\n\tIngrese un numero entero positivo > 1: "))
	return opc
	

#funcion que calcula si un numero es primo o no
#recibe como argumento (parametro) un numero
#divide este numero entre 2 hasta num-1
#si el residuo de alguna division anterior es cero no es primo
#sino es primo
#devuelve la respuesta y la cantidad de comparaciones
def fPrimo1(n):
	respuesta = ""
	comparaciones = 0
	
	if n>1:
		esprimo= True
		for i in range(2, n):
			comparaciones += 1
			if n % i == 0:
				#es un divisor
				esprimo = False
				break
		
		if esprimo:
			respuesta= "Es primo"
		else:
			respuesta= "No es primo"
			
	else:
		respuesta = "Error. Numero invalido."
	
	return respuesta, comparaciones
	
	
#funcion que calcula si un numero es primo o no
#recibe como argumento (parametro) un numero
#divide este numero entre 2, 3 y los impares hasta num-1
#si el residuo de alguna division anterior es cero no es primo
#sino es primo
#devuelve la respuesta y la cantidad de comparaciones
def fPrimo2(n):
	respuesta = ""
	comparaciones = 0
	
	if n % 2 == 0:
		if n != 2:
			respuesta = "No es primo"
		else:
			respuesta = "Es primo"
			
		comparaciones = 2
		
	elif n>2:
		esprimo= True
		comparaciones = 1
		for i in range(3, n, 2):
			comparaciones += 1
			if n % i == 0:
				#es un divisor
				esprimo = False
				break
			
		if esprimo:
			respuesta= "Es primo"
		else:
			respuesta= "No es primo"
		
	else:
		respuesta = "Error. Numero invalido."
	
	return respuesta, comparaciones

#funcion que calcula si un numero es primo o no
#recibe como argumento (parametro) un numero
#descarta multiplos de 2, 3, 5 y divide impares hasta raiz(n)
#devuelve la respuesta y la cantidad de comparaciones
def fPrimo3(n):
	respuesta = ""
	comparaciones = 0
	
	if n % 2 == 0:
		if n != 2:
			respuesta = "No es primo"
		else:
			respuesta = "Es primo"
			
		comparaciones = 2
		
	elif n % 3 == 0:
		if n != 3:
			respuesta = "No es primo"
		else:
			respuesta = "Es primo"
			
		comparaciones = 3
		
	elif n % 5 == 0:
		if n != 5:
			respuesta = "No es primo"
		else:
			respuesta = "Es primo"
			
		comparaciones = 4
		
	elif n>2:
		esprimo= True
		comparaciones = 3
		#la funcion round() redondea un numero al entero superior
		#la funcion int convierte el numero float que devuelve round() a entero
		raiz = int(round(n ** (0.5))) 
		for i in range(7, raiz + 1, 2):
			comparaciones += 1
			if n % i == 0:
				#es un divisor
				esprimo = False
				break
			
		if esprimo:
			respuesta= "Es primo"
		else:
			respuesta= "No es primo"
		
	else:
		print("\n\t>>> Error. Numero invalido.")
	
	return respuesta, comparaciones


def fSalida():
	submenu("Salida", "") #no importa enviarlo en minuscula submenu la convierte
	
	print("\n\t-> Gracias por usarnos. Adios.  ")
	print("\t   Presione cualquier tecla para terminar ...")
	input()
	print("\n" * 50) #varios cambios de lineas con el fin de limpiar la pantalla



#*************************
#*** PROGRAMA PRINCIAL ***
#*************************

resultado = -1
comparaciones = -1
num = -1
op= -1

while op != 0:
	op = opcion(0, 5, 0) #llama a la funcion opcion
	
	if op == 1:
		## funcion Suma
		num= capturaOpcion("primo 1", "Divide el numero desde 2 hasta n-1")
		(resultado, comparaciones) = fPrimo1(num)
		
	elif op == 2:
		## funcion Resta
		num= capturaOpcion("primo 2", "Divide el numero entre 2 y los impares desde 3 hasta n-1")
		(resultado, comparaciones) = fPrimo2(num)
		
	elif op == 3:
		## funcion Multiplicacion
		num= capturaOpcion("primo 3", "Descarta multiplos de 2, 3, 5 y divide impares hasta raiz(n)")
		(resultado, comparaciones) = fPrimo3(num)
		
	else:
		## funcion Salida
		fSalida()
		break
		
	print("\n\t-> El numero " + str(num) + " " +resultado)
	print("\t-> Cantidad de comparaciones: ",comparaciones)
	print("\n\t   Presione cualquier tecla para continuar ...")
	input()
