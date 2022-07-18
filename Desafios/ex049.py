m = 0
n = int(input('Qual tabuada você quer: '))

for c in range(1, 11):
    m = n * c
    print(f'{n} x {c} = {m}')
print('Fim!')