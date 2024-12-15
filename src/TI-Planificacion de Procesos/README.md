# Sistema Operativos II
## Trabajo de Investigación 
## Planificación de Procesos
#### Steven Gracia – 6050061
#### Marcos Ortiz - 6035220
## Investigo y respondo las siguientes preguntas

# Documentación sobre Procesos y Gestión en Sistemas Operativos

| Pregunta                                                                                           | Respuesta                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. En un sistema interactivo, ¿qué significa que los procesos típicamente están en ejecución un largo periodo? | Los procesos cortos se completan rápidamente y requieren poco tiempo de CPU. Aunque los procesos interactivos pueden estar activos durante largos períodos, su ejecución se interrumpe frecuentemente. Un ejemplo de proceso largo es el renderizado de video. |
| 2. ¿Qué es un tick?                                                                                | Un tick es una unidad de tiempo utilizada en sistemas operativos para gestionar la planificación de procesos. Indica cuándo se debe interrumpir un proceso para permitir que otro comience a ejecutarse, siendo esencial para el cambio de contexto.   |
| 3. ¿Qué es un quantum?                                                                             | Un quantum es el tiempo fijo asignado a un proceso para ejecutarse en un sistema de planificación, especialmente en el algoritmo Round Robin. Su duración afecta la eficiencia y el tiempo de respuesta del sistema.                                   |
| 4. ¿Qué se entiende por afinidad del procesador?                                                  | La afinidad del procesador es la preferencia de un proceso por ejecutarse en un núcleo específico de la CPU, mejorando el rendimiento al aprovechar la caché local y reducir la latencia.                                                            |
| 5. ¿Cuál es la diferencia entre afinidad dura y suave?                                            | La afinidad dura asigna un proceso a un núcleo específico sin permitir su movimiento, mientras que la afinidad suave permite que un proceso se ejecute preferentemente en un núcleo, pero puede ser trasladado a otros si es necesario.            |
| 6. ¿Cómo interactúan la afinidad a procesador y el balanceo de cargas?                             | La afinidad y el balanceo de cargas trabajan en contra del otro. La afinidad debe predominar cuando se busca maximizar el rendimiento en un núcleo específico, mientras que el balanceo de cargas es esencial para distribuir eficientemente la carga de trabajo. |

#### Afinidad del Procesador

| Aspecto        | Descripción                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| **Objetivo**   | Mantener un proceso en el mismo núcleo para aprovechar la caché y mejorar el rendimiento.    |
| **Desventaja** | Puede llevar a una distribución desigual de la carga de trabajo, con algunos núcleos sobrecargados y otros subutilizados. |

## Balanceo de Carga

| Aspecto        | Descripción                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| **Objetivo**   | Distribuir equitativamente los procesos entre los núcleos para maximizar el uso del CPU y evitar cuellos de botella. |
| **Desventaja** | Puede resultar en un mayor número de cambios de contexto y fallos de caché si los procesos se mueven frecuentemente entre núcleos. |

## Cuándo Predominar Cada Mecanismo

| Mecanismo                      | Contexto                                                                                      |
|--------------------------------|-----------------------------------------------------------------------------------------------|
| **Predominar la Afinidad**    | En aplicaciones que requieren un alto rendimiento y donde el acceso a datos en caché es crítico, como bases de datos o aplicaciones en tiempo real. |
| **Predominar el Balanceo de Carga** | En entornos donde la carga de trabajo es variable y se busca maximizar la utilización del CPU, como en servidores web o sistemas de procesamiento por lotes. |
7. ¿Qué son los procesos de tiempo real?

## Definición de Procesos de Tiempo Real

| Aspecto                               | Descripción                                                                                                                                       |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descripción**                       | Los procesos de tiempo real son aquellos que deben completarse dentro de un plazo específico para que el sistema funcione correctamente.        |

## Características de los Procesos de Tiempo Real

| Característica          | Descripción                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Determinismo**       | Cumplimiento estricto de plazos.                                                                                            |
| **Prioridades Elevadas** | Se les asignan altas prioridades en el sistema.                                                                             |

## Clasificación de Procesos de Tiempo Real

| Tipo                    | Descripción                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Tiempo Real Duro**   | Violaciones de plazos pueden causar fallos catastróficos (ej. control de aeronaves).                                       |
| **Tiempo Real Blando** | Violaciones pueden degradar el rendimiento, pero no causan fallos críticos (ej. aplicaciones multimedia).                     |

## Ejemplos de Procesos de Tiempo Real

| Ejemplo                |
|-----------------------|
| Control industrial     |
| Monitoreo médico      |
| Sistemas de navegación |

8. Asumiendo los siguientes procesos:
```csv
Proceso Llegada tick (t) 
A          0      8
B          2      13
C          4      3
D          4      6
E          6      8
F          6      3
```
Desarrolle la representación gráfica de cómo el despachador les asignaría el CPU, y la 
tabla de análisis, bajo: 
- Ronda (Round robin) con q = 1
- Ronda (Round robin) con q = 3
- Proceso más corto a continuación
Compare el rendimiento bajo cada uno de estos esquemas. 
https://colab.research.google.com/drive/1uly_hHsyPxOq1q6Dg￾veLKUQThpvKpt5?usp=sharing
Análisis Round Robin con q = 1:
Análisis de procesos:
```
Proceso | Tiempo de llegada | Duración | Tiempo de finalización | Tiempo de espera | 
Tiempo de retorno
----------------------------------------------------------------------------------------------------
C | 4 | 3 | 11 | 4 | 7 
F | 6 | 3 | 14 | 5 | 8 
A | 0 | 8 | 8 | 0 | 8 
D | 4 | 6 | 20 | 10 | 16 
E | 6 | 8 | 28 | 14 | 22 
B | 2 | 13 | 41 | 26 | 39 
Análisis Round Robin con q = 3:
Análisis de procesos:
Proceso | Tiempo de llegada | Duración | Tiempo de finalización | Tiempo de espera | 
Tiempo de retorno
----------------------------------------------------------------------------------------------------
A | 0 | 8 | 8 | 0 | 8 
B | 2 | 13 | 41 | 26 | 39 
C | 4 | 3 | 11 | 4 | 7 
D | 4 | 6 | 20 | 10 | 16 
E | 6 | 8 | 28 | 14 | 22 
F | 6 | 3 | 14 | 5 | 8 
Análisis Proceso Más Corto a Continuación (SJF):
Análisis de procesos:
Proceso | Tiempo de llegada | Duración | Tiempo de finalización | Tiempo de espera | 
Tiempo de retorno
----------------------------------------------------------------------------------------------------
A | 0 | 8 | 8 | 0 | 8 
C | 4 | 3 | 11 | 4 | 7 
F | 6 | 3 | 14 | 5 | 8 
D | 4 | 6 | 20 | 10 | 16 
E | 6 | 8 | 28 | 14 | 22 
B | 2 | 13 | 41 | 26 | 39 
````
¿Qué ventajas presenta cada uno?

## 1. Round Robin con Quantum = 1

| Aspecto                             | Detalles                                                                                     |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| **Tiempo de Finalización**          | C: 11, F: 14, A: 8, D: 20, E: 28, B: 41                                                     |
| **Tiempo de Espera Promedio**      | (4 + 5 + 0 + 10 + 14 + 26) / 6 = 9.17                                                      |
| **Tiempo de Retorno Promedio**     | (7 + 8 + 8 + 16 + 22 + 39) / 6 = 16                                                        |
| **Ventajas**                        |                                                                                              |
| Interactividad                      | Permite que todos los procesos reciban tiempo de CPU, lo cual es ideal para sistemas interactivos donde la respuesta rápida es crucial. |
| Simplicidad                         | Es fácil de implementar y entender.                                                         |
| Justicia                            | Todos los procesos tienen la misma oportunidad de ejecutarse, evitando que un proceso monopolice el CPU. |
| **Desventajas**                     |                                                                                              |
| Alto Tiempo de Espera              | El tiempo de espera puede ser alto, especialmente para procesos de larga duración, debido a la fragmentación del tiempo de CPU. |
| Overhead                            | Con quantum de 1, hay un alto número de cambios de contexto, lo que puede llevar a un desperdicio de tiempo. |

## 2. Round Robin con Quantum = 3

| Aspecto                             | Detalles                                                                                     |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| **Tiempo de Finalización**          | A: 8, B: 41, C: 11, D: 20, E: 28, F: 14                                                     |
| **Tiempo de Espera Promedio**      | (0 + 26 + 4 + 10 + 14 + 5) / 6 = 9.17                                                      |
| **Tiempo de Retorno Promedio**     | (8 + 39 + 7 + 16 + 22 + 8) / 6 = 16                                                        |
| **Ventajas**                        |                                                                                              |
| Mejor Rendimiento                   | Un quantum mayor reduce el número de cambios de contexto, lo que puede mejorar el rendimiento general. |
| Equilibrio                          | Mantiene la equidad, permitiendo que los procesos se ejecuten en intervalos más largos, lo que puede reducir el tiempo de espera. |
| **Desventajas**                     |                                                                                              |
| No Ideal para Procesos Cortos      | Puede ser menos eficiente para procesos cortos que podrían completarse rápidamente si se les da tiempo suficiente. |
| Complejidad en Ajustes             | Elegir el tamaño de quantum correcto puede ser complicado y depende de la carga de trabajo. |

## 3. Proceso Más Corto a Continuación (SJF)

| Aspecto                             | Detalles                                                                                     |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| **Tiempo de Finalización**          | A: 8, C: 11, F: 14, D: 20, E: 28, B: 41                                                     |
| **Tiempo de Espera Promedio**      | (0 + 4 + 5 + 10 + 14 + 26) / 6 = 9.17                                                      |
| **Tiempo de Retorno Promedio**     | (8 + 7 + 8 + 16 + 22 + 39) / 6 = 16                                                        |
| **Ventajas**                        |                                                                                              |
| Minimiza el Tiempo de Espera       | SJF generalmente tiene el menor tiempo de espera promedio, lo que mejora la eficiencia de CPU. |
| Ideal para Procesos Cortos         | Proporciona un rendimiento superior para cargas de trabajo con procesos de corta duración. |
| **Desventajas**                     |                                                                                              |
| Injusticia                          | Los procesos largos pueden quedar en espera indefinidamente (starvation), ya que los procesos cortos siempre tienen prioridad. |
| Conocimiento del Tiempo de Ejecución| SJF requiere que se conozcan de antemano los tiempos de ejecución de los procesos, lo cual no siempre es posible. |
