"""
T = int(input())
contador = 0
soma = 0
lista = []
v_final = 0
i = 0
while contador != T:
    i = 0
    lista.clear()
    A, N = input().split()
    A, N = [int(A), int(N)]
    lista.append(A)
    while i != N:
        A = A + 1
        lista.append(A)
        i = i + 1
    lista.pop()
    soma = sum(lista)
    v_final = ' '.join(map(str, lista))
    print(f'{v_final}', end=f'\n{soma}\n')
    contador = contador + 1


N = int(input())
contador = 0
lista = []
soma_impares = []
i = 0

while contador != N:
    i = 0
    lista.clear()
    X, Y = input().split()
    X, Y = [int(X), int(Y)]
    if X % 2 != 0:
        lista.append(X)
    while i != Y:
        X = X + 1
        if X % 2 != 0:
            lista.append(X)
        i = i + 1
    print(lista)
    print(sum(lista))
    soma_impares.append(sum(lista))
    contador = contador + 1

media_somas = 0
print(f'{max(soma_impares)} \n{min(soma_impares)} \n{((max(soma_impares)+min(soma_impares))/2):.2f}')


N = int(input())
contador = 0
soma = 0
lista = []
soma_impares = []
i = 0

while contador != N:
    i = 0
    lista.clear()
    X, Y = input().split()
    X, Y = [int(X), int(Y)]
    if X % 2 != 0:
        lista.append(X)
    while i != Y:
        X = X + 1
        if X % 2 != 0:
            lista.append(X)
            i = i + 1
    if Y != len(lista):
        lista.pop()
    print(lista)
    print(sum(lista))
    soma_impares.append(sum(lista))
    contador = contador + 1

print(f'{max(soma_impares)} \n{min(soma_impares)} \n{((max(soma_impares)+min(soma_impares))/2):.2f}')
"""
x = int(array = {1,2,3,4,5})
print(x[4])