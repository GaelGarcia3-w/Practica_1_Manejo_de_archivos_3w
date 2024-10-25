
# Programa 1

print(" ")

print("Edgar Gael Garcia Camacho 3w:Practica #1 Manejo_de_archivos")

print()

archivo = open("Pollos.txt.txt","r")#Aquí se agreaga el archivo del texto.

print(archivo.readable())#Este se usa para que el programa te identifique si es verdadero o falso.
print()
contenido = archivo.read()#Este se usa para imprimir el texto del archivo.
print()
print(contenido)#Para que el texto impreso se ejecute en la pantalla.

archivo.close()#Para que se cierre el archivo automaticamente.