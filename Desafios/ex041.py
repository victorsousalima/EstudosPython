an = int(input('Ano de Nascimento: '))

id = 2022 - an

if id <= 9:
    print(f'Você tem {id} anos ou seja, Sua Categoria é Mirim!')
elif id <= 14:
    print(f'Você tem {id} anos ou seja, Sua Categoria é Infantil!')
elif id <= 19:
    print(f'Você tem {id} anos ou seja, Sua Categoria é Junior!')
elif id <= 20:
    print(f'Você tem {id} anos ou seja, Sua Categoria é Sênior!')
elif id > 20:
    print(f'Você tem {id} anos ou seja, Sua Categoria é Master!')