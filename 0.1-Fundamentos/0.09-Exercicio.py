primeiroNome = str(input("Seu primeiro nome: "))
segundoNome = str(input("Seu segundo nome: "))

print(segundoNome, primeiroNome)

frase = str(input("Digite uma palavra: "))
print(frase[::-1])

palavra = str(input("Digite uma palavra: "))

print(f'A palavra {palavra} é um palíndromo {palavra == palavra[::-1]}')

