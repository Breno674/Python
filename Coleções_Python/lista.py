"""
Listas

Listas em python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tambem de podemos colocar QUALQUER tipo de dado.

 - Dinâmico: Não possui tamanho fixo; ou seja, podemos criar lista e simplesmente ir adicionando elementos;
 - Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipoo de dado;

As Listas em python são representados por colchetes: []

#Podemos facilmente checar se determinado valor está contido na lista

num = 8 

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#Podemos facilmente contar o número de ocorrencias de uma valor en uma lista
print(lista1.count(1))
print(lista2.count('E'))

#Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

OBS: com append, nós só conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([2,6,8])  # coloca a lista com elemento único (sublista)
print(lista1)

if [2,6,8] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # coloca cada elemento da lista como valor adicional á lista
print(lista1)

#Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)

lista5.reverse()
lista2.reverse()

print(lista2)
print(lista5)
"""

type([])

lista1 = [1, 99, 4, 5, 7, 90]

lista2 = ['G', 'E', 'E', 'K', ' ', 'U']

lista3 = []

lista4 = list(range(11))

lista5 = list('Breno Oliveira')

#podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo índice
lista5.pop(2)
print(lista5)




