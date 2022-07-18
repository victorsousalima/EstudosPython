tot = pmm = smd = 0
pmb = 9999
npb = ''
while True:
    print('-'*30)
    print('LOJINHA DO KOND')
    print('-'*30)

    np = input('Nome do produto: ')
    pp = float(input('Preço: '))

    smd += pp

    if pp > 1000.00:
        pmm += 1

    if pp < pmb:
        pmb = pp
        npb = np

    s = ' '
    while s not in 'SN':
        s = input('Quer continuat [S/N]: ').upper()
    if s == 'N':
        break


print(f'O total gasto foi R${smd:.2f}')
print(f'O total de produtos que custam mais de R$1000 é {pmm}')
print(f'O produto mais barato foi {npb} custando R${pmb:.2f}')