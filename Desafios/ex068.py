from random import randint
while True:
    c = randint(0, 10)
    print('-'*30)
    n = int(input('Um número: '))
    pi = input('Par ou Impar[P/I]: ').upper()

    s = c + n

    if s % 2 == 0:
        print('-'*30)
        print(f'Você jogou {n} e o computador {c}, a soma deu {s}, então é PAR')
        if pi == 'P':
            print('-'*30)
            print('Você Ganhou')
            print('Vamos Jogar Novamente...')
        elif pi == 'I':
            print('-'*30)
            print('Você Perdeu!')
            break
    else:
        print('-'*30)
        print(f'Você jogou {n} e o computador {c}, a soma deu {s}, então é IMPAR')
        if pi == 'I':
            print('-'*30)
            print('Você Ganhou')
            print('Vamos Jogar Novamente...')
        elif pi == 'P':
            print('-'*30)
            print('Você Perdeu')
            break
print('Fim!')