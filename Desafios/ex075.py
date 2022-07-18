t = (int(input('Digite um Valor: ')),
     int(input('Digite mais um Valor: ')),
     int(input('Digite outro Valor: ')),
     int(input('Digite mais outro Valor: ')))


print(f'O número 9 apareceu {t.count(9)} vezes!')
if t.count(3) != 0:
    print(f'O valor 3 foi digitado na {t.index(3)+1}o posição')
else:
    print('O valor 3 não foi encontrado!')
print('Os valores pares são: ', end=' ')
for c in range(0, len(t)):
    if t[c] % 2 == 0:
        print(t[c], end=' ')
