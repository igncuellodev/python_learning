archivo = open("archivo_ejemplo2.csv", "w" , encoding="UTF-8")

archivo_en_lineas = archivo.readlines()

numero_de_clientes = len(archivo_en_lineas)

matriz_de_datos = []


for linea in archivo_en_lineas:
	linea = linea.strip()
	fila = linea.split(";")
	matriz_de_datos.append(fila)

print(matriz_de_datos)

