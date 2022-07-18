e = 0
while e != 5:
    v1 = int(input('Primeiro Valor: '))
    v2 = int(input('Segundo Valor: '))

    print('[1] - Somar \n'
          '[2] - Multiplicar\n'
          '[3] - Maior\n'
          '[4] - Novos valores\n'
          '[5] - Sair\n')
    e = int(input('Qual você escolher: '))

    if e == 1:
        s = v1 + v2
        print(f'A soma é: {s}')
    if e == 2:
        m = v1 * v2
        print(f'A multiplicação entre esses dois números é: {m}')
    if e == 3:
        if v1 > v2:
            print(f'O {v1} é o maior!')
        else:
            print(f'O {v2} é o maior!')
    if e == 4:
        print('Você vai digitar novos valores então!')
print('Fim!')