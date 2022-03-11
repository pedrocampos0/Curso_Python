"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop


O bloco while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplos:

num = 5

num < 5

"""

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# Obs: Em um loop while, é importante que cuidemos do critério de parada.

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou jéssica? ')
