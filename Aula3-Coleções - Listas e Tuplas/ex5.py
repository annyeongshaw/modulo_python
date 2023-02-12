""" Escreva um programa que peça ao usuário que informe 10 números inteiros e adicione-os a uma lista. Em seguida, percorra toda a lista removendo todos os números pares. Por fim, apresente a lista na tela."""
numeros=[]
pares = []

for i in range(10):
    numeros.append(int(input("Informe o número: ")))
for n,z in enumerate(numeros):
    if z%2 == 0:
        pares.append(z)
print("\n"*10)
print("Os números pares da lista são: ")
for i in pares:
    print(f"{i}")

