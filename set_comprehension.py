"""
Set comprehension
"""
# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)

numeros_dict = {x: x ** 2 for x in range(10)}
print(numeros_dict)

 # Pra finalizar

letras = {letra for letra in 'Geek University'}
print(letras)
