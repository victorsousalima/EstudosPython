dt = float(input('Qual a distância da viagem: '))

print(f'A Viagem é de {dt} Kms')

if dt <= 200.0:
    dtf = dt * 0.50
    print(f'A distância não passou dos 200 Kms O preço da Viagem é de R${dtf:.2f}')
else:
    dtf = dt * 0.45
    print(f'A distância passou dos 200 Kms O preço da Viagem é de R${dtf:.2f}')

print('Fim')
