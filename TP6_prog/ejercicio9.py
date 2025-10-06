def celsius_a_fahrenheit(celsius):
    print(f"{celsius}°C es igual a {round(celsius * 9 / 5 + 32)}°F")

celsius_u = float(input("Ingrese una temperatura en grados celsius: "))

celsius_a_fahrenheit(celsius_u)