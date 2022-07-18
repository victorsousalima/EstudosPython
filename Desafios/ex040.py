n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

m = (n1 + n2) / 2
print(f'Sua média é: {m}')

if m < 5:
    print('Você está Reprovado!')
elif m >= 5 and m < 7:
    print('Você está de Recuperação!')
elif m >= 7:
    print('Parabéns, Você está Aprovado!')
elif m > 10 and m < 0:
    print('Média Invalida')