from random import randint

ex = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

ma = 0
me = 99

for c in range(0, len(ex)):
    if ex[c] > ma:
        ma = ex[c]

    if ex[c] < me:
        me = ex[c]


print(f'Os números sorteados foram: {ex}')
print(f'O maior número sorteado foi: {ma}')
print(f'O menor número sorteado foi: {me}')