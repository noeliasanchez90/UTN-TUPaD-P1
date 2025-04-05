#Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá 
#mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Por favor, ingrese su edad: "))
# Si edad es mayor o igal que 18, imprimir "Es mayor de edad"
if edad >= 18:
    print("Es mayor de edad")



# Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por 
# pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota=int(input("Ingrese su nota: "))
# Si la nota ingresada es mayor que 6, imprimir "Aprobado"
if nota >= 6:
    print("Aprobado")
# En cualquier otro caso, imprimir "Desaprobado""
else:
    print("Desaprobado")



# Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar 
# si un número es par o impar.

num_par=int(input("Por favor, ingrese un número par: "))
# Si al dividir num_par por 2 el resto es igaul a 0, imprimir "Ha ingresado un número par"
if num_par % 2 == 0:
    print("Ha ingresado un número par")
# Si no, si el resto es distinto de cero, imprimir "Por favor, ingrese un número par"
else:
    print("Por favor, ingrese un número par")



# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes 
# categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

Edad=int(input("Por favor, ingrese su edad: "))
# Determinar la categoría según la edad
if Edad < 12:
    categoria = "Niño/a"
elif 12 <= Edad < 18:
    categoria = "Adolecente"
elif 18 <= Edad < 30:
    categoria = "Adulto/a joven"
else :
    categoria = "Adulto/a"
# Imprimir la categoría
print(f"Tu categoría es: {categoria}")



#Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una 
# contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 
# 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que 
# tiene un iterable tal como una lista o un string.

contraseña=input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
# Calculo la cantidad de caracteres ingresados con la función len()
cantidad_caracteres = len(contraseña)
# Si la cantidad de caracteres ingresados esta entre 8 y 14, imprimir "Ha ingresado una contraseña correcta"
if 8 <= cantidad_caracteres <= 14:
    print("Ha ingresado una contraseña correcta")
# Si la cantidad de caracteres ingresados es menor que 8 o ayor que 14, imprimir "Por favor, ingrese una contraseña de 
# entre 8 y 14 caracteres"
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#Ejercicio 6: escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las 
# compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Creo una lista con 50 números entre 1 y 100 elegidos de forma aleatoria:
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (numeros_aleatorios)
import statistics
# Calcular la media
Media=statistics.mean(numeros_aleatorios)
# Calcular la moda
Moda=statistics.mode(numeros_aleatorios)
# Calcular la mediana
Mediana=statistics.median(numeros_aleatorios)
print(f"La Media es: {Media}, la Moda es: {Moda} y la Mediana es: {Mediana}")
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
if Media > Mediana and Mediana > Moda:
    print("Sesgo positivo o a la derecha")
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
elif Media < Mediana and Mediana < Moda:
    print("Sesgo negativo o a la izquierda")
# Sin sesgo: cuando la media, la mediana y la moda son iguales.
else:
    print("Sin sesgo")



 