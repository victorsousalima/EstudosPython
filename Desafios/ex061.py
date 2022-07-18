pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

c = 1
while c <= 10:
    pt += r
    print(pt, end=' ')
    c += 1
print('Fim!')