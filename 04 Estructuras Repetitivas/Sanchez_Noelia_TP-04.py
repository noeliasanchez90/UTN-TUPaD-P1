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

num = int(input("ingrese un número entero: "))
sumatoria = 0

while num != 0:
    sumatoria = sumatoria + num
    num = int(input("Ingrese otro número entero: "))

print("La sumatoria de los números ingresados es = ", sumatoria)
