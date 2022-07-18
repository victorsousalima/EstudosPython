km = int(input('Quantos km você chegou: '))

print('Você chegou aos {} KM'.format(km))

if km > 80:
    ckm = km - 80
    cfk = ckm * 7.0
    print('Você ultrapassou os 80KM, Valor da multa por km é de R$7,00')
    print('Como você ficou {} Kms acima do limite, o Valor da Multa será R${:.2f}'.format(ckm, cfk))
else:
    print('Você está dentro do limite: ')

print('Fim')