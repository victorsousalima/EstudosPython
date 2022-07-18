from random import randint

pc = randint(0, 2)

print('[0]- Pedra\n'
      '[1]- Papel\n'
      '[2]- Tesoura  ')
v = int(input('Qual você escolhe: '))

print(f'Você escolheu {v} e a Máquina {pc}')

#Empate
if v == pc:
    print('Os dois escolheram a mesma opção!')
    print('Empate!!')

#Pedra e Tesoura
if v == 0 and pc == 2:
    print('Você escolheu Pedra e a máquina Tesoura')
    print('Você Ganhou!')
elif pc == 0 and v == 2:
    print('Você escolheu Tesoura e a máquina Pedra')
    print('Você Perdeu!')

#Pedra e Papel
if v == 1 and pc == 0:
    print('Você escolheu Papel e a máquina Pedra')
    print('Você Ganhou!')
elif pc == 1 and v == 0:
    print('Você escolheu Pedra e a máquina Papel')
    print('Você Perdeu!')

#Tesoura e Papel
if v == 2 and pc == 1:
    print('Você escolheu Tesoura e a máquina Papel')
    print('Você Ganhou!')
elif pc == 2 and v == 1:
    print('Você escolheu Papel e a máquina Tesoura')
    print('Você Perdeu!')
