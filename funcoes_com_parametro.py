"""
Funções com Parãmetro de entrada

- Funções que recebnem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função. já sabemos que temos funlçies que:
- Não possuem entrada;
- Não possuem sáida;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""


# Refatorando uma função:

def quadrado(numero):
    return numero * numero


print(quadrado(2))


def cantar_parabens(aniversariante):
    print('parabéns p vc')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva o {aniversariante}')


cantar_parabens('marcos')


def soma(a, b):
    return a + b

print(soma(1, 2))



def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angeline','Jolie'))

# A ordem dos parâmetros importa:

nome = 'felicity'
sobrenome = 'jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados ( Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(nome='angelina', sobrenome='jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))


# Erros comuns na utilização do return:
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))