"""
Sorted

Podemos utilizzar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve apra odernar.
"""

# Exemplos

numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))

# Adicionando parãmetros ao sorted()[

print(sorted(numeros, reverse=True))  # Do maior para o menor

# Exemplos complexos

usuarios = [
    {'username': 'samuel', 'tweets': ['eu adoro bolos','eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['eu gosto de cachorros', 'vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]

# Odernando pelo username
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Odernando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
