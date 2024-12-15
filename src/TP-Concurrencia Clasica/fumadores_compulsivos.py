import threading
import random
import time

# Semáforos y variables compartidas
mutex = threading.Semaphore(1)  # Para proteger el acceso a la mesa
ingredients_on_table = []  # Ingredientes en la mesa
semaphore = threading.Semaphore(0)  # Para que los fumadores esperen

# Ingredientes disponibles
TABACCO = 'tabaco'
PAPER = 'papel'
MATCHES = 'fósforos'

# Fumadores
class Smoker(threading.Thread):
    def __init__(self, ingredient):
        super().__init__()
        self.ingredient = ingredient

    def run(self):
        while True:
            semaphore.acquire()  # Espera a que haya ingredientes en la mesa
            # Intenta fumar
            if (self.ingredient == TABACCO and PAPER in ingredients_on_table and MATCHES in ingredients_on_table) or \
               (self.ingredient == PAPER and TABACCO in ingredients_on_table and MATCHES in ingredients_on_table) or \
               (self.ingredient == MATCHES and TABACCO in ingredients_on_table and PAPER in ingredients_on_table):
                print(f'Fumador con {self.ingredient} está fumando.')
                time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo de fumar
                print(f'Fumador con {self.ingredient} ha terminado de fumar.')
                # Limpia la mesa
                ingredients_on_table.clear()
                mutex.release()  # Permite que el productor ponga más ingredientes

class Producer(threading.Thread):
    def run(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simula tiempo de producción
            # Produce dos ingredientes al azar
            ingredients = [TABACCO, PAPER, MATCHES]
            random.shuffle(ingredients)
            ingredients_on_table.extend(ingredients[:2])  # Toma los dos primeros
            print(f'Productor ha puesto en la mesa: {ingredients_on_table}')
            semaphore.release()  # Notifica a los fumadores que hay ingredientes
            mutex.acquire()  # Espera a que los fumadores terminen

# Inicializa los fumadores
smokers = [
    Smoker(TABACCO),
    Smoker(PAPER),
    Smoker(MATCHES)
]

# Inicializa el productor
producer = Producer()

# Inicia los hilos
producer.start()
for smoker in smokers:
    smoker.start()

# Mantiene los hilos en ejecución
for smoker in smokers:
    smoker.join()
producer.join()