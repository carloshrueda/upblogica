#este es un ejemplo del uso de funciones en python en el 
#calculo de la suma de dos numeros

#funcion suma
def suma(a, b):
	c= a + b
	return c
	
#*** PROGRAMA PRINCIPAL ***
n1= int(input("Introduzca un numero: "))
n2= int(input("Introduzca otro numero: "))

resultado= suma(n1, n2)
print("\n" + str(n1) + "+" + str(n2) + "= ", resultado)

