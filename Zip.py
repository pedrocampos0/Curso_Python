"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento a cada um dos iteráveis passados como entrada em apres.

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)

# Sempre podemos gerar uma lista, tupla, ou dicioniário

print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a':11, 'b':12, 'c':13, 'd':14, 'e':15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]

print(list(zip(*dados)))

"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# utilizando o map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))