""" Altere o programa de cálculo dos números primos, informando, caso o
número não seja primo, por quais número ele é divisível. """

cont = 0
n = int(input("Informe um número: "))

for i in range(1,n+1):
    if n % i == 0: cont+=1
if cont>=3: 
    print("Não é primo e é divisível pelo seguintes números:")
    for i in range(1,n+1):
        if n % i == 0: print(f"{i}", end=" ")
else: print("É primo")
