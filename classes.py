"""
POO - Classes
Em PO0, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
     Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
    iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é a luminosidade dela e etc.

   Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum ue muito provavelmente
    iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
oimplementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em
maiúsculo. Se o nome for composto, utiliza-se as iniciais de amabas as palavras em maiúsculo, todas juntas.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
   pass


lamp = Lampada()

print(type(lamp))

valor = int('42')  # cast

print(help(int))

inteiro = Int()

