pessoas = {
    "João": {
        "sobrenome": "Inácio",
        "idade": 25,
        "altura": 1.75,
        "vivo": True
    },
    "Lucas": {
        "sobrenome": "Arruda",
        "idade": 25,
        "altura": 1.72,
        "vivo": True
    },
    "Maria": {
        "sobrenome": "Alana",
        "idade": 25,
        "altura": 1.65,
        "vivo": True
    }
}

print(pessoas)

print(pessoas["Lucas"]['idade'])
pessoas["João"]["idade"] = 25
print(pessoas)

del pessoas["João"]
print(pessoas)
