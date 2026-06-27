nombre_tienda01 = input("Introduce el nombre de la tienda 1: ")
nombre_tienda02 = input("Introduce el nombre de la tienda 2: ")

tienda01_sin_abreviatura = nombre_tienda01 #Esta variable la creer para printear quien es mejor al final del programa.
tienda02_sin_abreviatura = nombre_tienda02


abreviatura_tienda01 = nombre_tienda01[0:3] #Con esto seleccioné las 3 primeras letras.
abreviatura_tienda02 = nombre_tienda02[0:3]


tienda01 = abreviatura_tienda01.upper() #Una vez seleccionadas las 3 primeras letras las transformé a mayusculas.
tienda02 = abreviatura_tienda02.upper()

monto_tienda_01 = 0 #Este es el monto que iré actualizando a medida que pasan las rondas
monto_tienda_02 = 0


if tienda01 == tienda02: #Verifico si hay una igualdad de las 3 primeras letras de tienda 1 y tienda 2
    tienda02 = f"{tienda02}2" #En caso de que sean iguales, con las etiquetas dinamicas (Se parecen mucho a los props de React), a la tienda 2 le añado un 2 al final


print(f"{tienda01}: ${monto_tienda_01}") #Nuevamente uso las etiquetas dinamicas, para llamar las 3 letras de la respectiva tienda en mayuscula, agregué la variable del monto y muestro en consola
print(f"{tienda02}: ${monto_tienda_02}")

ronda = 1 #Partimos de la ronda 1

tienda_input1 = "tienda 1" #Esta variable,la cree para que no tuviera que crear 3 inputs para la tienda 1 y 3 para la tienda 2, y solo tuviera que reemplazar la variable
tienda_input2 = "tienda 2"

def inputs_tienda(tienda): #Cree una función que llama a los 3 inputs y recibe el argumento tienda(en este caso serán las variables tienda_input1 y tienda_input2)
        ins1_tienda = input(f"Ingresa una instrucción para la {tienda}: ") #Aqui se puede ver el llamado del argumento
        ins2_tienda = input(f"Ingresa una instrucción para la {tienda}: ") 
        ins3_tienda = input(f"Ingresa una instrucción para la {tienda}: ")



        return ins1_tienda, ins2_tienda, ins3_tienda #Retorno los 3 inputs
        


def separacion_lista(ins1, ins2, ins3): #Aquí entran las instrucciones que se le dio a la tienda para ser separadas y almacenarse en una variables
        separar1 = ins1.split(" ") #Separé las dos instrucciones con un .split
        separar2 = ins2.split(" ") 
        separar3 = ins3.split(" ") 
        
        return separar1, separar2, separar3 #Retorno cada instrucción como una lista de 2 elementos, para manejar el indice [0] y [1]


def validacion(lista): #Aquí comienza la validación de cada una de las listas
         
         valor1 = lista[0] #Esta variable almacena el elemento 1 de la lista con indice 0 
         valor2 = lista[1] #Esta variable almacena el elemento 2 de la lista con indice 1

         if len(lista) == 2: #Esto lo use al principio como medida preventiva, en caso de que el usuario introduce un solo elemento (Se que nos dijo en la ayudantía y por mail que el usuario siempre introducirá un input correcto, pero quería aprovechar de practicar  )
           if valor1 == "despacho": #Valido si el elemento 1 es igual a despacho
             if valor2 == "cerca": #Una vez se cumpla la condición de despacho, vamos evaluando el segundo elemento y devolvemos un numero según la tabla del PDF
                  return 1000 
             elif valor2 == "normal": 
                   return 5000 
             elif valor2 == "lejos": 
                   return 10000 
             
           if valor1 == "descuento": 
                 return -int(valor2) #Aquí lo que hice fue aplicar la teoría de -(+numero) = -numero, para hacer el descuento, con el int(transformo el string a un numero)
      
 
           if valor1.isdigit(): #El método .isdigit lo saqué de https://www.w3schools.com/python/ref_string_isdigit.asp para evaluar si el valor con indice 0 es un digito
                 valor1 = int(valor1) #En caso de que el valor 1 sea digito, se transforma a un número enteno, para manipularlo como tal.
                 if valor1 >= 10: #Este if, verifica si el valor 1 que ya fue transformado a un entero es mayor a 10
                       return (valor1 - 1) * int(valor2) #Aquí aplique la formula que se muestra en el pdf con (X-1) * Z
                 return valor1 * int(valor2) #En caso de que no sea una compra mayorista, se devuelve la multiplicación     
                                     


while monto_tienda_01 < 100_000 and monto_tienda_02 < 100_000: #Aquí entramos al loop hasta que una de las tiendas llegue a 100_000
            print(f"Ronda: {ronda}") #Se muestra la nueva ronda
            ronda += 1 #Aumentamos en uno la ronda, cada vez que empieza un nuevo ciclo
            
            ins1,ins2,ins3 = inputs_tienda(tienda_input1) #Llamamos a la función que contiene a los inputs, le coloco como argumento la variable con valor "tienda 1".

            lista1, lista2, lista3 = separacion_lista(ins1,ins2,ins3) #Aquí separamos las instruccciones en 3 listas 
            


            resultado1_tienda1 = validacion(lista1) #Las listas pasan a ser validadas y se almacenan los datos en su respectiva variable
            resultado2_tienda1 = validacion(lista2)
            resultado3_tienda1 = validacion(lista3)


            monto_tienda_01 += resultado1_tienda1 #Se suma la variable que contiene la lista ya validada
            monto_tienda_01 += resultado2_tienda1
            monto_tienda_01 += resultado3_tienda1



            ins1_tienda2,ins2_tienda2,ins3_tienda2 = inputs_tienda(tienda_input2) #Llamamos a la función que contiene a los inputs, le coloco como argumento la variable con valor "tienda 2".

             
            lista1_tienda2, lista2_tienda2, lista3_tienda2 = separacion_lista(ins1_tienda2,ins2_tienda2,ins3_tienda2) #Aquí separamos las instruccciones en 3 listas 


            resultado1_tienda2 = validacion(lista1_tienda2) #Las listas pasan a ser validadas y se almacenan los datos en su respectiva variable
            resultado2_tienda2 = validacion(lista2_tienda2)
            resultado3_tienda2 = validacion(lista3_tienda2)

            monto_tienda_02 += resultado1_tienda2 #Se suma la variable que contiene la lista ya validada
            monto_tienda_02 += resultado2_tienda2
            monto_tienda_02 += resultado3_tienda2



            print(f"{tienda01}: ${monto_tienda_01}") #Nuevamente uso las etiquetas dinamicas, para llamar las 3 letras de la respectiva tienda en mayuscula, agregué la variable del monto y muestro en consola
            print(f"{tienda02}: ${monto_tienda_02}")

            if monto_tienda_01 < 0: #Aquí evito que el monto de cada tienda no baje de 0, al final de cada ronda (Como se menciona en el mail)
                  monto_tienda_01 = 0

            if monto_tienda_02 < 0:
                  monto_tienda_02 = 0



if monto_tienda_01 < 100_000 and monto_tienda_02 >= 100_000: #Una vez la tienda 2 sea igual o mayor que 100_000, mostramos en consola que la tienda 1 es mejor
      print(f"{tienda01_sin_abreviatura} es mejor")
elif monto_tienda_01 >= 100_000 and monto_tienda_02 < 100_000: #Una vez la tienda 1 sea igual o mayor que 100_000, mostramos en consola que la tienda 2 es mejor
      print(f"{tienda02_sin_abreviatura} es mejor") 


