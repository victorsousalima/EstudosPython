ex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
      'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


p = int(input('Um valor de 0 a 20: '))
while p > 20 or p < 0:
    p = int(input('Tente novamente. Um valor de 0 a 20: '))

print(f'você digitou o número {ex[p]}')