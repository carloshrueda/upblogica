# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:43:40 2016

@author: Carlos Rueda
"""

"""
hacer un programa que use vectores y diga si un texto es un palíndrome 
(texto que se lee igual al derecho y al revés)
"""

def esPalindorme(cad):
    """ Función que evalúa que un texto es palindrome """
    
    #las cadenas se puden acceder por indice como los vectores
    ultpos= len(cad) #ultima posición del vector
    
    espal= True #Suponemos al principio que es palindrome
    for i in range(ultpos // 2):
        ultpos = ultpos - 1
        if cad[i] != cad[ultpos]:
            #si no es igual la primera y la ultima posicion
            #no es palindrome
            espal= False
            break #sino es palindrome no es necesario seguir analizando
            
    return espal

def main():
    texto= input("Ingrese el texto a analisar: ")
    
    print("\n")
    if esPalindorme(texto) == True:
        print("El texto ES palíndrome :)")
    else:
        print("El texto NO ES palíndrome :(")

#**** PROGRAMA PRINCIPAL ****
main()
