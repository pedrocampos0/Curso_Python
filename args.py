"""
Entendendo o *args

- O *args é um parãmentro como um outro qualquer, isso significa que você poderá chamar de qualquer coisa, desde que
comece com *.

Ecemplo:

*xis

Mas por convenção, utilizamos *args apra definí-lo

Mas o que é o *args utilizado em uma função, coloca os valores extras informados em uma tupla.
Então lembre-se que tuplas são imutáveis

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 7))

# Entendo o args

def soma_todos_numeros(*args):
    #total = 0
    #for numero in args:
    #    total = total + numero
    #print(total)
    print(sum(args))


soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2.2, 3)
soma_todos_numeros(3, 4, 5, 6)

def verifica(*args):
    if 'Geek' in args and 'University' in args:
        print('Bem-Vindo geek!')
        return 0
    else:
        print('Não sei quem é você...')
        return 0


verifica()
verifica(1, True, 'University', 'Geek')

"""


# Outro exemplo de utilização do args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1, 4, 5, 6, 7))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

# num1, num2, num3, num4, num5, num6,  = numeros
print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará antes desempacotar estes dados.
