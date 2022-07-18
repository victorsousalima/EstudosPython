pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(pt, r*10, r):
    pt += r
    print(pt, end=' --> ')
print('Fim')
