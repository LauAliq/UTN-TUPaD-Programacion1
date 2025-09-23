from random import randint

lista = [randint(1, 100) for i in range(7)]
print(f"La lista original es {lista}.")
ultimo = lista.pop()
primero = [ultimo]
lista = primero + lista
print(f"Ahora la lista es {lista}.")
