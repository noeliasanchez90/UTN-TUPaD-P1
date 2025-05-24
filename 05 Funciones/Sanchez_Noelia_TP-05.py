# Ejercicio 1: 1. Crear una función llamada imprimir_hola_mundo que imprima porpantalla el mensaje:
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definición de funciones
def imprimir_hola_mundo():
    return print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()




# Ejercicio 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un 
# saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Definición de funciones
# def saludar_usuario(nombre):
   # return print(f"Hola {nombre}!")

# Programa principal
#nombre = input("Ingrese su nombre: ")
# saludar_usuario(nombre)




# Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro
# parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario
# y llamar a esta función con los valores ingresados.

# Definición de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)