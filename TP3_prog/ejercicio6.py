# Se importan algunas funciones de utilidad.

from statistics import mode, median, mean
from random import randint

# Se crea una lista de 50 números enteros aleatorios entre el 1 y el 100.

numeros_aleatorios = [randint(1, 100) for i in range(50)]

# Se definen las variables moda, media y mediana, según la lista creada anteriormente.

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

# Se imprime por pantalla si hay o no sesgo en los valores de la lista, y hacia dónde.

if media > mediana > moda:
    print("Hay un sesgo positivo.")
elif media < mediana < moda:
    print("Hay un sesgo negativo.")
else:
    print("No hay sesgo.")