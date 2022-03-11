"""
Módulo Collection - Named Tuple

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple ->  São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros.
"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração namedtuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração namedtuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# forma 1

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# forma 2

print(ray.idade)
print(ray.raça)
print(ray.nome)


print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
