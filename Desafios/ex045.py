import random

print('[0] Pedra \n'
      '[1] Tesoura \n'
      '[2] Papel')
v = int(input('Qual sua opção: '))
c = random.randint(0, 2)

#Empate
if v == 0 and c == 0:
    print('Empate, os dois escolheram Pedra!')
elif v == 1 and c == 1:
    print('Empate, os dois escolheram Tesoura!')
elif v == 2 and c == 2:
    print('Empate, os dois escolheram Papel!')
#Pedra e Tesoura
elif v == 0 and c == 1:
    print('Você escolheu Pedra e a máquina Tesoura')
    print('Você Ganhou')
elif v == 1 and c == 0:
    print('Você escolheu Tesoura e a máquina Pedra')
    print('Você Perdeu!')
#Tesoura e Papel
elif v == 1 and c == 2:
    print('Você escolheu Tesoura e a máquina Papel')
    print('Você Ganhou!')
elif v == 2 and c == 1:
    print('Você escolheu Papel e a máquina Tesoura')
    print('Você Perdeu!')
#Pedra e Papel
elif v == 2 and c == 0:
    print('Você escolheu Papel e a máquina Pedra')
    print('Você Ganhou!')
elif v == 0 and c == 2:
    print('Você escolheu Pedra e a máquina Papel')
    print('Você Perdeu!')
else:
    print('Opção Invalida!')