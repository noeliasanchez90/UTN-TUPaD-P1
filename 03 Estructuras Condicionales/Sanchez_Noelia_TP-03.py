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


