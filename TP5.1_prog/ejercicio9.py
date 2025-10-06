tateti: list = [[" ", "A", "B", "C"], ["1", "-", "-", "-"], ["2", "-", "-", "-"], ["3", "-", "-", "-"]]
for i in range(len(tateti)):
    for j in range(len(tateti[i])):
        print(tateti[i][j], end = " ")
    print()

bandera: bool = True

while bandera:

    guion_1: bool = True
    guion_2: bool = True

    while guion_1:
        fila: str = input("Jugador 1 (X), ingresa la fila en la que desea colocar una X: ")
        while fila not in ["1", "2", "3"]:
            fila = input("Intenta con una fila válida: ")
        fila = int(fila)
    
        columna: str = input("Jugador 1 (X), ingresa la columna en la que desea colocar una X: ")
        while columna.upper() not in ["A", "B", "C"]:
            columna = input("Intenta con una columna válida: ")
        if columna.upper() == "A":
            columna = 1
        elif columna.upper() == "B":
            columna = 2
        else:
            columna = 3
        
        if tateti[fila][columna] == "-":
            tateti[fila][columna] = "X"
            guion_1 = False
            for i in range(len(tateti)):
                for j in range(len(tateti[i])):
                    print(tateti[i][j], end = " ")
                print()
        else:
            print("Intenta de nuevo, esa casilla ya está ocupada.")
        
        for i in range(len(tateti[0])):
            if (tateti[i][1] == tateti[i][2] == tateti[i][3] == "X") or (tateti[1][i] == tateti[2][i] == tateti[3][i] == "X") or (tateti[1][1] == tateti[2][2] == tateti[3][3] == "X") or (tateti[1][3] == tateti[2][2] == tateti[3][1] == "X"):
                bandera = False
                guion_2 = False
                print("Ha ganado el jugador 1 (X)!")
            
        if "-" not in tateti[1] and "-" not in tateti[2] and "-" not in tateti[3] and bandera:
            bandera = False
            guion_2 = False
            print("Se quedaron sin espacio! El juego termina en empate.")

    while guion_2:
        fila = input("Jugador 2 (O), ingresa la fila en la que desea colocar una O: ")
        while fila not in ["1", "2", "3"]:
            fila = input("Intenta con una fila válida: ")
        fila = int(fila)
        
        columna = input("Jugador 2 (O), ingresa la columna en la que desea colocar una O: ")
        while columna.upper() not in ["A", "B", "C"]:
            columna = input("Intenta con una columna válida: ")
        if columna.upper() == "A":
            columna = 1
        elif columna.upper() == "B":
            columna = 2
        else:
            columna = 3
        
        if tateti[fila][columna] == "-":
            tateti[fila][columna] = "O"
            guion_2 = False
            for i in range(len(tateti)):
                for j in range(len(tateti[i])):
                    print(tateti[i][j], end = " ")
                print()

        else:
            print("Intenta de nuevo, esa casilla ya está ocupada.")

        for i in range(len(tateti[0])):
            if (tateti[i][1] == tateti[i][2] == tateti[i][3] == "O") or (tateti[1][i] == tateti[2][i] == tateti[3][i] == "O") or (tateti[1][1] == tateti[2][2] == tateti[3][3] == "O") or (tateti[1][3] == tateti[2][2] == tateti[3][1] == "O"):
                bandera = False
                guion_1 = False
                print("Ha ganado el jugador 2 (O)!")

    


