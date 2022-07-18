qm = 0
sm = 0
hm = 0
ih = 0
nhm = ''

for c in range(0, 4):
    n = input('Seu nome: ')
    i = int(input('Sua idade: '))
    print('[M]- Masculino'
          '[F]- Feminino')
    s = input('Sexo: ')

    sm += i

    if s == 'M':
        ih = i
        if ih > hm:
            hm = ih
            nhm = n

    if s == 'F' and i < 20:
        qm += 1
m = sm / 4

print(f'A média de Idade do Grupo é: {m}')
print(f'O homem mais velho tem {hm} anos e seu nome é {nhm}')
print(f'Foram registrado {qm} mulheres com menos de 20 anos!')