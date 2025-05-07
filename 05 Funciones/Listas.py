# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

# Se utiliza la función list() para crear una lista de números y por dentro la función range() para definir el rango y los saltos de números
lista_multiplo_4 = list(range(1,101,4))  
 
# Imprimo por pantalla la lista generada en la variable lista_multiplo_4
print(lista_multiplo_4)




# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como 
# se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
 
# Se crea una lista cuyos elementos son frutas
lista_elementos = ['manzana', 'banana', 'pera', 'kiwy', 'ciruela']
print(lista_elementos[3]) # Muestra el elemento de la posición 2 de la lista, contabilizando desde el 0 que corresponde a 'manzana'
print(lista_elementos[-2]) # indexing con número negativo, contabiliza desde el último elemento hacia el primero empezando del -1