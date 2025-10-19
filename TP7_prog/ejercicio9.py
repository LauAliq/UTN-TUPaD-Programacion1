agenda = {("sábado", "20:00"): "casamiento", ("sábado", "10:00"): "partido", ("lunes", "8:00"): "examen"}

dias_y_horas = list(agenda.keys())
print(f"Tienes actividades el {dias_y_horas[0][0]} a las {dias_y_horas[0][1]}, el {dias_y_horas[1][0]} a las {dias_y_horas[1][1]} y el {dias_y_horas[2][0]} a las {dias_y_horas[2][1]}.")
dia = input("¿Qué actividad desea consultar? Ingrese día: ")
hora = input("Ingrese hora (ejemplo: 20:00): ")
dia_y_hora = (dia.lower(), hora)
if dia_y_hora not in agenda:
    print("No tienes actividades ese día a esa hora.")
else:
    print(f"Tienes {agenda[dia_y_hora]} ese día a esa hora.")