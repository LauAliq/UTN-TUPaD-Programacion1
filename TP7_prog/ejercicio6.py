def es_float_valido(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

notas_de_todos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno al que desea cargarle las notas: ")
    while nombre in notas_de_todos:
        nombre = input("Ya le has cargado las notas a este alumno, prueba con otro: ")
    notas = []
    for i in range(3):
        nota = input(f"Ingrese la nota del parcial {i + 1} de {nombre}: ")
        while nota == "" or not es_float_valido(nota):
            nota = input("Por favor, ingrese una nota válida: ")
        notas.append(float(nota))
    notas_de_todos[nombre] = tuple(notas)

print(notas_de_todos)
solo_notas = list(notas_de_todos.values())
solo_alumnos = list(notas_de_todos.keys())
for i in range(3):
    promedio = 0
    for j in range(3):
        promedio += float(solo_notas[i][j])
    promedio /= 3
    print(f"El promedio de notas de {solo_alumnos[i]} es {promedio}.")