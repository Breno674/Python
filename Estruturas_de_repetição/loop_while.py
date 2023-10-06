"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco de while será enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde resultado é verdadeiro ou falso.

Exemplo: 

num = 5
num < 5

Exemplo 1 

numero = 0

while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante que cuidamos de critério de parada para não causar um loop infinito.
"""

# Exemplo 2 

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Breno? ')
