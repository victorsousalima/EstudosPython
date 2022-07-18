m18 = hc = mm20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)

    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = input('Sexo [M/F]: ').upper()

    if i >= 18:
        m18 += 1

    if s == 'M':
        hc += 1

    if s == 'F' and i < 20:
        mm20 += 1

    c = ' '
    while c not in 'SN':
        c = input('Quer continuar [S/N]: ').upper()

    if c == 'N':
        break

print('==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Total de homens cadastrados: {hc}')
print(f'Total de mulheres com menos de 20 anos: {mm20}')