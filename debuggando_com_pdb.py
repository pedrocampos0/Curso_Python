"""
Debuggando com PDB

PDB -> Python Debugger

# Print para debuggar código não é o idela para debuggar o código

# Exemplo com o PyChar

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


print(dividir(4, 0))

# Exemplo com o PDB  Importar a biliooteca pdb e utilizar a função set_trace()
# Comandos básico do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
"""

nome = 'angelina'
sorbenome = 'jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sorbenome
curso = 'Programação em Python Essencial'
final = nome_completo = ' faz o curso ' + curso
print(final)
