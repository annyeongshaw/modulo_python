""" Desenvolva um gerador de tabuada, capaz de gerar a tabuada de SOMA de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. """

numero = int(input("Informe o número que deseja ver a tabuada: "))
for i in range(1,11):
    print(f"{numero} + {i} = {numero+i}")
    
