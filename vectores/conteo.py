"""
En un proceso industrial son generados productos que contienen elementos los cuales son contados por la máquina. 
Construir un programa que vaya recibiendo ese listado de números y los separe por las cantidades que han sido 
pares e impares, asuma por facilidad que va ingresando el listado de números por teclado y que la cantidad de 
conteos es establecida por el usuario. Un ejemplo es presentado en la siguiente tabla.

------------------------------------------------
Entradas	Salidas
------------------------------------------------
Cantidad | Entrada de conteos	| Impares	| Pares
------------------------------------------------
cnt	     | Conteo	            | Impar[]	| Par[]
------------------------------------------------
3             5                   5	
              3	                  5, 3	
              8                   5, 3      8
""" 

import numpy as np

cnt= 0 #cuantos numeros el usuario va ingresar
conteo= 0 #cada numero del usuario
vecimp= [] #vector de impares 
vecpar= [] #vector de pares 
cntimp= 0 #cantidad de num imppares
cntpar= 0 #cantidad de num pares

cnt= int(input("Cantidad de números a ingresar: "))

vecimp= np.zeros(cnt)
vecpar= np.zeros(cnt)

for i in range(cnt):
  print("Ingrese el número ", i+1)
  conteo= int(input("? "))
  if conteo % 2 != 0: #si es par
    vecimp[cntimp]= conteo
    cntimp= cntimp  +1
  else:
    vecpar[cntpar]= conteo
    cntpar= cntpar  +1

print("Cantidad de números ingresados: ", cnt)
print("Números impares: ", vecimp[:cntimp]) #vecimp[:cntimp]: desde la pos 0 a la pos cntimp
print("Números pares: ", vecpar[:cntpar]) #vecimp[:cntimp]: desde la pos 0 a la pos cntimp
