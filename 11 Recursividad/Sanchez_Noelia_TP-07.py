# Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para 
# calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Función recursiva para calcular factorial 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Pedir al usuario que ingrese un num para calcular el factorial:
num = int(input("ingrese un número entero positivo: "))

if num < 0:
    num = int(print("Por favor, ingrese un número entero positivo: "))
else:
    print(f"Factoriales del 1 al {num}:")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")