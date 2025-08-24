# Se define la variable pal, la cual contiene una cadena de caracteres.

pal = input("Ingrese una palabra: ")

# Si la palabra guardada en la variable pal termina en vocal, se imprime con un signo de exclamación, si no, se imprime tal cual fue escrita por el usuario.

if pal[-1].lower() in "aeiou":
    print(pal + "!")
else:
    print(pal)