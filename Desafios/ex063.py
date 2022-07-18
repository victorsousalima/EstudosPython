print('-'*30)
n = int(input('Um número: '))
print('-'*30)
t1 = 0
t2 = 1
print(f'{t1} {t2}', end=' ')
co = 3
while co <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    co += 1
print(' -> Fim!')