""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
 a. valor do salário bruto. 

a. + Salário Bruto : R$ 
b. - IR (11%) : R$ 
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$ 
e. + Salário Liquido : R$ 
Obs.: Salário Bruto - Descontos = Salário Líquido.
 """

salarioHora = float(input("Informe quanto você ganha por hora: "))
horasMes = float(input("Informe quantas horas são trabalhadas por mês: "))
salarioBruto = salarioHora*horasMes
ir = salarioBruto*(11/100)
inss = salarioBruto*(8/100)
sindicato = salarioBruto*(5/100)
salarioLiquido = salarioBruto-(ir+inss+sindicato)
print(f""" 

a. + Salário Bruto : R$ {salarioBruto}
b. - IR (11%) : R$ {ir}
c. - INSS (8%) : R$ {inss}
d. - Sindicato (5%) : R$ {sindicato}  
e. + Salário Liquido : R$ {salarioLiquido}

""")