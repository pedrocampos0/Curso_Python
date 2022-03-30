"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    -not
Operadores binários:
    -and, or, is

Regras de funcionamento:

Para o 'and', ambos valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, se for True, vira False e vice-versa
Para o 'is', o valor é comparado com um segundo

"""
ativo = True
logado = True

'''if ativo and logado:
    print('Você precisca ativar sua conta por favor cheque o seu e-mail')
else:
    print('Usuário ativo e logado no sistema')

# ativo é True?
print(ativo is True)'''


a1 = 8
a2 = 5
a3 = 10
for i in range(1,4):
    for j in range(2,5):
        a3 = a3 + 2*a2 - a1
    a1 = a1-1

print(a3)