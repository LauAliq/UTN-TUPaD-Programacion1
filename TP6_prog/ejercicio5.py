def  segundos_a_horas(segundos):
    print(f"{segundos} segundos son {round(segundos / 3600, 2)} horas.")

segundos_u = int(input("¿Cuántos segundos quieres?: "))
segundos_a_horas(segundos_u)