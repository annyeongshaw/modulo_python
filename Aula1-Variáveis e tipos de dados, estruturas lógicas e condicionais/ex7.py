""" Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """

letra = str(input("Informe um letra para análise: ").lower())
if letra in ("aeiou"):
    print("É uma vogal")
else:
    print("É uma consoante")