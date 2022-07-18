from random import randint
t = 1
c = randint(0, 10)
vc = int(input('Advinhe o número: '))
while not vc == c:
    print('Tente Novamente')
    vc = int(input('Advinhe o número novamente: '))
    t += 1
print(f'Parabens! Você advinhou que o pc escolheu {c}, e foi em {t} tentativas')