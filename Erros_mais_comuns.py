"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreevu algo que o Python não
reconhece como parte da linguagem.

Exemplos:
a)

def funcao:
    print('Geek University')

b)
 def = 1

c)

return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
print(geek)

b)
geek()

c)
a = 18

if a < 10:
    msg = 'é maior q 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[0[10]])

5 - ValueError -> Ocorre quando uma função/cooperação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

Exemplos ValueError

print(int('Geek'))

6 - keyError -> Ocorre quando tentamos acessar umd cionário com uma chave que não existe.

# Exemplos KeyError

dic = {}
print(dic['Geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
for i in range(10):
i + 1

print(i)

OBS: Exceptions e Erros são sinônimos na programação

OBS: Importante ler e prestar atenção na saída de erro
"""










