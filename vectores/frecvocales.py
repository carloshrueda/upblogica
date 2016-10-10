# -*- coding: utf-8 -*-
"""
Hacer un programa que lea un texto y cuente la cantidad de vocales que hay. 
Ejemplo:

Entrada: Universidad Pontificia Bolivariana

Salida: 

A: 5
E: 1
I: 7
O: 2
U: 1
"""

import numpy as np

# vector de vocales
vvoc = np.array(['A', 'E', 'I', 'O', 'U'])
# vector de frecuencias de vocales
vfvoc = np.zeros(5)

texto = input("Ingrese el texto a analizar?: ")
tamtex = len(texto)

# Calcular la frecuencia de las vocales
for i in range(tamtex):
    # Convierto la letra en mayuscula
    letra = texto[i].upper()

    for j in range(len(vvoc)):
        if letra == vvoc[j]:
            # letra es igual a una vocal aumenta la frecuencia de esa vocal
            vfvoc[j] += 1
            break

# imprimir la frecuencia de vocales
for i in range(5):
    print(vvoc[i], ":", vfvoc[i])
