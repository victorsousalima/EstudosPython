p = float(input('Qual seu peso: '))
a = float(input('Qual sua altura em M: '))

imc = p / a ** 2

print(f'Seu imc é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Peso normal!')
elif imc > 25 and imc <= 30:
    print('Está com Sobrepeso')
elif imc > 30 and imc <=  40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
