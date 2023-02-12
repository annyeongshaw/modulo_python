""" Acesse o Site IMDb (www.imdb.com)
Pesquisa o NOME e a NOTA de 5 filmes.
Depois disso, crie um programa para armazenar as informações e
responder:
a) qual filme possui a menor nota
b) qual filme possui a maior nota
c) qual a média de notas dos filmes
d) mostrar em tela a lista em ordem crescente e decrescente (filme e nota)"""

filmes = ["Shazam","Um sonho de liberdade","O poderoso chefão","Pulp fiction","Clube da luta"]
notas = [7.0,9.2,9.2,8.8,8.7]; 
maior = 0
menor = 10
for i in range(5):
    if notas[i] <= menor:
        menor=notas[i]
        continue
    elif notas[i] >= maior:
        maior = notas[i]
media = sum(notas)/5
print(f"""
a) qual filme possui a menor nota:{menor}
b) qual filme possui a maior nota: {maior}
c) qual a média de notas dos filmes: {media}
d) mostrar em tela a lista em ordem crescente e decrescente (filme e nota): """)
for f,m in zip(filmes,notas):
    print(f"{f}: {m}")