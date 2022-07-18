while True:
    print('-' * 30)
    n = int(input('Qual tabuada quer ver? (um número negativo encerra!): '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        m = n * c
        print(f'{n} x {c} = {m}')

print('Programa encerrado!')