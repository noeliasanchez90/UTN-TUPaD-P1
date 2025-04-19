# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range (101):
    print (cont)
   # Ciclo for que muestra los números desde 0 hasta 100



# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

#Se solicita ingresar un número entero al usuario.
num = int(input("Ingrese un número entero: "))
#Le aplicamos el valor absoluto para contar dígitos sin el singno "-" si es negativo.
num_entero = abs(num)
#Aplicamos la función len() para contar dígitos
dígitos = len(str(num_entero))
print("El número ingresado,", num,", tiene", dígitos, "dígitos")



# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Solicito ingresar los números enteros al usuario:
print("Este programa devolverá la suma de los números comprendidos entre dos valores ingresados por el usuario:")
num_inicial = int(input("Ingrese el primer núm. entero: "))
num_final = int(input("Ingrese el segundo núm. entero: "))
# Inicializo la variable sumatoria en 0 
sumatoria = 0

# Evalúo con la función if cual de los dos número ingresados es mayor para poder sumar los núm del medio en forma creciente
if num_final > num_inicial:
    for num in range(num_inicial + 1, num_final):
        sumatoria += num
else:
    for num in range(num_final + 1, num_inicial):
        sumatoria += num

# Muestro por pantalla el valor de la sumatoria
print("La sumatoria de los num comprendidos entre ", num_inicial, "y", num_final, "es:", sumatoria)



# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa 
# debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("ingrese un número entero (0 para salir): "))
sumatoria = 0

# Mientras los números ingresados sean distinto de 0, se irán sumando secuencialmente acumulado.
while num != 0: 
    sumatoria = sumatoria + num
    num = int(input("Ingrese otro número entero (0 para salir): "))

# Mostrar el total acumulado de los números ingresados
print("La sumatoria de los números ingresados es = ", sumatoria)



# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Se importa la librería random
import random
#Se le solicita al usuario que adivine un núm entre 0 y 9
num = int(input("Adivine el número entre 0 y 9: "))
# Se aplica la función randint() para generar un num aleatorio entre 0 y 9
num_aleatorio = random.randint(0, 9)
print(num_aleatorio)
# Se inicializa un contador para contar la cantidad de intentos hasta adivinar el número.
cont = 1

# Inicializamos el bucle while hasta que el número ingresado por el usuario sea igual al aleatorio, ahí corta
while num != num_aleatorio:
    cont += 1
    num = int(input("Adivine el número entre 0 y 9:"))

# Se muestra por pantalla la cantidad de intentos.
print("se hicieron ", cont, "intentos")



# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for num in range (100, -1, -2):
    print(str(num), end=' ')



# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo: "))
sumatoria = 0

if num >= 0:
    for x in range(0, num + 1):
        sumatoria += x
    print("La sumatoria de los núm. comprendidos entre 0 y",num, "es de:", sumatoria)

else:
    print("No ingresó un número entero positivo")



# Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar 
# cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para 
# probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo 
# cambio).

# inicializo las vaiables contadoras en 0
par = 0
impar = 0
negativo = 0
positivo = 0

# Creo un ciclo for donde el usuario debe ingresar 100 números enteros
for cont in range(1, 101):
    num = int(input("Ingrese un número: "))
    if (num % 2) == 0:   # Si el resto de la división por 2 es 0, se cuenta como número par
        par += 1
    elif (num % 2) != 0: # Si el resto de la división por 2 es distinta de 0, se cuenta como número impar
        impar += 1
    if num < 0:          # Si el num ingresado es menor que cero, se cuenta como número negativo
        negativo += 1
    elif num >= 0:       # Si el número ingresado es mayor o igual que cero, se cuenta como número positivo
        positivo += 1

# Se muestran los resultados por pantalla
print("Se ingresaron", par, "números pares")
print("Se ingresaron", impar, "números impares")
print("Se ingresaron", negativo, "números negativos")
print("Se ingresaron", positivo, "números positivos")




# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos
# valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo 
# un valor).


CANT_NUMEROS = 100  # Defino una constante para definir la cantidad de números a ingresar
sumatoria = 0       # Inicializo la variable sumatoria en 0

# Inicializo un bucle for donde en cada ciclo solicita un número al usuario y los va sumando
for cont in range(1, CANT_NUMEROS + 1):
    num = int(input("Ingrese un número entero: "))
    sumatoria += num

# Muestra por pantalla la media de los valores ingresados
print("la media de los 100 valores ingresados es de", (sumatoria / CANT_NUMEROS))




# Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Se solicita al usuario que ingrese un número
num = input("Ingrese un número: ")

# Invertir el número convirtiéndolo en una cadena y usando slicing
numero_invertido = num[::-1]

# Se muestra por pantalla el número invertido
print("el número", num, "invertido es", numero_invertido)