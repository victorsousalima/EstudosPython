c = ''
s = 0
ma = 0
me = 999999
qt = 0

while c != 'N':
    n = int(input('Um número: '))

    s += n
    qt += 1

    if n > ma:
        ma = n

    if n < me:
        me = n

    c = input('Quer continuar [S/N]: ').upper()

m = s / qt
print(f'A média dos {qt} valores digitados é: {m}')
print(f'O maior número digitado foi {ma} , e o menor digitado foi {me} !')