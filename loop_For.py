"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""

nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)
"""
range(valor_inicial, valor_final)

Obs: O valor final não é inclusive.
"""
for numero in range(1, 10):
    print(f'{numero}')

"""
Enumerate:

((0,'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)
"""

for _, letra in enumerate(nome):
    print(letra)

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd):
    print(f'Imprimindo {n}')

"""
Emojis unicode: https://apps.timwthitlock.info/emoji/tables/unicode
"""
#Modificado: U0001F60D

for num in range(1,11):
    print('\U0001F60D' * num)
