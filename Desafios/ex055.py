mp = 0
mep = 999

for c in range(0, 5):
    p = float(input('Seu peso é: '))

    if p > mp:
        mp = p
    elif p < mep:
        mep = p
print(f'O maior peso digitado foi: {mp}')
print(f'O menor peso digitado foi: {mep}')