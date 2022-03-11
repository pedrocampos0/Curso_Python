"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
de acordo com a função

import statistics

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# Assim como a função map90, a filter() recebe dois parãmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

paises = ['', 'argentina', '', 'brasil', 'chile', '', 'colombia', '', 'equador', '', '', 'venezuela']

print(paises)

# filter(lambda pais: pais != '', paises)
res = filter(None, paises)

print(list(res))

"""

# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['eu adoro bolos','eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['eu gosto de cachorros', 'vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

print(usuarios)

# filtrar os usuários que estão inativos no twitter

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)
