# Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para 
# calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Función recursiva para calcular factorial 
#def factorial(num):
#    if num == 0:
#        return 1
#    else:
#        return num * factorial(num - 1)

# Pedir al usuario que ingrese un num para calcular el factorial:
#num = int(input("ingrese un número entero positivo: "))

#if num < 0:
#    num = int(print("Por favor, ingrese un número entero positivo: "))
#else:
#    print(f"Factoriales del 1 al {num}:")
#    for i in range(1, num + 1):
#        print(f"{i}! = {factorial(i)}")




# Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# definir función Fibonacci
#def fibonacci(pos):

#    if pos == 0:
#        return 0
#    elif pos == 1:
#        return 1
#    else:
#        return fibonacci(pos-1) + fibonacci(pos-2)

# solicitar al usuario que especifique la posición en la serie de Fibonacci 
#pos = int(input("Ingrese la posición de la serie de Fibonacci hasta la que quieres ver: "))

#for i in range(0, pos + 1):
#    print(f"F({i}) = {fibonacci(i)}")




# Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando
# la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

#def potencia(n, m):
#    if m == 0:
#        return 1 # Cualquier número elevado a la 0 es 1
#    else:
#        return n * potencia(n, m-1)

# Algoritmo general para probar la función
#base = int(input("Introduce la base (n): "))
#exponente = int(input("Introduce el exponente (m): "))

#resultado = potencia(base, exponente)
#print(f"{base} elevado a la {exponente} es: {resultado}")




# Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva
# su representación en binario como una cadena de texto.

def decimal_a_binario(numDec):
   if numDec == 0:
     return ""     #Cuando numDec==0, devolvemos una cadena vacía 
   else:
     return decimal_a_binario(numDec // 2) + str(numDec % 2)

# Ejemplo de uso
print(decimal_a_binario(34))
