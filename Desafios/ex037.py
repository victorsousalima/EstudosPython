n = int(input('Digite um Valor: '))
c = int(input('Digite 1(Para Binário), 2(Para Octal) e 3(Para Hexadecimal): '))

if c == 1:
    print(f'O número {n} convertido para binário é {bin(n)}')
elif c == 2:
    print(f'O número  {n} convertido para Octal é {oct(n)}')
elif c == 3:
    print(f'O número {n} convertido para Hexadecimal é {hex(n)}')
else:
    print('Numero Inválido!')
