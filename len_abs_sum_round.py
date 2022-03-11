"""
Len, Abs, Sum, Round

# Len

len() -> retorna o tamanho de um iterável

print(len('Geek University'))

# Por debaixo dos panos, o python faz o seguinte:
# Dunder len
print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(3.14))

# Sum

sum()-> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos.

#OBS: O valor inicial default = 0

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))

print(sum([3.145, 5.678]))

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa deciaml. Se a precisão não for
informada retorna o inteiro mais próximo da entrada
"""
# Exemplos round

print(round(10.2))

print(round(10.5))

print(round(1.2121212121, 2))






