"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1  - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis, ou seja, ao se criar uma tupla ela não muda.
Toda operação com tuplas gera uma nova tupla.

# OBS 1: As tuplas são representadas por parênteses, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# OBS 2: Tuplas com 1 elemento:

tupla3 = (4)  # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,)
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do ().

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

tupla = tuple(range(1, 11))
print(tupla)

print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um númerro diferente de elemnetos para desempacotar.

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis

# Soma*, Valor máximo*, Valor mínimo* e Tamanho

tupla = (1, 2, 3, 4, 5, 6)

print(f'A soma da tupla é {sum(tupla)}, o valor máx é {max(tupla)}, o mínimo é {min(tupla)} e o tamanho é {len(tupla)}')

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)


tupla1 = tupla1 + tupla2
print(tupla1)

# Verificar se determinado elem,ento está conditda na tupla

tupla = (1, 2, 3)

print(32 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)


for indice, valor in enumerate(tupla):
    print(f'o indice {indice} tem o valor {valor}')

# Contando os elementos de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses(i))
    i = i + 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado um ValueError.

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que nao precisarmos utilizar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro',  'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

# Slicing
# Tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro, isso porque trabalhar com elementos imutaveis traz segurança para o código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

"""


