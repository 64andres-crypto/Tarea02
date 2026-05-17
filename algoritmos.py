# algoritmos.py
# Implementación de algoritmos de búsqueda y ordenamiento
# Autor: Tu nombre
# Fecha: Mayo 2026

import time
import random

# ==========================================
# BÚSQUEDA SECUENCIAL ITERATIVA
# ==========================================
def busqueda_secuencial_iterativa(lista, elemento):
    # Funcionamiento: recorre la lista elemento por elemento buscando el valor
    # Entradas: lista (list), elemento (int) a buscar
    # Salidas: índice (int) donde se encontró el elemento, -1 si no existe
    # Restricciones: funciona con listas ordenadas y desordenadas
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# ==========================================
# BÚSQUEDA SECUENCIAL RECURSIVA
# ==========================================
def busqueda_secuencial_recursiva(lista, elemento, indice=0):
    # Funcionamiento: recorre la lista recursivamente buscando el valor
    # Entradas: lista (list), elemento (int) a buscar, indice (int) posición actual
    # Salidas: índice (int) donde se encontró el elemento, -1 si no existe
    # Restricciones: funciona con listas ordenadas y desordenadas
    if indice >= len(lista):
        return -1
    if lista[indice] == elemento:
        return indice
    return busqueda_secuencial_recursiva(lista, elemento, indice + 1)

# ==========================================
# BÚSQUEDA BINARIA ITERATIVA
# ==========================================
def busqueda_binaria_iterativa(lista, elemento):
    # Funcionamiento: divide la lista a la mitad en cada paso para encontrar el elemento
    # Entradas: lista (list) ordenada, elemento (int) a buscar
    # Salidas: índice (int) donde se encontró el elemento, -1 si no existe
    # Restricciones: la lista debe estar ordenada
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# ==========================================
# BÚSQUEDA BINARIA RECURSIVA
# ==========================================
def busqueda_binaria_recursiva(lista, elemento, inicio=0, fin=None):
    # Funcionamiento: divide la lista a la mitad recursivamente para encontrar el elemento
    # Entradas: lista (list) ordenada, elemento (int) a buscar, inicio (int), fin (int)
    # Salidas: índice (int) donde se encontró el elemento, -1 si no existe
    # Restricciones: la lista debe estar ordenada
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == elemento:
        return medio
    elif lista[medio] < elemento:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, elemento, inicio, medio - 1)

# ==========================================
# ORDENAMIENTO BURBUJA ITERATIVO
# ==========================================
def burbuja_iterativo(lista):
    # Funcionamiento: compara pares de elementos adyacentes e intercambia si están desordenados
    # Entradas: lista (list) de enteros
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# ==========================================
# ORDENAMIENTO BURBUJA RECURSIVO
# ==========================================
def burbuja_recursivo(lista, n=None):
    # Funcionamiento: compara pares de elementos recursivamente hasta ordenar la lista
    # Entradas: lista (list) de enteros, n (int) tamaño actual
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    lista = lista.copy()
    if n is None:
        n = len(lista)
    if n == 1:
        return lista
    for i in range(n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return burbuja_recursivo(lista, n - 1)

# ==========================================
# ORDENAMIENTO SELECCIÓN ITERATIVO
# ==========================================
def seleccion_iterativo(lista):
    # Funcionamiento: busca el elemento menor y lo coloca al inicio, repite con el resto
    # Entradas: lista (list) de enteros
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# ==========================================
# ORDENAMIENTO SELECCIÓN RECURSIVO
# ==========================================
def seleccion_recursivo(lista, indice=0):
    # Funcionamiento: busca el menor elemento recursivamente y lo coloca en su posición
    # Entradas: lista (list) de enteros, indice (int) posición actual
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    lista = lista.copy()
    if indice >= len(lista) - 1:
        return lista
    min_idx = indice
    for j in range(indice + 1, len(lista)):
        if lista[j] < lista[min_idx]:
            min_idx = j
    lista[indice], lista[min_idx] = lista[min_idx], lista[indice]
    return seleccion_recursivo(lista, indice + 1)

# ==========================================
# ORDENAMIENTO RÁPIDO ITERATIVO
# ==========================================
def rapido_iterativo(lista):
    # Funcionamiento: elige un pivote y divide la lista en menores y mayores iterativamente
    # Entradas: lista (list) de enteros
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    lista = lista.copy()
    if len(lista) <= 1:
        return lista
    pila = [(0, len(lista) - 1)]
    while pila:
        inicio, fin = pila.pop()
        if inicio >= fin:
            continue
        pivote = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j] <= pivote:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
        p = i + 1
        pila.append((inicio, p - 1))
        pila.append((p + 1, fin))
    return lista

# ==========================================
# ORDENAMIENTO RÁPIDO RECURSIVO
# ==========================================
def rapido_recursivo(lista):
    # Funcionamiento: elige un pivote y divide la lista recursivamente en menores y mayores
    # Entradas: lista (list) de enteros
    # Salidas: lista (list) ordenada de menor a mayor
    # Restricciones: ninguna
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return rapido_recursivo(menores) + iguales + rapido_recursivo(mayores)