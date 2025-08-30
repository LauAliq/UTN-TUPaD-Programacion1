sup: int = int(input("Ingrese una cota superior: "))
suma: int = 0
for i in range(0, sup + 1):
    suma += i

print(f"La suma de los primeros {sup} números naturales es {suma}.")