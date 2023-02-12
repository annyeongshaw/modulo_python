""" Para finalizar, utilize o programa anterior e imprima os
valores armazenados nas listas da seguinte forma:

Nome: Júnior  Idade: 31 anos """

nomes = []
idade = []
for i in range(5):
    nomes.append(input("Informe o nome da pessoa: "))
    for z in range(1):
        idade.append(int(input("Informe a idade da pessoa: ")))
print("\n"*10)

for n,i in zip(nomes,idade):
    print(f"Nome: {n}  Idade: {i} anos")