"""
Funções com retorno

numeros = [ 1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret}')

ret_pr = print(numeros)

print(f' retorno de print: {ret_pr}')

OBS: Em Python quando a função não retorna nenhum valor, o retorno é none

OBS: Funções Python que retonarm valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamo necessariamente criar uma variável para receber o retorno de uma função, podemos passar
a execução de uma função para outras funções

def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'retorno {ret}')
print(f'retorno: {quadrado_de_7() + 1}')

# Refatorando a função oi:

def diz_oi():
    return 'Oi '


alguem = 'Pedro!'

print(diz_oi() + alguem)


OBS: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execuçãod a função.
2- Podemos ter em uma função, diferentes returns;
3- Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores.

# Exemplo 1 - Finalizar a função

def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi '
    print('Estou sendo executado após o retorno')


print(diz_oi())


# Exemplo 2 - Diferentes returns

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores.

def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print(outra_funcao())

# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""

# Erros comuns na utilização de um retorno, com codificação desnecessária.

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())




