# Importamos la función randint

from random import randint

# Creamos la lista de siete números aleatorios y la imprimimos

lista: list = [randint(1, 100) for i in range(7)]
print(f"La lista original es {lista}.")

# Quitamos el último elemento de la lista y lo guardamos en una variable

ultimo: int = lista.pop()

# Convertimos dicho elemento a una variable tipo lista

primero: list = [ultimo]

# Sumamos dicha lista con la lista original e imprimimos el resultado

lista = primero + lista
print(f"Ahora la lista es {lista}.")
