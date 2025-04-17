# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range (101):
    print (cont)
   # Ciclo for que muestra los números desde 0 hasta 100



# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))
num_entero = abs(num)
dígitos = len(str(num_entero))
print("El número ingresado,", num,", tiene", dígitos, "dígitos")

