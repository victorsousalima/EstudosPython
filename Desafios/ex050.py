sp = 0
for c in range(0, 6):
    n = int(input('Um número: '))
    if n % 2 == 0:
        sp += n

print(f'O resultado da soma dos números pares é: {sp}')