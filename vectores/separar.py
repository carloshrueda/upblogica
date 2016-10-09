# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:52:14 2016

@author: Carlos Rueda
"""

"""
Hacer un programa que reciba un listado de palabras que se ingresan separadas por comas y las separe 
con saltos de línea y las almacene en un arreglo. 

Ejemplo:

Entrada: UPB,Ingeniería,Algoritmos,Carlos,Rueda

Salida: 
UPB 
Ingeniería 
Algoritmos 
Carlos Rueda
"""

import numpy as np

def esvacio(txt):
    """ Función que evalúa si un texto está vacío (True) o no (False) """
    lenstr= len(txt)
    if lenstr > 0:
        return False #no esta vacio
    else:
        return True

def main():
    """ Función principal del programa """
    
    texto= input("Texto de palabras separadas por coma (,):  ")

    if esvacio(texto) != True:
        #si el texto no es vacio
        
        #la función split separa el texto por un patron
        #separamos el texto por el patron "," e insertamos el resultado
        #en una vector de palabras
        vpal= np.array( [ texto.split(',') ] )
        
        #Recorremos el vector de palabras y se imprime cada una
        print("\nPalabras: ")
        for pal in vpal[0]:
            print("\t", pal)


#******** PROGRAMA PRINCIPAL ***********
main()  

