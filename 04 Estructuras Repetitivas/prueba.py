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
for cont in range(1, 10):
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
