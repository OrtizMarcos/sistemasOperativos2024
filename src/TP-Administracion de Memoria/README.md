# Documentación del Trabajo Práctico

## **1. Introducción**

Este trabajo práctico aborda la implementación de dos algoritmos de reemplazo de páginas: **FIFO** (First In, First Out) y **LRU** (Least Recently Used). Los algoritmos se aplican sobre una secuencia de páginas leída desde un archivo CSV, y su objetivo es gestionar eficientemente el uso de marcos de páginas en memoria, minimizando los fallos de página.

## **2. Descripción Algorítmica**

### **2.1 Algoritmo FIFO (First In, First Out)**
El algoritmo FIFO reemplaza la página que ingresó primero en memoria cuando ocurre un fallo de página y los marcos están llenos. Este enfoque es simple, pero no necesariamente el más eficiente.

**Pasos del algoritmo:**
1. Si la página solicitada ya está en memoria, no hay fallo de página.
2. Si la página no está en memoria:
   - Si hay espacio disponible, se agrega la página a la memoria.
   - Si no hay espacio, se reemplaza la página más antigua (primera en entrar).

### **2.2 Algoritmo LRU (Least Recently Used)**
El algoritmo LRU reemplaza la página que no ha sido utilizada durante más tiempo. Este enfoque utiliza información temporal para tomar decisiones más óptimas que FIFO.

**Pasos del algoritmo:**
1. Si la página solicitada ya está en memoria, no hay fallo de página y se actualiza su último uso.
2. Si la página no está en memoria:
   - Si hay espacio disponible, se agrega la página a la memoria.
   - Si no hay espacio, se reemplaza la página menos recientemente usada.

## **3. Implementación en Python**

### **3.1 Requisitos del entorno**
- **Lenguaje:** Python 3.10+
- **Bibliotecas utilizadas:**
  - `csv` (incluida en la biblioteca estándar de Python).
- **Sistemas operativos probados:** Windows 10 y Linux (Ubuntu 20.04).

### **3.2 Instrucciones para ejecutar el código**
1. Cree un archivo CSV con la secuencia de páginas. Ejemplo:
   ```
   1,3,2,1,5,3,4,1,5,2,6,7,5,7,2,5,3,5,3,1
   ```
2. Guarde el archivo con el nombre `secuencia_paginas.csv`.
3. Ejecute el script Python que contiene la implementación de los algoritmos FIFO y LRU.
4. Configure el número de marcos de memoria dentro del código según el caso de prueba deseado.
5. Observe los resultados en la consola, donde se mostrarán los fallos de página y la evolución de los marcos de memoria.

## **4. Casos de Prueba**

### **4.1 Archivo CSV de prueba**
Ejemplo de archivo CSV:

```
1,3,2,1,5,3,4,1,5,2,6,7,5,7,2,5,3,5,3,1
```

### **4.2 Resultados esperados**

| Algoritmo | Marcos | Secuencia de Páginas                   | Fallos |
|-----------|--------|----------------------------------------|--------|
| FIFO      | 3      | 1,3,2,1,5,3,4,1,5,2,6,7,5,7,2,5,3,5,3 | 11     |
| LRU       | 3      | 1,3,2,1,5,3,4,1,5,2,6,7,5,7,2,5,3,5,3 | 11     |

### **4.3 Pantallas de Ejecución**
Incluya capturas de la ejecución del programa en ambos sistemas operativos, mostrando los fallos y la evolución de los marcos.

![img.png](FIFO_Test.png)

![img_1.png](LRU_test.png)

## **5. Conclusión**

Este trabajo práctico demuestra cómo implementar y analizar algoritmos de reemplazo de páginas en un entorno sencillo. Ambos algoritmos tienen ventajas y desventajas dependiendo del caso de uso, siendo LRU más eficiente en general, pero más costoso computacionalmente.

---

**Sistemas Operativos Utilizados:**
- Windows 10
- Linux (Ubuntu 20.04)

**Lenguaje de Programación:**
- Python 3.10+

