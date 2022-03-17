"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Preinindo assim que o programa pare
de funcioanr e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando erro genérico
try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek, caso você encontre erros. imprima a mensagem de erro.

# Exemplo 2 - Tratando erro genérico
try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função len(5), caso você encontre erros. imprima a mensagem de erro.

# Exemplo 4 - tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - tratando um erro específico

try:
    len(5)
except TypeError as err:
    print(f'Você está utilizando uma função inexistente, logo gerou o seguinte erro {err}')

# Exemplo 6

try:
    # len(5)
    # geek()
    print('Geek'[9])
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err1:
    print(f'Deu TypeError: {err1}')
except:
    print('Deu um erro diferente')

# Exemplo 7
def pega_valor(dicionario, chave):
    # forma com erro
    # return dicionario[chave]

    # Erro tratado:
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except:
        return None


dic = {'nome': 'geek'}

print(pega_valor(dic, 'game'))

"""



