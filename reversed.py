"""
Reversed

Diferença entre reverse() e reversed():

Reverse() -> Funciona apemas com listas

Reversed() -> Funciona com qualuer iterável
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para outro tipo de dado:

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek university'))))

# Utilizando o slice de strings
print('Geek University'[::-1])

# Loop for reverso
for n in reversed(range(0, 10)):
    print(n)

for n in range(9, -1, -1):
    print(n)