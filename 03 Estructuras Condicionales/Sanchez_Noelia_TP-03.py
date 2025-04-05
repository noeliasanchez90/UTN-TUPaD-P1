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




 # Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con 
 # vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar 
 # el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Por favor, ingrese una frase o palabra: ")

# Verificar si el último carácter es una vocal
if frase[-1].lower() in 'aeiou':
    # Añadir un signo de exclamación
    frase += '!'
    
# Imprimir el resultado
print(frase)




# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la 
# opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el 
# resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre 
# mayúsculas y minúsculas.

# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitar la opción deseada
print("Selecciona una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")

opcion = input("Ingresa 1, 2 o 3: ")

# Transformar el nombre según la opción seleccionada
if opcion == '1':
    resultado = nombre.upper()
    print("Tu nombre en mayúsculas es:", resultado)
elif opcion == '2':
    resultado = nombre.lower()
    print("Tu nombre en minúsculas es:", resultado)
elif opcion == '3':
    resultado = nombre.title()
    print("Tu nombre con la primera letra mayúscula es:", resultado)
else:
    print("Opción no válida. Por favor, selecciona 1, 2 o 3.")




# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de 
# las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

Magnitud=float(input("Por favor, ingrese la magnitud de un terremoto: "))

# Determinar la intensidad según la magnitud
if Magnitud < 3:
    Intensidad = "Muy leve (imperceptible)"
elif 3 <= Magnitud < 4:
    Intensidad = "Leve (ligeramente perceptible)"
elif 4 <= Magnitud < 5:
    Intensidad = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= Magnitud < 6: 
    Intensidad = "Muy Fuerte (puede causar daños significativos)"
else:
    Intensidad = "Extremo (puede causar graves daños a gran escala)"

# Mostrar el resultado
print(f"La magnitud ingresada es de: {Magnitud}, en la escala de Richter equivale a un terremoto de intensidad {Intensidad}.")



# Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y 
# qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño,
# invierno, primavera o verano.

# Solicitar información al usuario
Hemisferio=input("Por favor, indique en que hemisferio se encuentra, si esta en el Norte ingrese N y si esta en el Sur ingrese S: ")
Dia=int(input("Ingrese el día: "))
Mes=input("Ingrese el mes en el que se encuentra: ")

# Función .upper para que el usuario pueda ingresar los datos solicitados tanto en minuscula como en mayúscula.
Hemisferio = Hemisferio.upper()
Mes = Mes.upper()

# Función para determinar la estación
if Hemisferio == 'N' and ((Mes == 'DICIEMBRE' and 21 <= Dia) or Mes == 'ENERO' or Mes == 'FEBRERO' or (Mes == 'MARZO' and Dia <= 20)):
    print("Usted se encuentra en Invierno")
elif Hemisferio == 'N' and ((Mes == 'MARZO' and Dia <=21) or Mes == 'ABRIL' or Mes == 'MAYO' or (Mes == 'JUNIO' and Dia <=20)):
    print("Usted se encuentra en Primavera")
elif Hemisferio == 'N' and ((Mes == 'JUNIO' and Dia >= 21) or Mes == 'JULIO' or Mes == 'AGOSTO' or (Mes == 'SEPTIEMBRE' and Dia <= 20)):
    print("Usted se encuentra en Verano")
elif Hemisferio == 'N' and ((Mes == 'SEPTIEMBRE' and Dia >= 21) or Mes == 'OCTUBRE' or Mes == 'NOVIEMBRE' or ( Mes == 'DICIEMBRE' and Dia <= 20)): 
    print("Usted se encuentra en Otoño")

elif Hemisferio == 'S' and ((Mes == 'DICIEMBRE' and 21 <= Dia) or Mes == 'ENERO' or Mes == 'FEBRERO' or (Mes == 'MARZO' and Dia <= 20)):
    print("Usted se encuentra en Verano")
elif Hemisferio == 'S' and ((Mes == 'MARZO' and Dia <=21) or Mes == 'ABRIL' or Mes == 'MAYO' or (Mes == 'JUNIO' and Dia <=20)):
    print("Usted se encuentra en Otoño")
elif Hemisferio == 'S' and ((Mes == 'JUNIO' and Dia >= 21) or Mes == 'JULIO' or Mes == 'AGOSTO' or (Mes == 'SEPTIEMBRE' and Dia <= 20)):
    print("Usted se encuentra en Invierno")
elif Hemisferio == 'S' and ((Mes == 'SEPTIEMBRE' and Dia >= 21) or Mes == 'OCTUBRE' or Mes == 'NOVIEMBRE' or ( Mes == 'DICIEMBRE' and Dia <= 20)): 
    print("Usted se encuentra en Primavera")

