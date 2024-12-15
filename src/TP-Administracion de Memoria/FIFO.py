import csv
from collections import deque
import sys


def leer_secuencia_csv(nombre_archivo):
    """Lee una secuencia de páginas desde un archivo CSV y devuelve una lista de enteros."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            secuencia = []
            for fila in lector:
                secuencia.extend(map(int, fila))
            return secuencia
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)


def fifo(secuencia, marcos):
    """Implementa el algoritmo FIFO para reemplazo de páginas.

    Args:
        secuencia (list): Lista de páginas a ser cargadas en memoria.
        marcos (int): Número de marcos de memoria disponibles.

    Returns:
        int: Número de fallos de página.
    """
    memoria = deque()
    fallos = 0
    memoria_set = set()  # Para verificar rápidamente si una página está en memoria

    for pagina in secuencia:
        if pagina not in memoria_set:
            fallos += 1
            if len(memoria) >= marcos:
                pagina_salida = memoria.popleft()  # Elimina la página más antigua
                memoria_set.remove(pagina_salida)  # Actualiza el conjunto
            memoria.append(pagina)
            memoria_set.add(pagina)  # Agrega la nueva página al conjunto
        print(f"Memoria: {list(memoria)}")  # Imprime el estado de la memoria

    return fallos


if __name__ == "__main__":
    # Nombre del archivo CSV con la secuencia de páginas
    nombre_archivo = "../CSV/secuencia_paginas.CSV"

    # Leer la secuencia de páginas
    secuencia_paginas = leer_secuencia_csv(nombre_archivo)

    # Configurar el número de marcos de memoria
    marcos = 3  # Esto podría hacerse dinámico usando argumentos de línea de comandos

    # Ejecutar el algoritmo FIFO
    fallos_fifo = fifo(secuencia_paginas, marcos)

    # Mostrar resultados
    print(f"FIFO: {fallos_fifo} fallos de página")