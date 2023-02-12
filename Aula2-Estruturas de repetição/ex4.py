""" Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. """

fator = int(input("Informe o número que deseja tirar o fatorial: "))
valor = fator
print(f"{fator}!=", end="")
for f in range(fator,0,-1):
    print(f"{fator}",end=".")
    valor*=fator-1
    fator-=1
    if fator==1:
        print(f"1={valor}")
        break

    
  