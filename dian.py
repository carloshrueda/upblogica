# -*- coding: utf-8 -*-
"""
La Dian está interesada en saber el uso de los nombres en Colombía, para esto 
se ha de desarrollar un programa en Python que ingrese el listado de los 
primeros y segundos nombres de los colombianos y se debe sacar la tabla con 
los nombres ordenados ascendentemente y al frente su frecuencia de aparición, 
así como un diagrama de barra con la frecuencia de los nombres. 
Los nombres serán ingresados hasta que se ingrese la palabra FIN.

Ejemplo:

Entrada:

Carlos   Oscar   Carlos   Maria   Diana  Maria  Carlos FIN

Salida:
Tablas de frecuencia
--------------------------
Carlos : 3
Diana  : 1
Maria   : 2
Oscar   : 1

Diagrama de frecuencia:
------------------------------
Carlos : ***
Diana  : *
Maria  : **
Oscar  : *
"""

lstNombres = []
lstFrecNom = []

nombre = ""
while nombre != "FIN":
    nombre = input("NOMBRE?: ").upper()

    swExiste = False
    for i in range(len(lstNombres)):
        if nombre == lstNombres[i]:
            swExiste = True
            lstFrecNom[i] += 1

    if not swExiste:
        lstNombres.append(nombre)
        lstFrecNom.append(1)


print("\nFRECUENCIA")
print("-" * 15)
cantnombres = len(lstNombres) - 1
for i in range(cantnombres):
    print(lstNombres[i], " = ", lstFrecNom[i])

sumfrec = sum(lstFrecNom)
print("-" * 15)
print("Total Frecuencia: ", sumfrec)
print("Total Nombres: ", cantnombres)


# Para la frecuencia:
# la cantidad maxima de * son 20
# entonces =>
# freci / sumfrec * 20
print("\n\nDIAGRAMA")
print("-" * 15)
print("*FRECUENCIA MAX\t( 100.0 %)\t: ", "*" * 20)
for i in range(len(lstNombres) - 1):
    porcentaje = round(lstFrecNom[i] / sumfrec, 3)
    cantasc = int(porcentaje * 20)
    print(lstNombres[i], "\t\t(", porcentaje * 100, "%)\t: ", ("*" * cantasc))
