"""
Escopo de variáveis

Dois casos de escopo: 

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

para declarar variáceis em python fazemos:

nome_da_variavel = valor_da_variavel

python é uma linguagem de tipagem dinâmiva. Isso significa que 
ao declaramos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuímos o valor à mesma.

"""

numero = 42
print(numero)
print(type(numero))

numero = "Breno"
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10
    print(novo)