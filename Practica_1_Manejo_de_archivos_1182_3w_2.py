# Programa para abrir un archivo en una ubicación diferente
archivo = open("Pollos.txt.txt", "r")#Se abre y selecciona el archivo que se quiere imprimir el texto.
print(archivo.read())#Se imprime el archivo
archivo.close()#Se cierra el archivo.