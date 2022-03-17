'''Dosagem de medicamento
Crie um programa que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento e
apresenta a quantidade de gotas do medicamento que o paciente deve tomar por dose. Considere que o medicamento
em questão possui 500 mg por ml, e que cada ml corresponde a 20 gotas.
 • Adultos ou adolescentes desde 12 anos (inclusive) se tiverem peso igual ou acima de 60 quilos devem tomar 1000 mg
  e com peso abaixo de 60 quilos devem tomar 875 mg.
 • Para crianças ou adolescentes abaixo de 12 anos a dosagem é calculada pelo peso corpóreo conforme a tabela a
  seguir:
Peso Dosagem
5 kg a 9 kg 125 mg 
9.1 kg a 16 kg 250 mg
16.1 kg a 24 kg 375 mg
24.1 kg a 30 kg 500 mg
Acima de 30 kg 750 mg
             
Entrada:
Duas entradas, idade (em anos) e peso (em kg). A idade é do tipo inteiro e o peso do tipo float, inseridos nessa ordem e
na mesma linha, separados por espaço.
Saída:
Uma saida, sem casas decimais, correspondendo a quantidade de gotas de acordo com a dosagem em relação à idade e
ao peso, seguida da palavra "gotas". Caso o peso seja menor que 5.0 kg, o programa deve apresentar a mensage consulte o médico

while True:
    idade, peso = input().split()
    idade, peso = [int(idade), float(peso)]
    if idade >= 12 and peso >= 60:
        mg = 1000
    elif idade >= 12 and peso < 60:
        mg = 875
    elif peso < 5:
        print('consulte o medico')
        break
    elif idade < 12:
        if peso >= 5 and peso < 9:
            mg = 125
        elif peso >= 9 and peso < 16:
            mg = 250
        elif peso >= 16 and peso < 24:
            mg = 375
        elif peso >= 24 and peso < 30:
            mg = 500
        elif peso > 30:
            mg = 750
    print(f"{int((mg/500)*20)} gotas")
    break'''

sm = 0
si = 0
while True:
    m, i = input().split()
    m, i = [int(m), int(i)]
    sm = sm + m
    si = si + i
    if m == 0 and i == 0:
        break
sm = int((sm/4))
si = int((si/2))
print(f'{int(sm+si)}')
