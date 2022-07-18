p = ('Lápis', 1.75,
     'Borracha', 2.00,
     'Caderno', 15.90,
     'Estojo', 25.00,
     'Transferidor', 4.20)

print('='*30)
print(f'{"Lista de Preço":^30}')
print('='*30)

for c in range(0, len(p)):
    if c % 2 == 0:
        print(f'{p[c]:.<30}', end='')
    else:
        print(f'R${p[c]:>7.2f}')

print('-'*30)