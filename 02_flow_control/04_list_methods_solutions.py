###
# EJERCICIOS
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nEjercicio 1:")
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)  # Output: [0, 2, 10, 3, 4, 5, 6]

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("\nEjercicio 2:")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
elemento_eliminado = lista_a.pop(3)
print(f"Elemento eliminado: {elemento_eliminado}") #Output: Elemento eliminado: 5
lista_b.clear()
print("Lista a:", lista_a) #Output: Lista a: [2, 3, 4, 6, 1, 2]
print("Lista b:", lista_b) #Output: Lista b: []

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("\nEjercicio 3:")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:5]
print(lista)  # Output: [1, 2, 6, 7, 8, 9, 10]

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("\nEjercicio 4:")
lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
cantidad_dos = lista.count(2)
esta_el_siete = 7 in lista
print(f"Lista ordenada: {lista}") #Output: Lista ordenada: [1, 2, 2, 4, 5, 8, 9]
print(f"Cantidad de 2: {cantidad_dos}") #Output: Cantidad de 2: 2
print(f"¿Está el 7?: {esta_el_siete}") #Output: ¿Está el 7?: False

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("\nEjercicio 5:")
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(f"Original: {original}")       # Output: Original: [10, 2, 3]
print(f"Copia 1 (slicing): {copia_1}") # Output: Copia 1 (slicing): [1, 2, 3]
print(f"Copia 2 (copy()): {copia_2}") # Output: Copia 2 (copy()): [1, 2, 3]
print(f"Referencia: {referencia}")     # Output: Referencia: [10, 2, 3]

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("\nEjercicio 6:")
strings = ["Manzana", "pera", "BANANA", "naranja"]
strings.sort(key=str.lower)
print(strings) # Output: ['BANANA', 'Manzana', 'naranja', 'pera']