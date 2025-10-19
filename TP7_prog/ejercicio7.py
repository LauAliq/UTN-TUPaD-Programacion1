aprobados_1 = {"Jero", "Fer", "Bauti", "Franco", "Nahuel"}
aprobados_2 = {"Jero", "Fer", "Nahuel", "Facu", "Mateo", "Ramiro"}
aprobaron_ambos = aprobados_1 & aprobados_2
aprobaron_1 = aprobados_1 ^ aprobados_2
aprobaron_al_menos_1 = aprobados_1 | aprobados_2
print(f"Aprobaron los dos parciales {aprobaron_ambos}, aprobaron uno sólo {aprobaron_1} y aprobaron al menos uno {aprobaron_al_menos_1}.")
