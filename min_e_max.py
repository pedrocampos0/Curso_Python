"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario))  # f

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(max(dicionario.values()))  # 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

min() -> Retonar o menor valor em um iterável ou o menor de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(min(dicionario))

dicionario = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':129}
print(min(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(in(val1, val2))
"""

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))
