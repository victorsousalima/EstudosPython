alt = float(input('Altura em M: '))
peso = float(input('Peso em KG: '))

imc = peso / (alt ** 2)
print(f'Seu Imc é: {imc:.2f}')

if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print('Você está com o Peso Normal')
elif imc > 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc > 30 and imc < 40:
    print('Você está com Obesidade')
elif imc > 40:
    print('Você está com Obesidade Mórbida')
else:
    print('Imc Inválido!')
