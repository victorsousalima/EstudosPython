pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

re = 10
c = 1
tot = 0
while re != 0:
    tot += re
    while c <= tot:
        pt += r
        print(pt, end=' ')
        c += 1
    print('Pausa')
    re = int(input('\nQuer ver mais quantas progressões? se for 0 o programa encerra: '))
print(f'Total de termos mostrado: {tot}')
