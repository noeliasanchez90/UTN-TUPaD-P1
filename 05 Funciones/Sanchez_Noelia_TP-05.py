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




# Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área
# del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

# Definición de funciones
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El área del circulo es {area: .2f}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es {perimetro:.2f}")

# Programa principal
radio = float(input("ingrese el radio del círculo: "))
calcular_area_circulo(radio)
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




# Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la
# tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{i} x {numero} = {resultado} ")
    
# Programa principal
numero = int(input("ingrese un numero del cual quiere conocer su tabla de multiplicar: "))
tabla_multiplicar(numero)




# Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una
# tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Definición de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = None
        
    else:
        division = a / b 
    return (suma, resta, multiplicacion, division) #tupla

# Programa principal
a = int(input("ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))

resultado = operaciones_basicas(a, b)
print(f"{a} + {b} = {resultado[0]}")
print(f"{a} - {b} = {resultado[1]}")
print(f"{a} * {b} = {resultado[2]}")
if resultado[3] is not None:
    print(f"{a} / {b} = {resultado[3]:.2f}")
else:
    print("División no válida (división por cero).")




# Ejercicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en 
# metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar
# el resultado con dos decimales.

# Definición de funciones
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

imc = calcular_imc(peso, altura)
print(f"El IMC es = {imc:.2f}")




# Ejercicio 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando
# la función.


# Definición de funciones
def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Programa principal

temp = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{temp} equivalen a {celsius_a_fahrenheit(temp):.2f} grados Fahrenheit")




# Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva 
# el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de funciones

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("ingrese el primer número: "))
b = float(input("ingrese el segundo número: "))
c = float(input("ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio entre {a}, {b} y {c} es {promedio:.2f}")