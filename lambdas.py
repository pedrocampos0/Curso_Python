"""
Utilizando lambdas

Conhecidas por expressões lambdas, são funções sem nome ou seja, funções anônimas.

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão lambda
lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo(' angeline', 'JOLIE'))
print(nome_completo(' FELICITY        ', '  JONES         '))

# Em funções python podemos ter nenhuma ou várias entradas. Em lambdas também.

amar = lambda: 'Como não amar Python'

uma = lambda x: 3*x+1

duas = lambda x, y: (x*y)** 0.5

tres = lambda x, y, z: 3/(1/x+1/y+1/z)

#n = lambda x1, x2, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: Se passarmos mais parâmetros ou mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
   retorna a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))

"""


