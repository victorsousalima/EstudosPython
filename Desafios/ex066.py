s = 0
qt = 0
while True:
    n = int(input('Um valor (999 - Para parar) : '))
    if n == 999:
        break
    s += n
    qt += 1

print(f'A soma dos {qt} valores digitados foi {s}')
print('Fim!')
