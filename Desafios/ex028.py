import random

nc = random.randint(0, 5)

n = int(input('Digite um número de 0 a 5: '))

if n == nc:
    print('Parabéns, você acertou o número {} que o computador digitou {}'.format(n, nc))
else:
    print('Você errou, vc digitou {} e o pc {}'.format(n, nc))

print('Fim')

