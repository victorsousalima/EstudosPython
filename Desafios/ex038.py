n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

if n1 > n2:
    print(f'O Primeiro Valor {n1} é maior que o Segundo Valor {n2}')
elif n2 > n1:
    print(f'O Segundo Valor {n2} é maior que o Primeiro Valor {n1}')
elif n1 == n2:
    print('O Valor {} e {} são IGUAIS'.format(n1, n2))
else:
    print('Valores Inválidos!')
