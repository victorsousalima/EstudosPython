s = 0
q = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        q += 1

print(f'A soma dos {q} valores impares de 1 a 500 é {s}')