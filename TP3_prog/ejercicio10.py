# Definimos las variables hemis, mes, dia y dict, las cuales serán de utilidad en el código.

hemis: str = input("Por favor, ingrese una N si se encuentra en el hemisferio norte o una S si se encuentra en el hemisferio sur: ").title()
mes: str = input("Por favor, ingrese el mes del año en el que se encuentra: ").title()
dia: str = (input("Por favor, ingrese qué día es hoy (número entre 1 y 31): "))
dct: dict = {"Enero": "1",
        "Febrero": "2",
        "Marzo": "3",
        "Abril": "4",
        "Mayo": "5",
        "Junio": "6",
        "Julio": "7",
        "Agosto": "8",
        "Septiembre": "9",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"}

# Definimos la variable fecha, la cual contiene la información sobre en qué día y en qué mes está el usuario.

fecha: int = int(dct[mes] + dia)

# Si estamos en el hemisferio sur:

if hemis == "S":
    if fecha > 1220 or (fecha > 0 and fecha <= 320):
        print("Estás en verano.")
    elif fecha > 320 and fecha <= 620:
        print("Estás en otoño.")
    elif fecha > 620 and fecha <= 920:
        print("Estás en invierno.")
    elif fecha > 920 and fecha <= 1220:
        print("Estás en primavera.")
    else:
        pass

# Si estamos en el hemisferio norte:

elif hemis == "N":
    if fecha > 1220 or (fecha > 0 and fecha <= 320):
        print("Estás en invierno.")
    elif fecha > 320 and fecha <= 620:
        print("Estás en primavera.")
    elif fecha > 620 and fecha <= 920:
        print("Estás en verano.")
    elif fecha > 920 and fecha <= 1220:
        print("Estás en otoño.")
    else:
        pass

# Si no estamos en ningún hemisferio:

else:
    print("No se seleccionó ningún hemisferio.")