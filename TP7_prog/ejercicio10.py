original = {"Argentina": "CABA", "Chile": "Santiago", "Bután": "Timbu"}
invertido = {}

paises = list(original.keys())
capitales = list(original.values())

for i in range(len(paises)):
    invertido[capitales[i]] = paises[i]

print(invertido)