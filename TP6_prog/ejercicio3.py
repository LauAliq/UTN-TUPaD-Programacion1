def  informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre_u = input("¿Cuál es tu nombre?: ")
apellido_u = input("¿Cuál es tu apellido?: ")
edad_u = input("¿Cuántos años tienes?: ")
residencia_u = input("¿En qué país vives?: ")

informacion_personal(nombre_u, apellido_u, edad_u, residencia_u)