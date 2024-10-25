# Programa para eliminar un archivo (sin usar os, no se puede hacer realmente)
archivo = open("Pollos.txt.txt", "w")  #Se abre el rchivo
archivo.write("Este archivo será eliminado.\n")# Se agrega el mensaje de este archivo sera eliminado.
archivo.close()# Se cierra el archivo.