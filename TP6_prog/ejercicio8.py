def calcular_imc(peso, altura):
    print(f"Tu IMC es igual a {round(peso / (altura ** 2), 2)}")

peso_u = float(input("¿Cuánto pesas en kilogramos?: "))
altura_u = float(input("¿Cuánto mides en metros?: "))

calcular_imc(peso_u, altura_u)