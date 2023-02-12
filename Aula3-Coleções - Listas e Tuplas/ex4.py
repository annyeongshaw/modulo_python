""" Escreva um programa que peça o nome e a média de 10 alunos, Adicione à uma lista apenas os nomes dos alunos com média maior do que sete. Imprima em tela a lista dos aprovados. """
aprovados = []
nome = []
media = []

for i in range(10):
    nome.append(input("Informe o nome do aluno: "))
    for z in range(1):
        media.append(float(input("Informe a média do aluno: ")))
        if media[i] >= 7:
            aprovados.append(nome[i])

for i,a in enumerate(aprovados,start = 1):
    print(f"{i}° {a} Aprovado")

