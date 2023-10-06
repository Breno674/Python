nome = 'Breno Oliveira'
lista = [1,3,5,7,9]
numeros = range(1, 10)

# Exemplo de for 1 (iterando em uma string)
"""
for letra in nome:
    print(letra)
"""

#Exemplo de for 2 (iterando sobre uma lista)
"""
for numero in lista:
    print(numero)
"""

#Exemplo de for 3 (iterando sobre um range)
"""
for numero in range(1, 10):
    print(numero)
"""

"""
for _, letra in enumerate(nome):
    print(letra)
"""

"""
for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe 0 {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


nome = 'Breno Oliveira'

for letra in nome:
    print(letra, end='')

"""
# Original: U+1F970
# Modificado: U0001F970
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F970' * num)
