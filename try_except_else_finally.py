"""
Try / Except / Else / Finally

Toda entrada deve ser tratada!

num = 0

try:
    num = int(input())
except ValueError:
    print('Valor incorreto')
if num > 0:
    print(f'Você digitou {num}')

# Exepmlo mais correto

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""

# Exepmlo - semi genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

