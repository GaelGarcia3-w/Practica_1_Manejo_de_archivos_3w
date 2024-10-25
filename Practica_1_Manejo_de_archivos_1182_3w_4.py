# Programa para anexar contenido a un archivo existente
archivo = open("Pollos.txt.txt", "a")#Se abre el archivo.
archivo.write("Pollos a bajo precio!\n")#Se agrega la opcin "write" para agregar o anexar otra palabra.
archivo.close()#Se cierra el archivo.
