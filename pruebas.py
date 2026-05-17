# pruebas.py
# Mide el tiempo computacional de cada algoritmo con listas de 10, 100, 1000 y 10000 elementos
# Entradas: ninguna, genera las listas automáticamente
# Salidas: tiempos de ejecución de cada algoritmo impresos en consola
# Restricciones: ninguna

import time
import random
from algoritmos import *
import sys
sys.setrecursionlimit(15000)

tamanios = [10, 100, 1000, 10000]

def medir_tiempo(funcion, *args):
    # Funcionamiento: mide el tiempo que tarda una función en ejecutarse
    # Entradas: funcion (function), args (argumentos de la función)
    # Salidas: tiempo (float) en segundos
    # Restricciones: ninguna
    inicio = time.perf_counter()
    funcion(*args)
    fin = time.perf_counter()
    return fin - inicio

print("=" * 60)
print("ANÁLISIS DE TIEMPO COMPUTACIONAL")
print("=" * 60)

# ==========================================
# BÚSQUEDA SECUENCIAL
# ==========================================
print("\n--- BÚSQUEDA SECUENCIAL ---")
print(f"{'Tamaño':<10} {'Ordenada Iter':<20} {'Ordenada Rec':<20} {'Desordenada Iter':<20} {'Desordenada Rec':<20}")

for n in tamanios:
    lista_ordenada = list(range(n))
    lista_desordenada = random.sample(range(n), n)
    elemento = n - 1  # Peor caso: buscar el último elemento

    t1 = medir_tiempo(busqueda_secuencial_iterativa, lista_ordenada, elemento)
    t2 = medir_tiempo(busqueda_secuencial_recursiva, lista_ordenada, elemento)
    t3 = medir_tiempo(busqueda_secuencial_iterativa, lista_desordenada, elemento)
    t4 = medir_tiempo(busqueda_secuencial_recursiva, lista_desordenada, elemento)

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f} {t3:<20.8f} {t4:<20.8f}")

# ==========================================
# BÚSQUEDA BINARIA
# ==========================================
print("\n--- BÚSQUEDA BINARIA ---")
print(f"{'Tamaño':<10} {'Ordenada Iter':<20} {'Ordenada Rec':<20}")

for n in tamanios:
    lista_ordenada = list(range(n))
    elemento = n - 1

    t1 = medir_tiempo(busqueda_binaria_iterativa, lista_ordenada, elemento)
    t2 = medir_tiempo(busqueda_binaria_recursiva, lista_ordenada, elemento)

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f}")

# ==========================================
# ORDENAMIENTO BURBUJA
# ==========================================
print("\n--- ORDENAMIENTO BURBUJA ---")
print(f"{'Tamaño':<10} {'Ordenada Iter':<20} {'Ordenada Rec':<20} {'Desordenada Iter':<20} {'Desordenada Rec':<20} {'Invertida Iter':<20} {'Invertida Rec':<20}")

for n in tamanios:
    lista_ordenada = list(range(n))
    lista_desordenada = random.sample(range(n), n)
    lista_invertida = list(range(n, 0, -1))

    t1 = medir_tiempo(burbuja_iterativo, lista_ordenada)
    t2 = medir_tiempo(burbuja_recursivo, lista_ordenada)
    t3 = medir_tiempo(burbuja_iterativo, lista_desordenada)
    t4 = medir_tiempo(burbuja_recursivo, lista_desordenada)
    t5 = medir_tiempo(burbuja_iterativo, lista_invertida)
    t6 = medir_tiempo(burbuja_recursivo, lista_invertida)

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f} {t3:<20.8f} {t4:<20.8f} {t5:<20.8f} {t6:<20.8f}")

# ==========================================
# ORDENAMIENTO SELECCIÓN
# ==========================================
print("\n--- ORDENAMIENTO SELECCIÓN ---")
print(f"{'Tamaño':<10} {'Ordenada Iter':<20} {'Ordenada Rec':<20} {'Desordenada Iter':<20} {'Desordenada Rec':<20} {'Invertida Iter':<20} {'Invertida Rec':<20}")

for n in tamanios:
    lista_ordenada = list(range(n))
    lista_desordenada = random.sample(range(n), n)
    lista_invertida = list(range(n, 0, -1))

    t1 = medir_tiempo(seleccion_iterativo, lista_ordenada)
    t2 = medir_tiempo(seleccion_recursivo, lista_ordenada)
    t3 = medir_tiempo(seleccion_iterativo, lista_desordenada)
    t4 = medir_tiempo(seleccion_recursivo, lista_desordenada)
    t5 = medir_tiempo(seleccion_iterativo, lista_invertida)
    t6 = medir_tiempo(seleccion_recursivo, lista_invertida)

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f} {t3:<20.8f} {t4:<20.8f} {t5:<20.8f} {t6:<20.8f}")

# ==========================================
# ORDENAMIENTO RÁPIDO
# ==========================================
print("\n--- ORDENAMIENTO RÁPIDO ---")
print(f"{'Tamaño':<10} {'Ordenada Iter':<20} {'Ordenada Rec':<20} {'Desordenada Iter':<20} {'Desordenada Rec':<20} {'Invertida Iter':<20} {'Invertida Rec':<20}")

for n in tamanios:
    lista_ordenada = list(range(n))
    lista_desordenada = random.sample(range(n), n)
    lista_invertida = list(range(n, 0, -1))

    t1 = medir_tiempo(rapido_iterativo, lista_ordenada)
    t2 = medir_tiempo(rapido_recursivo, lista_ordenada)
    t3 = medir_tiempo(rapido_iterativo, lista_desordenada)
    t4 = medir_tiempo(rapido_recursivo, lista_desordenada)
    t5 = medir_tiempo(rapido_iterativo, lista_invertida)
    t6 = medir_tiempo(rapido_recursivo, lista_invertida)

    print(f"{n:<10} {t1:<20.8f} {t2:<20.8f} {t3:<20.8f} {t4:<20.8f} {t5:<20.8f} {t6:<20.8f}")