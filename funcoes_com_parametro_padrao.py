"""
Funções com Default Parameters
- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parametro seja obrigatório:

def quadrado(numero):
    return numero * numero


print(quadrado(2))
print(quadrado()) #TypeError

def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3))  # Por padrão eleve ao quadrado

# OBS
# Se o usuário passar somente 1 argumente, este será atribuido ao parâmetro numero, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo a o parãmetro potencia. Então
# será calculada esta potêcia

#OBS: Em funções Python os parâmetros com valores default DEVEM sempre estar ao final da declaração

# Outros exemplos

def soma(num1=2, num2=3):
    return num1+num2

print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TypeError

# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor geek!'
    elif nome == 'Geek':
        return 'Eu pensei q vc era instrutor'
    else:
        return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# Pq utilizar defaul parameters?
# Nos permite ser mais flexíveis nas funções
# Evita erros com parâmetros incorretos;
# Nos permite trabalhar com exemplos mais legíveis de código;

#Podemos usar qualquer tipo de dados como default parameters

def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mat(num1, num2, fun_qualquer=soma):
    return fun_qualquer(num1, num2)


print(mat(2, 2))
print(mat(2, 2, sub))

# Escopo - Evitar problemas e confusões
# Variáveis globais
# Variáveis locais

instrutor_global = 'Geek'  # vairável global

def diz_oi():
    instrutor_local = 'Python'
    return f'oi {instrutor_local}'
    return f'oi {instrutor_global}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

def diz_oi():
    prof = 'geek' # variavel local
    return f'olá {prof}'

print(diz_oi())
print(prof)    #NameError

total = 0

def incrementa():
    total = total + 1   # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido
    inicializada)
    return total

print(incrementa())

# ATENÇÃO COM VARIÁVEIS GLOBAIS (se puder evitar, evite!)

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1  # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido
    # inicializada)
    return total


for n in range(1, 4):
    print(incrementa())

"""


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador

    return dentro()


for n in range(1, 4):
    print(fora())
