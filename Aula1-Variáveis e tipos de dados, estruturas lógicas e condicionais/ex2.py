""" Faça um programa em python que permita entrar com o ano de nascimento da pessoa e com o ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de verificar se o ano de nascimento informado é válido. """

anoAtual = int(input("Informe o ano atual: "))
anoNascimento = int(input("Informe o ano de nascimento: "))
mesNascimento = int(input("Informe um mês de nascimento: "))
mesAtual = int(input("Informe o mês atual: "))
diaNascimento = int(input("Informe o dia de nascimento: "))
diaAtual = int(input("Informe o dia atual: "))
idade = anoAtual-anoNascimento

if anoNascimento<1900:
    print("Data de nascimento inválida")
elif mesNascimento < mesAtual:
    print(f"Sua idade é {idade}")
elif mesNascimento > mesAtual:
    idade-=1
    print(f"Sua idade é {idade}")
elif mesNascimento == mesAtual:
    if diaNascimento <= diaAtual:
        print(f"Sua idade é {idade}")
    else:
        idade-=1
        print(f"Sua idade é {idade}")
            