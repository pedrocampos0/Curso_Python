"""
Ranges

- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não incluso e início padrão 0 e passo de 1 em 1

for num in range(11):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não incluso e início especificado pelo usuário e passo de 1 em 1

for num in range(1,11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não incluso, início e passo especificados pelo usuário

for num in range(1,11,2):
    print(num)

# Forma 4 (inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não incluso, início e passo especificados pelo usuário

for num in range(10, 0, -1):
    print(num)

"""



