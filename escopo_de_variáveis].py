"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ouu seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar uma variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel


Python é uma linguagem de tipagem dinâmima. Isso significa que
ao declararmos uma variável, no´s não colocamos o tipo de dado dela.
Este tipe é inferido ao atribuirmos o valor à mesma.
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)


numero = 2
# novo = 0

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if. Portando é local.
    print(novo)

print(novo)
