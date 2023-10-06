"""
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor de booleano é invertido, ou seja, se for True, vira False, se for False vira True
"""

ativo = True
logado = False

if ativo or logado:
    print('Bem-vimdo usuário!')
else:
    print('você precisa ativar sua conta. Por favor, cheque seu e-mail')