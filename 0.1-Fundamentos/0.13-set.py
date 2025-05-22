frutasSet = {"Maça", "Banana", "Limão", "Abacaxi"}

print(type(frutasSet))

print(len(frutasSet))

exempleSet = {"Uva", True, 1, 8.0}
print(exempleSet)
frutasSet.update(exempleSet)
print(frutasSet)

frutasSet.remove(True)
frutasSet.remove(8.0)

print(frutasSet)

