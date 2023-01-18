""" Depois da liberação do governo para as mensalidades dos planos de saúde, as pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Faça um programa que entre com o nome e a idade de uma pessoa e imprima o nome e o valor que ela deverá pagar.
               Idade                                               Valor 
              Até 10 anos                                     R$30,00 
             Acima de 10 até 29 anos            R$60,00 
             Acima de 29 até 45 anos           R$120,00 
             Acima de 45 até 59 anos           R$150,00 
             Acima de 59 até 65 anos           R$250,00
             Maior que 65 anos                       R$400,00
 """
nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))

if idade <= 10:
    print(f"{nome} deverá pagar R$ 30,00")
elif idade <= 29:
    print(f"{nome} deverá pagar R$ 60,00")
elif idade <= 45:
    print(f"{nome} deverá pagar R$ 120,00")
elif idade <= 59:
    print(f"{nome} deverá pagar R$ 150,00")
elif idade <= 65:
    print(f"{nome} deverá pagar R$ 250,00")
else:
    print(f"{nome} deverá pagar R$ 400,00")    