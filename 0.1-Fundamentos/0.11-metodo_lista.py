listaFruta = ["Maça", "Banana", "Limão", "Abacaxi"]

print(len(listaFruta))
print(listaFruta.index("Limão"))

listaFruta.append("Goiaba")
print(listaFruta)

listaFruta.sort()
print(listaFruta)

frutascopy = listaFruta.copy()
frutascopy.remove("Maça")

print(listaFruta)
print(frutascopy)


