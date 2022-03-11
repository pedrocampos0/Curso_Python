"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Importando
from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionando elementos no deq

deq.append('y')  # Adiciona no final

print(deq)

deq.appendleft('k')

print(deq)

# Removendo elementos

print(deq.pop())

print(deq.popleft())

print(deq)