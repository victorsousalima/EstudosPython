qa = 0
qm = 0

for c in range(0, 7):
    an = int(input('Ano em que nasceu: '))

    if 2022 - an > 18:
        qa += 1
    elif 2022 - an < 18:
        qm += 1
print(f'Foram digitados {qa} pessoas maiores de idade!')
print(f'Foram digitados {qm} pessoas menores de idade!')