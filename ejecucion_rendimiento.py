import time
import numpy as np

# Definir un volumen significativo de información (1 millón de elementos)
tamaño = 1_000_000

print(f"Rendimiento / Lista vs Array ({tamaño:,} elementos)")


# Prueba con Lista.

lista_datos = list(range(tamaño))

# Registra el tiempo exacto (en segundos) justo antes de empezar a operar con la lista.
inicio_lista = time.time()

# Operación matemática: sumar 5 a cada elemento mediante comprensión de lista
lista_resultado = [x + 5 for x in lista_datos]
fin_lista = time.time()

tiempo_lista = fin_lista - inicio_lista
print(f"Tiempo con una lista: {tiempo_lista:.6f} segundos")


# Prueba con Arrays

array_datos = np.arange(tamaño)

inicio_numpy = time.time()

# Operación matemática: sumar 5 directamente a todo el array

array_resultado = array_datos + 5
fin_numpy = time.time()

tiempo_numpy = fin_numpy - inicio_numpy
print(f"Tiempo con un array: {tiempo_numpy:.6f} segundos")


# Resultados

if tiempo_numpy > 0:
    aceleracion = tiempo_lista / tiempo_numpy
    print(f"Resultado del análisis: El array fue aproximadamente {aceleracion:.2f} veces más rápido que la lista.")