# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

CANT_NUMEROS = 10
sumatoria = 0

for cont in range(1, CANT_NUMEROS + 1):
    num = int(input("Ingrese un número entero: "))
    sumatoria += num


print("la media de los 100 valores ingresados es de", (sumatoria / CANT_NUMEROS))