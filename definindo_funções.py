"""Definindo funções

 - Funções são pequenas partes de código que realizam tarefas específicas;
 - Pode ou não receber entradas de dados e retonar uma sáida de dados;
 - Muito úteis para executar procedimentos similares por repetidas vezes;

 OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
 é bom fazer uma verificação para que a função seja simplificada.

"""

# Exemplo de utilização de funções:
# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizandos a função integada (Built-in) do python print()

# print(cores)

"""
Em python a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função
    
Onde:

nome_da_funcao -> SEMPRE, com letras minbúsculas, e se for nome composto, separado por underline (Snake Case):
parâmetros_de_entrada -> São opcionais, onde tendo mais de um, cada um é separado por vígulas, podendo ser opcionais 
ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco do código com o já conhecido dois pontos: Que é utilizado em Python para definir 
bloco.
"""


# Definindo a primeira função

def diz_oi():
    print('oi!')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, que é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada; 
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

diz_oi()
"""


def cantar_parabens():
    print('parabéns p vc')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('viva o aniversariante')


cantar_parabens()

# Em python podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens()

canta()
