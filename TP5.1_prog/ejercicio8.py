from random import randint

lista: list = [[randint(1, 10) for i in range(3)] for j in range(5)]
print(lista)

prom_e = [0, 0, 0, 0, 0]

prom_m = [0, 0, 0]

for j in range(len(lista)):
    for i in range(len(lista[j])):
        prom_e[j] += lista[j][i] / 3
        prom_m[i] += lista[j][i] / 5



print(f"Los promedios de cada estudiante fueron: {prom_e}, mientras que los de cada materia fueron {prom_m}.")
    