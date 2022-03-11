"""
List Comprehension

-Utilizando list comprehension nós podemos gerar novas listas com dados processador a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)

# List comprehension vs loop

# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)


# List comprehension
print([numero*2 for numero in numeros])

# Outros exemplos

#1

nome = 'Geek university'

print([letra.upper() for letra in nome])


"""


# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme']

print([caixa_alta(amigo) for amigo in amigos])

#3

print([numero * 3 for numero in range(1, 10)])

#4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1,2,3,4,5]])