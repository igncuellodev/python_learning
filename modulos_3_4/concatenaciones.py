#def juntar_letras(a, b):
#    return a[4] + b[2]
#
#resultado = juntar_letras("Los datos", "Móvil")
#print(resultado)



#def largo_texto():
#    texto1 = input("Introduce una palabra:\n")
#    texto2 = input("Introduce otra palabra:\n")
#
#    print(len(texto1))
#    print(len(texto2))
#
#
#largo_texto()
#

#lista = ["Ignacio", "Pedro", "Juan", "Agustin"]
#fin = "Fin"
#while True:
#    
#    nuevo_nombre = input("Introduce otro nombre:\n")
#
#    if nuevo_nombre == fin:
#        print(lista[:-1])
#        break
#
#    elif nuevo_nombre.isalpha():
#        lista.append(nuevo_nombre)
#        print(f"¡Agregado! Lista actual: {lista}")
#
#    else:
#        print("Debes introducir un nombre, intentalo de nuevo")

l = ["Hugo", "Paco", "Luis"]
l[0] = l[1]
l[1] = l[0]
for t in l:
    print(t)