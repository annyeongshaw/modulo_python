""" Escreva um programa que solicite ao usuário o nome de 5 pessoas e adicione-os à uma lista. Por fim imprima a lista na tela. """

nomes = []
for i in range(5):
    nomes.append(input("Informe o nome da pessoa: "))
print("\n"*10)
for i,n in enumerate(nomes, start=1):
    print(f"{i}°: {n}")