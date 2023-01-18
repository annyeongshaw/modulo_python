""" Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido; """

dia = int(input("""
Informe o número correspondente ao dia da semana:
1- Domingo
2- Segunda-feira
3- Terça-feira
4- Quarta-feira
5- Quinta-feira
6- Sexta-feira
7- Sábado
Digite o número correspondente aqui: """))
print("-"*50)
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Valor inválido")
print("-"*50)