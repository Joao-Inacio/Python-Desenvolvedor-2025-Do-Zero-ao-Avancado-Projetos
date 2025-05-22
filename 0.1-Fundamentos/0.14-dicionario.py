pessoa = {
    "nome": "João",
    "idade": 25,
    "altura": 1.75,
    "vivo": True
}
print(pessoa)
print(len(pessoa))
print(type(pessoa))

print(pessoa["altura"])
print(pessoa.get("idade"))

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa["Comidas"] = ["Macarronada", "Suco"]
print(pessoa)

pessoa.update({"idade": 26})
print(pessoa)

pessoa.pop("Comidas")
print(pessoa)
