""" Reescreva o programa da questão anterior, mas agora armazenando os nomes e idades em duas listas diferentes.Por fim, também apresente na tela as duas listas obtidas. """

nomes = []
idade = []
for i in range(5):
    nomes.append(input("Informe o nome da pessoa: "))
    for z in range(1):
        idade.append(int(input("Informe a idade da pessoa: ")))
print("\n"*10)

for n,i in zip(nomes,idade):
    print(f"{n} tem {i} anos")