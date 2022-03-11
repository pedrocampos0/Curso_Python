"""
List comprehension

nós podemos adicionar estruturas condicionais lógicas às nossa list comprehension

"""

# Exxemplos

numeros =[1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero%2==0]
impares = [numero for numero in numeros if numero%2!=0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par modulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# Exemplo 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)