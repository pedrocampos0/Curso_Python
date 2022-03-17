"""
Levantando os próprios erros com raise

raise -> Lança exceções

Obs: o raise não é uma função. É uma paalvra reservada, assim como def ou qualquer outra em PPython.

Para simplificar, pense no raise com sendo útil para que possamos criar nsosas próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')
"""


# Exemplo

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f' A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('true', 'roxo')
