# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:52:14 2016

@author: Carlos Rueda
"""
"""
Hacer un programa que reciba una lista de n números enteros definida por 
el usuario y los clasifique en tres arreglos: Un vector de números 
múltiplos de 5, otro vector de números múltiplos de 3 y otro vector con 
el resto de números. Un número puede estar en las dos primeras listas 
generadas. El programa debe imprimir las cuatros listas: La de entrada 
y las de listas de salida.
"""

import numpy as np

def main():
    n= int(input("Cuantos numeros va a ingresar: "))
    
    vmul5= np.zeros(n)
    vmul3= np.zeros(n)
    votros= np.zeros(n)
    
    cntmul5= 0
    cntmul3= 0
    cntotros= 0
    
    #Captura de numero y llenado de vectores
    for i in range(n):
        print("Ingrese el numero: ", i+1)
        num= int(input("? "))
        
        if (num % 3==0) or (num % 5==0):
            #Si es multiplo de 3 o de 5
            if (num%3 == 0):
                vmul3[cntmul3]= num #editar la pos cntmul3 con el valor de num
                cntmul3 += 1 #se incrementa en 1 el valor 
            if (num%5 == 0):
                vmul5[cntmul5]= num #editar la pos cntmul5 con el valor de num
                cntmul5 += 1 #se incrementa en 1 el valor 
        else:
            votros[cntotros]= num #editar la pos cntotros con el valor de num
            cntotros += 1 #se incrementa en 1 el valor 
    
    #Mostrar resultados en pantalla
    print("\nCantidad de numeros ingresados: ", n)
    print("Cantidad de multiplos de 3: ", cntmul3)
    #Se imprime el vector 0 ... cntmul3 : [:cntmul3]
    print("Multiplos de 3: ", vmul3[:cntmul3])
    
    print("\nCantidad de multiplos de 5: ", cntmul5)
    #Se imprime el vector 0 ... :cntmul5 [:cntmul5]
    print("Multiplos de 5: ", vmul5[:cntmul5])
    
    print("\nCantidad de otros numeros: ", cntotros)
    #Se imprime el vector 0 ... :cntmul5 [:cntmul5]
    print("Otros numeros: ", votros[:cntotros])


#*** Programa principal
main()