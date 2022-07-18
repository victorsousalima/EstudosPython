s = input('Digite seu sexo: [M/F] ').upper()
while s != 'M' and s != 'F':
    print('Digite novamente, apenas [M/F]')
    s = input('Digite seu sexo: ').upper()
print('Obrigado!')