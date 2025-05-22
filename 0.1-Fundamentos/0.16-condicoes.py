nome = input("Digite seu nome: ")
idade = int(input("Digite o seu ano de nascimento: "))
altura = float(input("Digite sua altura: "))

if (2025 - idade) > 10 and altura < 1.90:
    print("Você é bem alto")
elif (2025 - idade) > 18 and altura < 1.70:
    print("Você é baixo")
else:
    print("Altura mediana")
