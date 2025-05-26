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




# Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin 
# espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
   # La solución debe ser recursiva.
   # No se debe usar [::-1] ni la función reversed().

def es_palindromo(texto):
  if len(texto) <= 1: # cadenas vacías o de un solo caracter son palidromos
    return True
  
  if texto[0] != texto[-1]:
    return False
  
  else:
    return es_palindromo(texto[1:-1]) # llama con el texto sin el primer y último carácter

  
print(f"NOELIA es palidromo: {es_palindromo("NOELIA")}")
print(f"ANA es palidromo: {es_palindromo("ANA")}")




# Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
# devuelva la suma de todos sus dígitos.

def suma_digitos(n):
  if n < 10:
    return n
  else:
    return n % 10 + suma_digitos(n // 10)
  
print(f"La suma de los dígitos  es: {suma_digitos(2523)}")




# Ejercicio 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el 
# siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el 
# total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
  if n == 1:
    return 1 # caso base: la cima de la pirámide
  else:
    return n + contar_bloques(n - 1) # suma el nivel actual y pasa al superior
  
print(f"La cantidad de bloques ingresado es: {contar_bloques(4)}")





# Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
# (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
   if numero == 0:
     return 0
   else:
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
      return contar_digito(resto, digito)
    

print(contar_digito(12233421, 3))