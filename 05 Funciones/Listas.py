# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

# Se utiliza la función list() para crear una lista de números y por dentro la función range() para definir el rango y los saltos de números
lista_multiplo_4 = list(range(1,101,4))  
 
# Imprimo por pantalla la lista generada en la variable lista_multiplo_4
print(lista_multiplo_4)




# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como 
# se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
 
# Se crea una lista de 5 elementos, cuyos elementos son frutas
lista_elementos = ['manzana', 'banana', 'pera', 'kiwy', 'ciruela']

print(lista_elementos[3]) # Muestra el elemento de la posición 3 de la lista, contabilizando desde el 0 que corresponde a 'manzana'
print(lista_elementos[-2]) # indexing con número negativo, contabiliza desde el último elemento hacia el primero empezando del -1




# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una 
# lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = [] 

# Se crea la lista vacía
lista_vacia = []

# Se agregan tres palabras usando append en la variable lista_vacia
lista_vacia.append("uno")
lista_vacia.append("dos") 
lista_vacia.append("tres")

# Se muestra la variable lista_vacia con los 3 elementos agregados
print(lista_vacia)




# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"] # Lista de animales dada por la consigna

animales[1] = "loro"  # Se reemplaza el segundo elemento de la lista
animales[-1] = "oso"  # Se reemplaza el ultimo elemento de la lista (indexing con num negativos)

# Se muestra por pantalla la lista con el segundo y el ultimo elemento reemplazados
print(animales)




# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7] # Crea una lista con 5 números según consigna
numeros.remove(max(numeros)) # Con la función max() selecciona el numero de mayor valor de la lista, 22, y con la función remove() lo elimina
print(numeros) # Muestra el contenido de lista con el máximo valor eliminado 
