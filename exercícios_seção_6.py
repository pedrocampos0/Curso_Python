"""
# 1)

for numero in range(3, 16, 3):
    print(numero)

# 2)
contagem = 0
for n in range(1, 101):
    print(n)
    contagem = contagem + 1
if contagem == 100:
    print('Primeira vez finalizada vamos para a próxima')
num = 1
while contagem < 301:
    while contagem < 201:
        print(num)
        num = num + 1
        contagem = contagem + 1
        if num == 101:
            print('Segunda vez finalizada vamos para a terceira e última')
            num = 0
            break
    print(num)
    num = num + 1
    contagem = contagem + 1

# 3)
ctg = 10
while ctg > -1:
    print(ctg)
    ctg = ctg - 1
    if ctg == -1:
        print('FIM!')
        break

# 4)
numero = 0
while numero < 100001:
    print(numero)
    numero = numero + 1000

# 5)
n = 0
soma = 0
for num in range(1,11):
    n = int(input('Digite um número: '))
    soma = soma + n
print(f'A soma dos seus números foi: {soma}')

# 6)
n = 0
soma = 0
média = 0
qtd = 0
for num in range(1,11):
    n = int(input('Digite um número: '))
    qtd = qtd + 1
    soma = soma + n
média = soma // qtd
print(f'A média dos seus números foi: {média}')

# 7)
n = 0
soma = 0
média = 0
qtd = 0
for num in range(1, 11):
    n = int(input('Digite um número: '))
    if n > 0:
        qtd = qtd + 1
        soma = soma + n
    else:
        print('Digite um número positivo, os negativos serão descartados')
média = soma // qtd
print(f'A média dos seus números foi: {média}')

# 8)
n = 0
numrecebido = 0
maiornum = 0
menornum = 0
for num in range(1,11):
    n = int(input('Digite um número: '))
    numrecebido = n
    if numrecebido > maiornum:
        maiornum = numrecebido
    elif numrecebido < menornum:
        menornum = numrecebido
print(f'O maior número é: {maiornum} e o menor é {menornum}')

# 9)
qtdnum = 0
numeros = 0
numimpar = []
stop = 0
while qtdnum != 1:
    qtdnum = int(input('Quantos números você irá digitar? Se quiser sair, digite "1"'))
    print('Irei mostrar todos os números ímpares ao final.')
    if qtdnum == 1:
        print(f'Seus números ímpares foram: {numimpar}')
        break
    for num in range(1, (qtdnum + 1)):
        numeros = int(input('Digite um número:'))
        if (numeros%2) != 0:
              numimpar.insert(num, numeros)
        elif numeros == 1:
            numimpar = numeros


"""
# 10)
qtdnum = 0
numeros = 0
somapar = 0
stop = 0
while qtdnum != 1:
    qtdnum = int(input('Digite mais de 50 números. Quantos números você irá digitar? Se quiser sair, digite "1"'))
    if qtdnum < 50:
        print('Digite mais de 50 números.')
        qtdnum = int(input('Quantos números você irá digitar? Se quiser sair, digite "1"'))
    print('Irei mostrar a soma de todos os números pares ao final.')
    if qtdnum == 1:
        print(f'A some dos primeros 50 números pares foi:: {somapar}')
        break
    for num in range(1, (qtdnum + 1)):
        numeros = int(input('Digite um número:'))
        if (numeros%2) == 0:
              somapar = somapar + numeros

