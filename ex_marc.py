"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela"""

lista = [0]

for i in range(0, 5):
    n = int(input())
    if lista[0] < n:
        lista.insert(0, n)
    elif lista[1] < n:
        lista.insert(1, n)
    elif lista[2] < n:
        lista.insert(2, n)
    elif lista[3] < n:
        lista.insert(3, n)
    elif lista[4] < n:
        lista.insert(4, n)

print(lista)


