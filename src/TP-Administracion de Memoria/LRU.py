import csv
from collections import OrderedDict
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


def lru(secuencia, marcos):
    """Implementa el algoritmo LRU para reemplazo de páginas.

    Args:
        secuencia (list): Lista de páginas a ser cargadas en memoria.
        marcos (int): Número de marcos de memoria disponibles.

    Returns:
        int: Número de fallos de página.
    """
    memoria = OrderedDict()  # Utiliza OrderedDict para manejar el orden de uso
    fallos = 0

    for i, pagina in enumerate(secuencia):
        if pagina not in memoria:
            fallos += 1
            if len(memoria) >= marcos:
                memoria.popitem(last=False)  # Elimina el elemento menos recientemente usado
            memoria[pagina] = None  # Agrega la nueva página
        # Actualiza el orden de uso
        memoria.move_to_end(pagina)
        print(f"Memoria: {list(memoria.keys())}")  # Muestra solo las páginas en memoria

    return fallos


if __name__ == "__main__":
    # Nombre del archivo CSV con la secuencia de páginas
    nombre_archivo = "../CSV/secuencia_paginas.CSV"

    # Leer la secuencia de páginas
    secuencia_paginas = leer_secuencia_csv(nombre_archivo)

    # Configurar el número de marcos de memoria
    marcos = 3  # Podrías usar sys.argv para obtener este valor

    # Ejecutar el algoritmo LRU
    fallos_lru = lru(secuencia_paginas, marcos)

    # Mostrar resultados
    print(f"LRU: {fallos_lru} fallos de página")