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
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

# Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)
