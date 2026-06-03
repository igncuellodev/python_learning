import random
numero_random = random.randint(1,100)
print(numero_random)
nombre_user = input("Dinos tu nombre, antes de empezar:\n")
user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))
intentos = 0

while user_num != numero_random:

        #Fin del juego
        if user_num == 0:
            print("No lo lograste a pesar de tratar " + str(intentos) + " veces" ".Mas suerte para otra vez")
            break
        #Fin del juego




        #Intervalo de 5
        if user_num > numero_random and user_num - numero_random <= 5:
            intentos = intentos + 1
            print("Sorry " + nombre_user + ", ese no es pero estas a una distancia menor a 5")
            user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))

        elif user_num < numero_random and numero_random - user_num <= 5:
              intentos = intentos + 1
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia menor a 5")
              user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))

        #Intervalo de 5


        #Intervalo 10
        elif user_num > numero_random and user_num - numero_random <= 10:
              intentos = intentos + 1
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 5 y menor que 10")
              user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))


        elif user_num < numero_random and numero_random - user_num <= 10:
              intentos = intentos + 1
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 5 y menor que 10")
              user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))
      #Intervalo 10

      #Intervalo 20

        elif user_num > numero_random and user_num - numero_random <= 20:
            intentos = intentos + 1
            print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 10 y menor que 20")
            user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))

        elif user_num < numero_random and numero_random - user_num <= 20:
          intentos = intentos + 1
          print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 10 y menor que 20")
          user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))

      #Intervalo 20


      #Intervalo 20 o más
        elif user_num > numero_random and user_num - numero_random >= 20:
              intentos = intentos + 1
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 20")
              user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))
        elif user_num < numero_random and numero_random - user_num >= 20:
              intentos = intentos + 1
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 20")
              user_num = int(input("Ingresa el numero que crees que es (0 para parar):\n"))





if user_num == numero_random:
       intentos = intentos + 1
       print("Felicitaciones " + nombre_user + ", lo lograste en " + str(intentos) + " intentos")