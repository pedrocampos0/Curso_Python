"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários:
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto a chave como o valor podem ser de qualquer tipo de dado.
    - Podemos misturar tipos de dados

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado um KeyError

pais = paises.get('ru')

if russia:
    print(f'Encontrei o país{pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado, inclusive lista, tupla, dicionário, como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são
# imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (35.6895, 74.0060): 'Escritório em Nova York',
    (35.6895, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atulizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum:

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS: Aqui precisamos sempre informar a chave e caso não encontre o elemento um KeyError é retornado.
# OBS 2: Ao remover um objeto, o valor desse objeto é sempre retornado.

# Forma 2:

del receita['fev']

print(receita)

# OBS 2: Ao remover um objeto, o valor desse objeto não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
    - nome;
    - quantidade;
    - preço;
    Produto 2:
    - nome;
    - quantidade;
    - preço;


# 1 - Poderiamos utilizar uma lista para isso:

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla:

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionário:
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

# Copiando um dicionário para outro.

# Forma 1 -  Deep copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'valor')
print(veja)