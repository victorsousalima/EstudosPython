c = 0
s = 0
qt = 0
while c != 999:
    c = int(input('Um número (999- para parar): '))
    if c == 999:
        s -= 999
        qt -= 1
    s += c
    qt += 1
print(f'A soma dos {qt} números digitados é {s} !')