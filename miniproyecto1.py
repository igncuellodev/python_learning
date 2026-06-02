#Debe generar un numero de 1 a 100 aleatorio y debe guardarse
#El programa solicita el nombre del usuario y lo guarda
#

import random
numero_aleatorio = random.randint(1,100)
nombre_de_usuario = input("Introduce tú nombre:\n")
introducir_numero = int(input("Introduce un número para empezar a adivinar (Presiona 0, para terminar juego):\n"))
intentos_del_usuario = 0

if introducir_numero == 0:
    intentos_del_usuario = intentos_del_usuario + 1
    print("No lo lograste a pesar de intentar " + str(intentos_del_usuario) + " veces")


else:
    print("Ese no es el numero")