""" Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1. """

cont = 0 

numero = int(input("Informe um numero: "))
for p in range(1,numero+1):
    if numero % p == 0: cont+=1
if cont >= 3:
    print("Não é primo")
else:
    print("É um número primo")