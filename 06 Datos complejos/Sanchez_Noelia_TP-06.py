# Ejercicio 1: Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 
# 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Se añaden nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar resultado
print(precios_frutas)




# Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el 
# punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# Reemplazar el precio de las frutas 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)





# Ejercicio 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el 
# punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print(precios_frutas.keys())




# Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
#       • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#       • Luego, pedí un nombre y mostrale el número asociado, si existe.

#agenda={}

#for i in range(1,6):
#    Nombre = input(f"Ingrese el nombre del alumno {i}: ")
#    Tel = input(f"Ingrese el telefono de {Nombre}: ")
#    agenda[Nombre] = Tel
#print("Agenda completa: ")
#print(agenda)

# Consultar un numero de telefono
#Nom = input("Ingrese el nombre para obtener su telefono: ")

#if Nom in agenda:
#    print(f"El teléfono de {Nom} es: {agenda[Nom]}")
#else:
#    print(f"{Nom} no se encuentra en la agenda.")





# Ejercicio 5: Solicita al usuario una frase e imprime:
#     • Las palabras únicas (usando un set).
#     • Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar las palabras
palabras = frase.split()

# Obtener las palabras únicas usando un set
palabras_unicas = set(palabras)

# Crear el diccionario de recuento
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)





# Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el 
# promedio de cada alumno.

#notas_alumnos = {}

#for i in range(1,4):
#    nombre = input(f"Ingrese el nombre del alumno {i}: ")
#    nota1 = float(input(f"Ingrese la primer nota de {nombre}: "))
#    nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
#    nota3 = float(input(f"Ingrese la tercer nota de {nombre}: "))

#    notas_alumnos[nombre] = (nota1, nota2, nota3) # Tupla

#print("\nNotas de los alumnos:")
#for nombre, notas in notas_alumnos.items():
#    print(f"{nombre}: {notas}")

#print("\nPromedios:")
#for nombre, notas in notas_alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"{nombre}: {promedio:.2f}")





# Ejercicio 7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#   • Mostrá los que aprobaron ambos parciales.
#   • Mostrá los que aprobaron solo uno de los dos.
#   • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"100", "103", "105", "108", "110"}
parcial2 = {"103", "105", "106", "108", "113"}

#Alumnos que aprobaron ambos parciales (interesección)
aprobaron_ambos = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:", aprobaron_ambos)

# Alumnos que aprobaron un solo parcial de los dos (diferencia simétrica)
aprobaron_uno = parcial1 ^ parcial2
print("Estudiantes que aprobaron un solo parcial de los dos: ", aprobaron_uno)

# lista total de estudiantes que aprobaron al menos un parcial (union)
aprobaron_al_menos_uno = parcial1 | parcial2
print("Estudiantes que aprobaron al menos un parcial: ", aprobaron_al_menos_uno)





#Ejercicio 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario con frutas
stock_frutas = {"pera": 5, "manzana": 10, "banana": 9, "uva": 8}

# Se solicita al usuario que ingrese una fruta
fruta = input("Ingrese la fruta para saber su stock: ").lower()

# Si la fruta está en el stock
if fruta in stock_frutas:
    print(f"El stock de '{fruta}' es de {stock_frutas[fruta]} unidades.")

    # Consultar si se desea agregar más unidades
    respuesta = input(f"¿Desea agregar más unidades a '{fruta}'? (s/n): ").lower()
    if respuesta == 's':
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock_frutas[fruta] += cantidad
        print(f"Nuevo stock de '{fruta}': {stock_frutas[fruta]} unidades.")
else:
    print(f"'{fruta}' no se encuentra en el stock.")

    # Preguntar si quiere agregar la fruta como nuevo producto
    respuesta = input(f"¿Desea agregar '{fruta}' como nuevo producto? (s/n): ").lower()
    if respuesta == "s":
        cantidad = int(input(f"¿Cuántas unidades tiene '{fruta}'?: "))
        stock_frutas[fruta] = cantidad
        print(f"'{fruta}' fue agregado al stock con {cantidad} unidades.")

# Mostrar stock final
print("\n Stock actual:")
for prod, cantidad in stock_frutas.items():
    print(f"- {prod}: {cantidad} unidades")