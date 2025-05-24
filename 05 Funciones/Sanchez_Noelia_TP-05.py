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
#def informacion_personal(nombre, apellido, edad, residencia):
    #return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
# Programa principal
#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su residencia: ")

#informacion_personal(nombre, apellido, edad, residencia)




# Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área
# del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

# Definición de funciones
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
   # print(f"El área del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
  #  print(f"El perimetro del circulo es {perimetro}")

# Programa principal
radio = float(input("ingrese el radio del círculo: "))
# calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)



# Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y
# devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta 
# función.

# Definición de funciones
def segundos_a_horas(seg):
    horas = seg / 3600
    print(f"{seg} segundos equivalen a {horas:.2f} horas")

# Programa principal
segundos = int(input("ingrese los segundos: "))
segundos_a_horas(segundos)