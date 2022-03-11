"""
Listas

Listas em Python funcionam como vetores/matrizes (arrayz) em outras linguagens, com a diferença de serem dinâmicos e
também de podermos colocar QUALQUER tipo de dado.

- Linguagens C/Java:
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se vocÇe criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá SEMPRE no máximo 5 valores.

Já em Python

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 7]

lista2 = ['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek university')

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em lista

'''
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
'''
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])  # Coloca a lista como elemento único SUBLISTA
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a possição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntas duas listas

#lista1.extend(lista2)
lista1 = lista1 + lista2
print(lista1)

print(lista1, lista2)

# Forma 1
# lista1.reverse()
# lista2.reverse()

# Forma 2
print(lista1[::-1], lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro de uma lista

print(len(lista1))

# Podemos facilmente remover o último elemento de uma lista

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado teremos o erro IndexError

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista
#Exemplo 1

curso = 'Programação em Python: essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas.

#Exemplo 2

curso = 'Programação,em,Python:,essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

lsita6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 4535454545]

# Iterando sobre listas
# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas:
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Fazemos acesso aos elementos de forma indexada

#       [   0         1        2         3   ]
#       [  -4        -3       -2        -1   ]
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[1])
print(cores[2])

#Fazemos acesso aos elementos de forma indexada
print(cores[-1])
print(cores[-2])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for:
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))

# Em qual indice da lista está o valor 9?
print(numeros.index(9))

# Em qual indice da lista está o valor 5?
print(numeros.index(5))  # acha a primeira ocorrência do valor


# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar

print(numeros.index(5, 1))  # buscando a partir do índice 1

# Podemos fazer busca dentro de um range, início/fim
print(numeros.index(8, 3, 6))  # buscar o valor 8, começando do indice 3 e finalizando no indice 6

# Revisão do slicing

# Lista[inicio:fim:passo] OBS: Pode passar valores negativos para o programa
# range(inicio:fim:passo)

# Trabalhando com o slicing de listas com o parâmetro 'início'

lista = [1, 2, 3, 4]

print(lista[1:])  # podendo passar valores negativos também

# Trabalhando com o slicing de listas com o parâmetro 'fim'

print(lista[:2])  # começa em 0, vai até o indice 2 - 1

print(lista[:4])  # começa em 0, vai até o indice 4 - 1

print(lista[1:3])  # começa em 1, vai até o indice 3 - 1

# Trabalhando com o slicing de listas com o parâmetro 'passo'

print(lista[1::2])  # começa em 1, vai até fim de 2 em 2

print(lista[0::2])  # começa em 0, vai até fim de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista), max(lista), min(lista), len(lista))

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos value error
# também é válido para a operação reversa

# Copiando uma lista para outra (Shallow copy and Deep copy
# Forma 1 -  Deep Copy:
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista mas elas ficaram totalmente
# independentes, isso em Python é chamado de Deep Copy

# Forma 2 - Shallou copy

lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que na Shallow copy a alteração da lista copiada também altera a lista original.

"""

