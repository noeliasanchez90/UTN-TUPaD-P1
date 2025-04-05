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
