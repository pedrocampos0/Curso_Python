"""
Generators
- Tuple Comprehension

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes

# Poderíamos ter feito utilizando generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# Lisst Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
"""

# Retorna a qtd de bytes em memória do elemento passado como parãmetro
from sys import getsizeof

print(getsizeof('Geek'))

lsit_comp = getsizeof([x * 10 for x in range(1000)])

gen = getsizeof(x * 10 for x in range(1000))
print(f'Generator: {gen} bytes, e List Comprehension: {lsit_comp}')

