# Practica_1_Manejo_de_archivos_3w
Edgar Gael Garcia Camacho 3-W
# Programa 1

print(" ")

print("Edgar Gael Garcia Camacho 3w:Practica #1 Manejo_de_archivos")

print()

archivo = open("Los pollos.txt.txt","r")#Aquí se agreaga el archivo del texto.

print(archivo.readable())#Este se usa para que el programa te identifique si es verdadero o falso.

contenido = archivo.read()#Este se usa para imprimir el texto del archivo.

print(contenido)#Para que el texto impreso se ejecute en la pantalla.

archivo.close()#Para que se cierre el archivo automaticamente.

![image](https://github.com/user-attachments/assets/8a9e0776-2691-4231-8965-1a5d300b63fc)

![image](https://github.com/user-attachments/assets/d11aebcf-0ec1-4070-8ed7-51deaa41b6cd)

# Programa 2

archivo = open("Pollos.txt.txt", "r")#Se abre y selecciona el archivo que se quiere imprimir el texto.

print(archivo.read())#Se imprime el archivo

archivo.close()#Se cierra el archivo.

![image](https://github.com/user-attachments/assets/4be8dc8d-869b-401a-afd5-4e7b03a363af)

![image](https://github.com/user-attachments/assets/b5570a1c-ae8e-4dae-acd1-37607879994c)

# Practica 3

archivo = open("Pollos.txt.txt", "r")#Se abre y se selleciona el archivo.

print(archivo.read(18))#Se imprime el archivo con el numero de caracteres que se desea imprimir.

archivo.close()#Se cierra el archivo.

![image](https://github.com/user-attachments/assets/e5bcea51-ebdd-43d7-8fd9-0d7cebfb642e)

![image](https://github.com/user-attachments/assets/b43b9583-341f-4e2d-b059-1b69480eec32)

# Programa 4

archivo = open("Pollos.txt.txt", "a")#Se abre el archivo.

archivo.write("Pollos a bajo precio!\n")#Se agrega la opcin "write" para agregar o anexar otra palabra.

archivo.close()#Se cierra el archivo.

![image](https://github.com/user-attachments/assets/2dc6b937-481b-4b12-8be7-1454b8f464cb)

![image](https://github.com/user-attachments/assets/587df32e-6fe8-4e90-857c-10ffd98d81cd)

![image](https://github.com/user-attachments/assets/c228a7b7-2bb6-47d7-ae3a-8b33ff5f2509)

# Programa 5

archivo = open("Pollos.txt.txt", "w")#Se abre el archivo.

archivo.write("Combo 1!\n")#Se sobrescibe una palabra en el archivo.

archivo.close()#Se cierra el archivo.

![image](https://github.com/user-attachments/assets/4b296a6c-d6ce-484c-9841-c125a8d9c25b)

![image](https://github.com/user-attachments/assets/480c0222-e19b-46ab-9abf-e999dadc45c9)

# Programa 6

archivo = open("Pollos.txt.txt", "w")  #Se abre el rchivo

archivo.write("Este archivo será eliminado.\n")# Se agrega el mensaje de este archivo sera eliminado.

archivo.close()# Se cierra el archivo.

![image](https://github.com/user-attachments/assets/8f95dd92-73fb-4985-b1ae-56a055f139fe)

# Programa 7

print("Para comprobar si el archivo existe, usa 'os.path.exists(\"Pollos.txt.txt\")'.")

![image](https://github.com/user-attachments/assets/b46f7c02-8956-4b2a-8469-6439044c169f)

![image](https://github.com/user-attachments/assets/0b8fad41-8be0-43e4-b149-6e7025dd8d54)

# Programa 8

print("Para eliminar la carpeta, usa 'os.rmdir(\"myfolder\")'.")

![image](https://github.com/user-attachments/assets/97c4c34c-c41f-4701-98dd-ebc2a230d345)

![image](https://github.com/user-attachments/assets/fa5ab74b-d94b-4981-ba40-bb53e5b84579)

# Programa 9

archivo = open("Pollos.txt.txt", "w")  

archivo.write("Este archivo será eliminado.\n")

archivo.close()

#Simulación de eliminación (no funcional)

print("Para eliminar el archivo, usa 'os.remove(\"Pollos.txt.txt\")'.")

![image](https://github.com/user-attachments/assets/93c829c6-dd4b-4c2c-a3db-366e492a2b59)

![image](https://github.com/user-attachments/assets/8237fb16-7403-4245-b1fa-a0f308599643)





