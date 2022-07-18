s = float(input('Qual seu sálario: '))

print(f'Seu sálario é {s}')

if s > 1250.00:
    sf = s + (s * 0.10)
    print(f'Você ganhou um Aumento de 10%, Seu sálario agora é {sf}')
else:
    sf = s + (s * 0.15)
    print(f'Você ganhou um Aumento de 15%, Seu sálario agora é {sf}')

print('Fim')