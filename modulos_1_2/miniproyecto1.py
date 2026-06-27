import random
numero_random = random.randint(1,100)
#print(numero_random) #Este print lo hice para printear en consola el numero aleatorio y testear.
nombre_user = input("Dinos tu nombre, antes de empezar:\n")
user_num = int(input("Ingresa el número que crees que es (0 para parar):\n"))
intentos = 0

while user_num != numero_random:

        #Fin del juego
        if user_num == 0:
            print("No lo lograste a pesar de tratar " + str(intentos) + " veces" ".Mas suerte para otra vez")
            break
        #Fin del juego




        #Aquí comienza el Intervalo de 5
        if user_num > numero_random and user_num - numero_random <= 5: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
            intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
            print("Sorry " + nombre_user + ", ese no es pero estas a una distancia menor a 5")


        elif user_num < numero_random and numero_random - user_num <= 5:#En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
              intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia menor a 5")
      

        #Aquí termina el Intervalo de 5


        #Aquí comienza el Intervalo 10
        elif user_num > numero_random and user_num - numero_random <= 10: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
              intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 5 y menor que 10")
      


        elif user_num < numero_random and numero_random - user_num <= 10: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
              intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 5 y menor que 10")

      #Aquí termina el Intervalo 10

      #Aquí comienza el Intervalo 20

        elif user_num > numero_random and user_num - numero_random <= 20: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
            intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
            print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 10 y menor que 20")


        elif user_num < numero_random and numero_random - user_num <= 20: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
          intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
          print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 10 y menor que 20")
          

      #Aquí termina el Intervalo 20


      #Aquí comienza el Intervalo 20 o más
        elif user_num > numero_random and user_num - numero_random >= 20: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
              intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 20")

        elif user_num < numero_random and numero_random - user_num >= 20: #En estas comparaciones estoy usando el ->and<- para que ambas condiciones se cumplan :)
              intentos += 1 #Antes había colocado intento = intentos + 1 y en la ayudantía vimos el x += y que es lo mismo.
              print("Sorry " + nombre_user + ", ese no es pero estas a una distancia mayor a 20")
      
      
        user_num = int(input("Ingresa el número que crees que es (0 para parar):\n")) #Al principio, había puesto esta variable en cada uno de los elifs, y el ayudante fernando, me recomendó que lo colocara al final de toda la cadena.





if user_num == numero_random:
       intentos += 1
       print("Felicitaciones " + nombre_user + ", lo lograste en " + str(intentos) + " intentos")