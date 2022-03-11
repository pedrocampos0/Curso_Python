"""
**kwargs

O kwargs exique que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwards não são obrigatórios

cores_favoritas()

cores_favoritas(geek='navy')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é . . . '


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções podemos ter (NESTA ORDEM):

- parâmetros obrigatórios
- *args
- Parametros default
-**kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(9, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='não', você='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

"""

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome':'jones'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)


dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

#OBS: Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros de uma função

# dicionario = dict(d=1, e=2, f=3) TypeError
# print(soma_multiplos_numeros(**dicionario))

