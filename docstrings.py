"""
Documentando funções com docstrings
OBS: Podemos ter acesso a documentação de uma função em Python utilizando o métodos especial __doc__
"""

def diz_oi():

    """Uma função que retorna a string 'OI'!"""
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Funação que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Número que desejamos parar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'número' por 'potência'
    """
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3))  # Por padrão eleve ao quadrado