n = int(input('Digite um número: '))
q = 0
for c in range(1, n+1):
    if n % 1 == 0 and n % c == 0:
        print(f'\033[33m{c} \033[m', end=' ')
        q += 1
    else:
        print(f'\033[31m{c} \033[m', end=' ')
print(f'\nO número {n} é divisível {q} vezes')
if q == 2:
    print('Então ele é primo!!!')
else:
    print('Então ele não é primo!!')