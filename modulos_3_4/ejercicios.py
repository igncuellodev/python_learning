#Escribir un programa que pida los nombres de personas separados por un espacio

s1 = input("Intorduce los nombres de las personas:\n")

lista_nombres = s1.split(" ")

nombre1 = lista_nombres[0][0:3]
nombre2 = lista_nombres[1][0:3]

if nombre1 == nombre2:
    nombre2 = f"{nombre2}2"


nombres = nombre1.upper() + " " + nombre2.upper()



print(nombres)


#Ejercicio2

resultado = input("Ingrese la jugada: ")

resultado_upper = resultado.upper()



if resultado_upper == "SINGLE BULL":
    print(25)

elif resultado_upper == "DOUBLE BULL":
    print(50)

elif resultado_upper == "NULL":
    print(0)

else:
    separar = resultado.split(" ")
    numero1 = separar[0]
    numero2 = separar[1]
    suma = int(numero1) * int(numero2)
    print(suma)

