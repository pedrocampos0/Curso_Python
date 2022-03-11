"""
Listas aninhadas

- Algumas linguages de programação (C/java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais ( arrays/vetores );
    - multidimensionais (matrizes);


Em python nós temos as listas

numeros = [1, 'b1, 3.234, True, 5]

# EXEMPLOS

listas = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)
print(type(listas))

print(listas[0][1])
print(listas[2][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)


listas = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

# List comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Outros exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha =  [['X' if numero % 2 == 0 else 'O' for numero in range (1,4)] for valor in range(1,4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range (1,4)] for j in range (1,4)])