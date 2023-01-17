#Desafio: Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Álcool:
#  Até 20 litros: desconto de 3% por litro
# Acima de 20 litros: Desconto de 5% por litro 99.
# Gasolina:
# Até 20 litros: desconto de 4% por litro
# Acima de 20 litros, desconto de 6% por litro
# Valores dos Combustivel:
# Alcool: R$ 5,40
# Gasolina: R$ 4,70
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool. G-gasolina), calcule e imprima o valor a ser pago pelo cliente.

print("-"*50)
print("""
Álcool:
Até 20 litros: desconto de 3% por litro
Acima de 20 litros: Desconto de 5% por litro 

Gasolina:
Até 20 litros: desconto de 4% por litro
Acima de 20 litros, desconto de 6% por litro

Valores dos Combustivel:
Alcool: R$ 5,40
Gasolina: R$ 4,70 """)
print("-"*50)
pay=0
quantity = float(input("Informe a quantidade de combustível em litros: "))
tipo = str(input("Qual o tipo de combustível: A-álcool ou G-gasolina").lower())

if quantity <= 20 and tipo == "a":
    pay = quantity*5.238
    print(f"O valor a pagar é R$ {pay}")
elif quantity > 20 and tipo == "a":
    pay = (20*5.238)+((quantity-20)*5.13)
    print(f"O valor a pagar é R$ {pay}")
elif quantity <= 20 and tipo == "g":
    pay = quantity*4.512
    print(f"O valor a pagar é R$ {pay}")
else:
    pay = (20*4.512)+((quantity-20)*4.418)
    print(f"O valor a pagar é R$ {pay}")
