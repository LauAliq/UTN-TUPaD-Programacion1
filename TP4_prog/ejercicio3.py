inf: int = int(input("Ingrese una cota inferior: "))
sup: int = int(input("Ingrese una cota superior: "))
suma: int = 0
for i in range(inf + 1, sup):
    suma += i

print(f"La suma de los números estrictamente entre {inf} y {sup} es {suma}.")