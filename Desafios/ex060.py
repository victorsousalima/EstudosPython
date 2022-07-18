#Feito com o while

f = int(input('Fatorial de qual número: '))
c = f
cf = 1
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    cf *= c
    c -= 1

print(f'{cf}')

#Feito com o for

cf = 1

for d in range(f, 0, -1):
    print(f'{f}', end='')
    if f > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    cf *= f
    f -= 1
print(f'{cf}')
