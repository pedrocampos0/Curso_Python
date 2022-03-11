"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos conjuntos de Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Ditos isto,d a mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenaçãod deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto caso seja adicionado um valor existente, o mesmo será ignorado sem gerar erros e não fará
# parte do conjunto

# Forma 2 - Mais comum:

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está em um conjunto

if 3 in s:
    print('Tem o três')
else:
    print('Não tem o três')

# Importante lembrar que, além de não termos valores duplicadosm, não temos ordem

# Listas aceitam valores duplicados.
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados.
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas (8 elementos)
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados (8 elementos)
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes em Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamo cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter
# epetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo grande', 'Cuiabá', 'Campo grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas ou seja únicas, temos.

# Oque você faria?

# Podemos utilizar o Set para isso

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)
print(s)

# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # não é índice, é valor
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado nenhum erro é gerado.

# Copiando um conjunto para outro

# Forma 1 de cópia - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(s)
print(novo)

# Forma 2 - shallow copy

novo = s

novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()

# Métodos matemáticos de conjunto

# Imagine que temos dois conjuntos, 1 contendo estudanmtes do curso Python e o outro contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando Union

u = estudantes_python.union(estudantes_java)
print(u)

# Forma 2 - Utilizando o caractere pipe |

u2 = estudantes_python | estudantes_java
print(u2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos = estudantes_python.intersection(estudantes_java)
print(ambos)

# Forma 2 - Utilizando &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudando que estão só em um curso

so_py = estudantes_python.difference(estudantes_java)
print(so_py)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# Soma, maior valor, menor valor e tamanho de um conjunto

s = {1, 2, 3, 4, 5, 6}

print(f'a soma é {sum(s)}')
print(f'o valor máx é {max(s)}')
print(f'o valor min é {min(s)}')
print(f'o tamanho é {len(s)}')
